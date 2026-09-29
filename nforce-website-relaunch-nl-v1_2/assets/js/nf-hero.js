/* ==========================================================================
   NForce — nf-hero.js
   Home-hero: een live ijsvlak in WebGL. Laag camerastandpunt boven het ijs,
   de blauwe lijn, een face-offcirkel en arenalicht dat in het ijs weerspiegelt.
   Eén rustige beweging: de camera glijdt langzaam over het ijs.

   - Geen WebGL of prefers-reduced-motion: de posterafbeelding blijft staan
     (assets/img/hero-ice.jpg, CSS-achtergrond van .hero--ice).
   - Rendert alleen als de hero in beeld is en het tabblad zichtbaar is.
   - Lage renderresolutie (DPR max 1, schaal 0,75): zacht, snel en zuinig.
   ========================================================================== */
(function () {
  'use strict';
  var hero = document.querySelector('.hero--ice');
  var canvas = hero && hero.querySelector('.hero__ice');
  if (!canvas) return;

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gl = null;
  try {
    gl = canvas.getContext('webgl', { antialias: false, alpha: false, premultipliedAlpha: false, powerPreference: 'low-power' }) ||
         canvas.getContext('experimental-webgl');
  } catch (e) { gl = null; }
  if (!gl) return;

  var VERT = 'attribute vec2 p; void main(){ gl_Position = vec4(p, 0.0, 1.0); }';

  var FRAG = [
    'precision highp float;',
    'uniform vec2 uRes; uniform float uTime; uniform vec2 uMouse; uniform float uStill;',
    'const vec3 BLUE = vec3(0.494, 0.784, 1.0);',                 /* #7ec8ff */
    'float hash(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }',
    'float noise(vec2 p){ vec2 i = floor(p); vec2 f = fract(p); vec2 u = f * f * (3.0 - 2.0 * f);',
    '  return mix(mix(hash(i), hash(i + vec2(1.0, 0.0)), u.x), mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x), u.y); }',
    'float fbm(vec2 p){ float v = 0.0; float a = 0.5; for (int i = 0; i < 5; i++) { v += a * noise(p); p = p * 2.03 + 11.7; a *= 0.5; } return v; }',
    /* schaatssporen: sterk uitgerekte ruis onder een paar hoeken */
    'float scratches(vec2 p){ float s = 0.0;',
    '  for (int k = 0; k < 4; k++) { float a = 0.35 + float(k) * 0.83; float c = cos(a); float sn = sin(a);',
    '    vec2 q = vec2(c * p.x - sn * p.y, sn * p.x + c * p.y);',
    '    float n = noise(vec2(q.x * 0.35, q.y * 42.0) + float(k) * 17.0);',
    '    s += smoothstep(0.82, 0.99, n) * (0.35 + 0.65 * noise(q * 0.8)); }',
    '  return s; }',
    /* lijn met anti-aliasing die meeschaalt met de afstand */
    'float band(float d, float w, float aa){ return 1.0 - smoothstep(w, w + aa, abs(d)); }',
    'void main(){',
    '  vec2 uv = (gl_FragCoord.xy - 0.5 * uRes) / uRes.y;',
    '  float t = uTime * (1.0 - uStill);',
    '  vec3 ro = vec3(uMouse.x * 0.3 + sin(t * 0.04) * 0.2, 1.05 + uMouse.y * 0.04, 0.0);',
    '  vec3 rd = normalize(vec3(uv.x, uv.y - 0.14, 1.35));',
    '  vec3 col = vec3(0.0);',
    '  float glide = t * 0.15;',
    /* lichten rechts van de tekstkolom op brede schermen */
    '  float lb = uRes.x / uRes.y > 1.2 ? 0.36 : 0.04;',
    '  if (rd.y < -0.0005) {',
    '    float dist = -ro.y / rd.y;',
    '    vec3 pos = ro + rd * dist;',
    '    vec2 w = vec2(pos.x, pos.z + glide);',                     /* wereldpositie op het ijs */
    '    float aa = 0.0035 * dist + 0.004;',
    '    float fade = smoothstep(55.0, 6.0, dist);',
    /* ijs: diep, koel, bijna zwart; wolkigheid en fijne structuur */
    '    float cloud = fbm(w * 0.14);',
    '    float fine = fbm(w * 2.6);',
    '    vec3 ice = vec3(0.018, 0.022, 0.027) + vec3(0.030, 0.038, 0.046) * cloud + vec3(0.010) * fine;',
    '    vec2 wq = w * 0.8 + vec2(fbm(w * 0.22), fbm(w * 0.22 + 5.2)) * 3.2;',
    '    float sc = scratches(wq) * smoothstep(30.0, 3.0, dist);',
    '    ice += vec3(0.042, 0.048, 0.055) * sc;',
    /* belijning onder het ijs: iets diffuus */
    '    float soft = 0.8 + 0.2 * fine;',
    /* belijning herhaalt elke 44 m: blauwe lijn op 8 m, face-offcirkel 6 m verder */
    '    float blue = band(mod(w.y - 8.0 + 22.0, 44.0) - 22.0, 0.15, aa * 1.5);',
    '    vec2 fo = vec2(w.x - 4.2, mod(w.y - 14.0 + 22.0, 44.0) - 22.0);',
    '    float r = length(fo);',
    '    float circle = band(r - 4.57, 0.035, aa);',
    '    float spot = 1.0 - smoothstep(0.3, 0.3 + aa, r);',
    '    float hashes = band(abs(fo.y) - 0.9, 0.035, aa) * step(4.57, abs(fo.x)) * step(abs(fo.x), 5.2);',
    '    float white = max(max(circle, spot * 0.8), hashes);',
    '    ice = mix(ice, BLUE * 0.55, blue * soft * 0.92);',
    '    ice = mix(ice, vec3(0.60, 0.64, 0.68), white * soft * 0.6);',
    /* glad ijs: zachte, licht uitgesmeerde reflecties van verre lichtrijen */
    '    float hx = fbm(w * vec2(0.35, 0.08) + 3.0) - 0.5;',
    '    float hz2 = fbm(w * vec2(0.08, 0.35) + 9.0) - 0.5;',
    '    vec3 n = normalize(vec3(hx * 0.035, 1.0, hz2 * 0.035));',
    '    vec3 rf = reflect(rd, n);',
    '    float spec = 0.0;',
    /* lichtrijen rechts van de tekst; reflecties rekken uit naar de kijker */
    '    for (int i = 0; i < 3; i++) { for (int j = 0; j < 2; j++) {',
    '      float lz = 70.0 + float(j) * 40.0 - mod(glide * 2.0, 40.0);',
    '      vec3 L = vec3((lb + 0.13 * float(i)) * lz / 1.35 + ro.x, 6.0, lz);',
    '      vec3 ld = normalize(L - pos);',
    '      vec2 dd = (rf.xy - ld.xy) / vec2(0.010, 0.050);',
    '      spec += exp(-dot(dd, dd)) * 0.75 + exp(-dot(dd, dd) * 0.08) * 0.05;',
    '    } }',
    /* glans: de donkere arena met een band licht van de tribunes */
    '    float sheen = exp(-abs(rf.y - 0.035) * 30.0) * 0.05;',
    /* op smalle schermen staat de tekst over de hele breedte: reflecties zachter */
    '    spec *= uRes.x / uRes.y > 1.2 ? 1.0 : 0.4;',
    '    col = ice + vec3(0.78, 0.86, 0.94) * spec * fade + vec3(0.55, 0.62, 0.70) * sheen;',
    /* diepte: ijs loopt weg in het donker */
    '    col *= 0.25 + 0.75 * fade;',
    '  }',
    /* verre arenalampen boven de horizon, zacht */
    '  for (int i = 0; i < 3; i++) {',
    '    vec3 L = normalize(vec3((lb + 0.13 * float(i)) * 110.0 / 1.35, 6.0 - ro.y, 110.0));',
    '    vec2 dl = (rd.xy - L.xy) / vec2(0.012, 0.008);',
    '    col += vec3(0.75, 0.83, 0.92) * exp(-dot(dl, dl)) * 0.18;',
    '  }',
    /* horizon: donkere arena met een vleugje licht */
    '  float hzn = exp(-abs(rd.y + 0.004) * 42.0);',
    '  col += vec3(0.04, 0.05, 0.06) * hzn;',
    /* ruimte voor de tekst links en een rustige vignet */
    '  col *= mix(0.12, 1.0, smoothstep(-0.9, 0.45, uv.x));',
    '  col *= 1.0 - 0.5 * dot(uv * vec2(0.5, 0.9), uv * vec2(0.5, 0.9));',
    '  col = pow(max(col, 0.0), vec3(0.9));',
    /* filmkorrel */
    '  col += (hash(gl_FragCoord.xy + fract(uTime * 7.13) * 91.0) - 0.5) * 0.024;',
    '  gl_FragColor = vec4(col, 1.0);',
    '}'
  ].join('\n');

  function shader(type, src) {
    var s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) { throw new Error(gl.getShaderInfoLog(s)); }
    return s;
  }
  var prog;
  try {
    prog = gl.createProgram();
    gl.attachShader(prog, shader(gl.VERTEX_SHADER, VERT));
    gl.attachShader(prog, shader(gl.FRAGMENT_SHADER, FRAG));
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(prog));
  } catch (err) {
    if (window.console) console.warn('NForce hero: WebGL uit, poster blijft staan.', err);
    return;
  }
  gl.useProgram(prog);
  var buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  var loc = gl.getAttribLocation(prog, 'p');
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  var uRes = gl.getUniformLocation(prog, 'uRes');
  var uTime = gl.getUniformLocation(prog, 'uTime');
  var uMouse = gl.getUniformLocation(prog, 'uMouse');
  var uStill = gl.getUniformLocation(prog, 'uStill');

  var SCALE = 0.75;
  function resize() {
    var dpr = Math.min(window.devicePixelRatio || 1, 1);
    var w = Math.max(1, Math.round(canvas.clientWidth * dpr * SCALE));
    var h = Math.max(1, Math.round(canvas.clientHeight * dpr * SCALE));
    if (canvas.width !== w || canvas.height !== h) {
      canvas.width = w; canvas.height = h;
      gl.viewport(0, 0, w, h);
    }
  }

  var mouse = { x: 0, y: 0 }, target = { x: 0, y: 0 };
  hero.addEventListener('pointermove', function (e) {
    var r = hero.getBoundingClientRect();
    target.x = ((e.clientX - r.left) / r.width) * 2 - 1;
    target.y = ((e.clientY - r.top) / r.height) * 2 - 1;
  });

  var start = performance.now();
  var visible = true, raf = 0;
  function frame(now) {
    raf = 0;
    resize();
    mouse.x += (target.x - mouse.x) * 0.04;
    mouse.y += (target.y - mouse.y) * 0.04;
    gl.uniform2f(uRes, canvas.width, canvas.height);
    gl.uniform1f(uTime, reduce ? 0 : (now - start) / 1000);
    gl.uniform2f(uMouse, reduce ? 0 : mouse.x, reduce ? 0 : -mouse.y);
    gl.uniform1f(uStill, reduce ? 1 : 0);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    if (!hero.classList.contains('is-live')) hero.classList.add('is-live');
    if (!reduce && visible && !document.hidden) raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(frame); }

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      if (visible) kick();
    }, { threshold: 0 }).observe(hero);
  }
  document.addEventListener('visibilitychange', function () { if (!document.hidden) kick(); });
  window.addEventListener('resize', function () { if (reduce) kick(); });
  kick();
})();
