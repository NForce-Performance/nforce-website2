/* ==========================================================================
   NForce — nf-hero.js  (ijs-engine v2)
   Live ijsvlak in WebGL voor de hero's: laag camerastandpunt boven het ijs,
   de blauwe lijn, een face-offcirkel, schaatssporen en arenalicht dat in het
   ijs weerspiegelt. De camera glijdt langzaam over het ijs.

   Scherp en vloeiend:
   - De ijstextuur wordt één keer gebakken (GPU-ruis + getekende schaatssporen)
     en daarna met mipmaps gesampled: weinig rekenwerk per frame, geen flikkering.
   - Rendert op de echte pixeldichtheid (max 2×) en past de resolutie automatisch
     aan als een apparaat het niet bijhoudt (doel: 60 fps).
   - Belijning met anti-aliasing op basis van de pixelgrootte op het ijs.

   Gebruik: <section class="ice" data-ice="home|page" data-ice-seed="0..9">
              <canvas class="ice__canvas"></canvas> …
   Geen WebGL of prefers-reduced-motion: de poster (CSS-achtergrond) blijft
   staan, of er wordt één stilstaand frame gerenderd.
   ========================================================================== */
(function () {
  'use strict';

  var hosts = document.querySelectorAll('[data-ice]');
  if (!hosts.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------------- shaders */
  var VERT = 'attribute vec2 p; void main(){ gl_Position = vec4(p, 0.0, 1.0); }';

  /* Bakpass: naadloos herhalende ruis (periodiek rooster) in vier kanalen.
     R: wolkigheid · G: fijne structuur · B/A: kleine normaalverstoring x/z */
  var BAKE = [
    'precision highp float;',
    'uniform float uSize;',
    'float h(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }',
    'float n(vec2 p, float per){ vec2 i = floor(p); vec2 f = fract(p); vec2 u = f * f * (3.0 - 2.0 * f);',
    '  float a = h(mod(i, per)); float b = h(mod(i + vec2(1.0, 0.0), per));',
    '  float c = h(mod(i + vec2(0.0, 1.0), per)); float d = h(mod(i + vec2(1.0, 1.0), per));',
    '  return mix(mix(a, b, u.x), mix(c, d, u.x), u.y); }',
    'float fbm(vec2 uv, float per){ float v = 0.0; float a = 0.5;',
    '  for (int i = 0; i < 6; i++) { v += a * n(uv * per, per); per *= 2.0; a *= 0.5; } return v; }',
    'void main(){ vec2 uv = gl_FragCoord.xy / uSize;',
    '  gl_FragColor = vec4(fbm(uv, 4.0), fbm(fract(uv + 0.37), 16.0), fbm(fract(uv + 0.11), 6.0), fbm(fract(uv + 0.73), 6.0)); }'
  ].join('\n');

  var MAIN = [
    'precision highp float;',
    'uniform vec2 uRes; uniform float uTime; uniform vec2 uMouse; uniform float uGlide;',
    'uniform float uHorizon; uniform float uLights; uniform float uSeed; uniform float uFoX; uniform float uShade;',
    'uniform sampler2D uNoise; uniform sampler2D uMarks;',
    'const vec3 BLUE = vec3(0.494, 0.784, 1.0);',                         /* #7ec8ff */
    'float hash(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }',
    /* lijn met anti-aliasing: d = afstand in meters, w = halve breedte, px = pixelvoetafdruk */
    'float line(float d, float w, float px){ return clamp((w - abs(d)) / px + 0.5, 0.0, 1.0); }',
    'void main(){',
    '  vec2 uv = (gl_FragCoord.xy - 0.5 * uRes) / uRes.y;',
    '  float aspect = uRes.x / uRes.y;',
    '  vec3 ro = vec3(uMouse.x * 0.3 + sin(uTime * 0.04) * 0.2, 1.05 + uMouse.y * 0.04, 0.0);',
    '  vec3 rd = normalize(vec3(uv.x, uv.y - uHorizon, 1.35));',
    '  vec3 col = vec3(0.0);',
    '  float lb = aspect > 1.2 ? 0.36 : 0.04;',                          /* lichten rechts van de tekst */
    '  if (rd.y < -0.0005) {',
    '    float dist = -ro.y / rd.y;',
    '    vec3 pos = ro + rd * dist;',
    '    vec2 w = vec2(pos.x, pos.z + uGlide);',
    '    float pxX = dist / (uRes.y * 1.35);',                             /* pixel in meters, dwars */
    '    float pxZ = pxX * dist / max(ro.y, 0.2);',                       /* pixel in meters, in de diepte */
    '    float fade = smoothstep(58.0, 6.0, dist);',
    '    vec4 nz = texture2D(uNoise, w * 0.018);',
    '    float fine = texture2D(uNoise, w * 0.21).g;',
    '    float marks = texture2D(uMarks, w * vec2(0.055, 0.055) + uSeed * 0.37).r * smoothstep(34.0, 2.0, dist);',
    '    vec3 ice = vec3(0.016, 0.020, 0.025) + vec3(0.034, 0.042, 0.050) * nz.r + vec3(0.012) * fine;',
    '    ice += vec3(0.070, 0.078, 0.088) * marks;',
    /* belijning: blauwe lijn op 8 m, face-offcirkel 6 m verder, herhaalt elke 44 m */
    '    float soft = 0.82 + 0.18 * fine;',
    '    float zb = mod(w.y - 8.0 + 22.0, 44.0) - 22.0;',
    '    float blue = line(zb, 0.15, pxZ * 1.2);',
    '    vec2 fo = vec2(w.x - uFoX, mod(w.y - 14.0 + 22.0, 44.0) - 22.0);',
    '    float r = length(fo);',
    '    float pxC = mix(pxX, pxZ, abs(fo.y) / max(r, 0.001));',
    '    float circle = line(r - 4.57, 0.03, pxC);',
    '    float spot = line(r, 0.3, pxC);',
    '    float hashes = line(abs(fo.y) - 0.9, 0.03, pxZ) * step(4.57, abs(fo.x)) * step(abs(fo.x), 5.2);',
    '    float white = max(max(circle, spot * 0.8), hashes);',
    '    ice = mix(ice, BLUE * 0.55, blue * soft * 0.92);',
    '    ice = mix(ice, vec3(0.60, 0.64, 0.68), white * soft * 0.6);',
    /* glad ijs: zachte, uitgerekte reflecties van verre lichtrijen */
    '    vec2 nn = texture2D(uNoise, w * vec2(0.012, 0.045)).ba - 0.5;',
    '    vec3 nrm = normalize(vec3(nn.x * 0.07 + (fine - 0.5) * 0.012, 1.0, nn.y * 0.07));',
    '    vec3 rf = reflect(rd, nrm);',
    '    float spec = 0.0;',
    '    for (int i = 0; i < 3; i++) { for (int j = 0; j < 2; j++) {',
    '      float lz = 70.0 + float(j) * 40.0 - mod(uGlide * 2.0, 40.0);',
    '      vec3 L = vec3((lb + 0.13 * float(i)) * lz / 1.35 + ro.x, 6.0, lz);',
    '      vec3 ld = normalize(L - pos);',
    '      vec2 dd = (rf.xy - ld.xy) / vec2(0.010, 0.050);',
    '      float lw = smoothstep(30.0, 40.0, lz) * smoothstep(110.0, 100.0, lz);',   /* geen sprong bij herhaling */
    '      spec += (exp(-dot(dd, dd)) * 0.75 + exp(-dot(dd, dd) * 0.08) * 0.05) * lw;',
    '    } }',
    '    spec *= uLights * (aspect > 1.2 ? 1.0 : 0.4);',
    '    float sheen = exp(-abs(rf.y - 0.035) * 30.0) * 0.05;',
    '    col = ice + vec3(0.78, 0.86, 0.94) * spec * fade + vec3(0.55, 0.62, 0.70) * sheen;',
    '    col *= 0.25 + 0.75 * fade;',
    '  }',
    /* verre arenalampen boven de horizon */
    '  for (int i = 0; i < 3; i++) {',
    '    vec3 L = normalize(vec3((lb + 0.13 * float(i)) * 110.0 / 1.35, 6.0 - ro.y, 110.0));',
    '    vec2 dl = (rd.xy - L.xy) / vec2(0.012, 0.008);',
    '    col += vec3(0.75, 0.83, 0.92) * exp(-dot(dl, dl)) * 0.18 * uLights;',
    '  }',
    '  col += vec3(0.04, 0.05, 0.06) * exp(-abs(rd.y + 0.004) * 42.0);',
    /* ruimte voor de tekst links en een rustige vignet */
    '  col *= mix(0.12, 1.0, smoothstep(-0.9, 0.45, uv.x / max(aspect * 0.5, 0.9) * 0.9));',
    /* subpagina's: tekstvlak links extra rustig */
    '  float sx = gl_FragCoord.x / uRes.x;',
    '  col *= mix(1.0, mix(0.2, 1.0, smoothstep(0.2, 0.7, sx)), uShade);',
    '  col *= 1.0 - 0.5 * dot(uv * vec2(0.5 / max(aspect * 0.55, 1.0), 0.9), uv * vec2(0.5 / max(aspect * 0.55, 1.0), 0.9));',
    '  col = pow(max(col, 0.0), vec3(0.9));',
    /* fijne filmkorrel */
    '  col += (hash(gl_FragCoord.xy + fract(uTime * 7.13) * 91.0) - 0.5) * 0.018;',
    '  gl_FragColor = vec4(col, 1.0);',
    '}'
  ].join('\n');

  /* ------------------------------------------------------ schaatssporen (2D) */
  function drawMarks(size, seed) {
    var c = document.createElement('canvas');
    c.width = c.height = size;
    var x = c.getContext('2d');
    x.fillStyle = '#000';
    x.fillRect(0, 0, size, size);
    var s = seed || 1;
    function rnd() { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }
    function arc(cx, cy, r, a0, a1, lw, alpha) {
      for (var ox = -1; ox <= 1; ox++) {
        for (var oy = -1; oy <= 1; oy++) {
          x.beginPath();
          x.arc(cx + ox * size, cy + oy * size, r, a0, a1);
          x.lineWidth = lw;
          x.strokeStyle = 'rgba(255,255,255,' + alpha + ')';
          x.stroke();
        }
      }
    }
    var i, cx, cy, r, a0;
    /* lange, rustige bochten */
    for (i = 0; i < 170; i++) {
      cx = rnd() * size; cy = rnd() * size; r = 80 + rnd() * 520; a0 = rnd() * Math.PI * 2;
      arc(cx, cy, r, a0, a0 + 0.2 + rnd() * 0.9, 0.5 + rnd() * 1.1, (0.05 + rnd() * 0.16).toFixed(3));
    }
    /* korte, scherpe stops en crossovers: bundels van parallelle sporen */
    for (i = 0; i < 26; i++) {
      cx = rnd() * size; cy = rnd() * size; r = 30 + rnd() * 90; a0 = rnd() * Math.PI * 2;
      var span = 0.3 + rnd() * 0.6, k = 3 + Math.floor(rnd() * 5);
      for (var j = 0; j < k; j++) arc(cx, cy, r + j * 1.6, a0, a0 + span, 0.6, (0.06 + rnd() * 0.12).toFixed(3));
    }
    return c;
  }

  /* ------------------------------------------------------------- per host */
  function start(host) {
    var canvas = host.querySelector('.ice__canvas');
    if (!canvas) return;
    var gl = null;
    try {
      gl = canvas.getContext('webgl', { antialias: false, alpha: false, premultipliedAlpha: false, powerPreference: 'high-performance' }) ||
           canvas.getContext('experimental-webgl');
    } catch (e) { gl = null; }
    if (!gl) return;

    function compile(type, src) {
      var sh = gl.createShader(type);
      gl.shaderSource(sh, src);
      gl.compileShader(sh);
      if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(sh));
      return sh;
    }
    function program(fs) {
      var p = gl.createProgram();
      gl.attachShader(p, compile(gl.VERTEX_SHADER, VERT));
      gl.attachShader(p, compile(gl.FRAGMENT_SHADER, fs));
      gl.linkProgram(p);
      if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
      return p;
    }
    var bakeProg, mainProg;
    try { bakeProg = program(BAKE); mainProg = program(MAIN); }
    catch (err) { if (window.console) console.warn('NForce ijs: WebGL uit, poster blijft staan.', err); return; }

    var buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    function bindQuad(p) {
      var loc = gl.getAttribLocation(p, 'p');
      gl.enableVertexAttribArray(loc);
      gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
    }

    var aniso = gl.getExtension('EXT_texture_filter_anisotropic') ||
                gl.getExtension('WEBKIT_EXT_texture_filter_anisotropic') ||
                gl.getExtension('MOZ_EXT_texture_filter_anisotropic');
    function texParams() {
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.REPEAT);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      if (aniso) {
        var max = gl.getParameter(aniso.MAX_TEXTURE_MAX_ANISOTROPY_EXT) || 1;
        gl.texParameterf(gl.TEXTURE_2D, aniso.TEXTURE_MAX_ANISOTROPY_EXT, Math.min(8, max));
      }
    }

    /* 1. ruistextuur bakken op de GPU */
    var SIZE = 1024;
    var noiseTex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, noiseTex);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, SIZE, SIZE, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
    texParams();
    var fb = gl.createFramebuffer();
    gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, noiseTex, 0);
    gl.viewport(0, 0, SIZE, SIZE);
    gl.useProgram(bakeProg);
    bindQuad(bakeProg);
    gl.uniform1f(gl.getUniformLocation(bakeProg, 'uSize'), SIZE);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    gl.bindTexture(gl.TEXTURE_2D, noiseTex);
    gl.generateMipmap(gl.TEXTURE_2D);

    /* 2. schaatssporen tekenen en uploaden */
    var marksTex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, marksTex);
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, drawMarks(SIZE, 7 + (+host.getAttribute('data-ice-seed') || 0)));
    texParams();
    gl.generateMipmap(gl.TEXTURE_2D);

    /* 3. hoofdprogramma */
    gl.useProgram(mainProg);
    bindQuad(mainProg);
    var U = {};
    ['uRes', 'uTime', 'uMouse', 'uGlide', 'uHorizon', 'uLights', 'uSeed', 'uFoX', 'uShade', 'uNoise', 'uMarks'].forEach(function (k) {
      U[k] = gl.getUniformLocation(mainProg, k);
    });
    gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, noiseTex); gl.uniform1i(U.uNoise, 0);
    gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, marksTex); gl.uniform1i(U.uMarks, 1);

    var variant = host.getAttribute('data-ice') || 'home';
    var seed = +host.getAttribute('data-ice-seed') || 0;
    gl.uniform1f(U.uHorizon, variant === 'page' ? 0.22 : 0.14);
    gl.uniform1f(U.uLights, 1.0);
    gl.uniform1f(U.uSeed, seed);
    /* home: cirkel vlak rechts van de camera; subpagina's: verder naar rechts,
       zodat de lijnen niet door de korte tekstkolom lopen */
    gl.uniform1f(U.uFoX, variant === 'page' ? 7.4 : 4.2);

    /* dynamische resolutie: begin op de echte pixeldichtheid, zak als het
       apparaat de 60 fps niet haalt, klim weer als er ruimte is */
    var MAXQ = Math.min(window.devicePixelRatio || 1, 2);
    var quality = MAXQ, MINQ = Math.min(0.75, MAXQ);
    function resize() {
      var w = Math.max(1, Math.round(canvas.clientWidth * quality));
      var h = Math.max(1, Math.round(canvas.clientHeight * quality));
      if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; }
      gl.viewport(0, 0, canvas.width, canvas.height);
    }

    var mouse = { x: 0, y: 0 }, target = { x: 0, y: 0 };
    host.addEventListener('pointermove', function (e) {
      var r = host.getBoundingClientRect();
      target.x = ((e.clientX - r.left) / r.width) * 2 - 1;
      target.y = ((e.clientY - r.top) / r.height) * 2 - 1;
    });

    var t0 = performance.now(), last = t0, raf = 0, visible = true;
    var glide = seed * 11.0, samples = [], sinceChange = 0, warm = 20, ceil = MAXQ;
    function frame(now) {
      raf = 0;
      var dt = Math.min(0.1, (now - last) / 1000);
      last = now;
      if (!reduce) glide += dt * 0.18;
      /* resolutie bijsturen op de gemeten frametijd. Kosten schalen met het
         aantal pixels (kwaliteit²), dus één stap is meestal genoeg. Omhoog pas
         na 4 s stabiel op 60 fps, en nooit boven een eerder te zware stand. */
      if (!reduce && warm-- <= 0) {
        samples.push(dt);
        sinceChange++;
        if (samples.length > 24) samples.shift();
        if (samples.length === 24) {
          var avg = samples.reduce(function (a, b) { return a + b; }, 0) / samples.length;
          if (avg > 0.021 && quality > MINQ && sinceChange > 24) {
            ceil = quality * 0.97;
            quality = Math.max(MINQ, quality * Math.max(0.6, Math.sqrt(0.0167 / avg)));
            samples = []; sinceChange = 0;
          } else if (avg < 0.0175 && quality < ceil && sinceChange > 240) {
            quality = Math.min(ceil, quality * 1.1);
            samples = []; sinceChange = 0;
          }
        }
      }
      resize();
      mouse.x += (target.x - mouse.x) * 0.05;
      mouse.y += (target.y - mouse.y) * 0.05;
      gl.uniform2f(U.uRes, canvas.width, canvas.height);
      gl.uniform1f(U.uShade, variant === 'page' ? (canvas.width > canvas.height * 1.2 ? 1.0 : 0.45) : 0.0);
      gl.uniform1f(U.uTime, reduce ? 0 : (now - t0) / 1000);
      gl.uniform2f(U.uMouse, reduce ? 0 : mouse.x, reduce ? 0 : -mouse.y);
      gl.uniform1f(U.uGlide, glide);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      if (!host.classList.contains('is-live')) host.classList.add('is-live');
      if (!reduce && visible && !document.hidden) raf = requestAnimationFrame(frame);
    }
    function kick() { if (!raf) { last = performance.now(); samples = []; warm = 10; raf = requestAnimationFrame(frame); } }

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (visible) kick();
      }, { threshold: 0 }).observe(host);
    }
    document.addEventListener('visibilitychange', function () { if (!document.hidden) kick(); });
    window.addEventListener('resize', kick);
    kick();
  }

  for (var i = 0; i < hosts.length; i++) start(hosts[i]);
})();
