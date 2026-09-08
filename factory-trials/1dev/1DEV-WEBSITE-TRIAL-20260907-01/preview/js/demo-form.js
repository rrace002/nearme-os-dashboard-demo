(function () {
  document.querySelectorAll("form[data-demo-form]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        form.classList.remove("is-ok");
        return;
      }
      form.classList.add("is-ok");
      var box = form.querySelector("[data-demo-result]");
      if (box) {
        box.hidden = false;
        box.textContent =
          "DEMO ONLY / NOT CONNECTED — nothing was sent. This is not operational lead delivery. GHL webhook is skipped.";
      }
    });
  });
})();
