(function () {
  var key = "tagsLayout";
  var allowed = ["pills","cloud","cards","masonry","heatmap","buckets"];

  var wrap = document.getElementById("tags-terms");
  if (!wrap) return;

  var picker = document.getElementById("stylePicker");
  var variants = Array.prototype.slice.call(wrap.querySelectorAll(".variant"));

  function norm(s){ return (s||"").toLowerCase(); }
  function show(name){ variants.forEach(function(v){ v.hidden = v.dataset.style !== name; }); }

  var url = new URL(window.location.href);
  var fromQuery = norm(url.searchParams.get("style"));
  var fromStorage = norm(localStorage.getItem(key));
  var fromDefault = norm(wrap.getAttribute("data-default")) || "cloud"; // cloud default

  var current = allowed.includes(fromQuery) ? fromQuery
              : (allowed.includes(fromStorage) ? fromStorage : fromDefault);

  picker.value = current; show(current);

  picker.addEventListener("change", function(){
    var val = norm(picker.value); if (!allowed.includes(val)) return;
    localStorage.setItem(key, val);
    var u = new URL(window.location.href); u.searchParams.set("style", val);
    history.replaceState({}, "", u); show(val);
  });
})();
