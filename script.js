// Theme toggle
const themeBtn = document.getElementById("themeToggle");
if (themeBtn) {
  themeBtn.addEventListener("click", () => {
    const html = document.documentElement;
    const newTheme = html.dataset.theme === "dark" ? "light" : "dark";
    html.dataset.theme = newTheme;
    localStorage.setItem("theme", newTheme);
  });
  document.documentElement.dataset.theme = localStorage.getItem("theme") || "dark";
}

// Popup function
function showPopup(msg) {
  const popup = document.getElementById("popup");
  const text = document.getElementById("popup-text");
  text.textContent = msg;
  popup.classList.add("show");
  setTimeout(() => popup.classList.remove("show"), 4000);
}

// Generic AJAX handler
function handleForm(formId, endpoint) {
  const form = document.getElementById(formId);
  if (!form) return;
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const res = await fetch(endpoint, { method: "POST", body: data });
    const json = await res.json();
    showPopup(json.result);
  });
}

// Initialize all forms
handleForm("messageForm", "/api/message");
handleForm("emailForm", "/api/email");
handleForm("websiteForm", "/api/website");
