/* Prototype: the face-off circle as a stage.
   On wide screens with motion allowed, the figure stays in view while the list scrolls past,
   and one variable is lit at a time: its node turns blue, the puck moves to it, and the ring
   draws up to it. Everywhere else (phones, reduced motion, no JavaScript) the figure is the
   normal static one and nothing here runs. Nothing is fetched and nothing is tracked. */
(function () {
  var stages = document.querySelectorAll(".rc--scroll");
  if (!stages.length || !("IntersectionObserver" in window)) return;
  var wide = window.matchMedia("(min-width: 900px)");
  var calm = window.matchMedia("(prefers-reduced-motion: reduce)");

  stages.forEach(function (rc) {
    var n = parseInt(rc.getAttribute("data-n"), 10) || 0;
    var items = rc.querySelectorAll(".rc-list li");
    var nodes = rc.querySelectorAll(".rc-node");
    var nums = rc.querySelectorAll(".rc-num");
    var io = null;

    function show(step) {
      rc.style.setProperty("--rc-step", step);
      items.forEach(function (li, i) { li.classList.toggle("is-active", i === step); li.classList.toggle("is-done", i < step); });
      nodes.forEach(function (el, i) { el.classList.toggle("is-active", i === step); el.classList.toggle("is-done", i < step); });
      nums.forEach(function (el, i) { el.classList.toggle("is-active", i === step); });
    }
    function on() {
      if (rc.classList.contains("rc--live")) return;
      rc.classList.add("rc--live");
      rc.style.setProperty("--rc-n", n);
      show(0);
      // The lit step is the item crossing the middle band of the screen.
      io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) show(parseInt(e.target.getAttribute("data-i"), 10) || 0);
        });
      }, { rootMargin: "-45% 0px -45% 0px", threshold: 0 });
      items.forEach(function (li) { io.observe(li); });
    }
    function off() {
      if (io) { io.disconnect(); io = null; }
      rc.classList.remove("rc--live");
      items.forEach(function (li) { li.classList.remove("is-active", "is-done"); });
      nodes.forEach(function (el) { el.classList.remove("is-active", "is-done"); });
      nums.forEach(function (el) { el.classList.remove("is-active"); });
    }
    function sync() { (wide.matches && !calm.matches) ? on() : off(); }
    sync();
    if (wide.addEventListener) { wide.addEventListener("change", sync); calm.addEventListener("change", sync); }
  });
})();
