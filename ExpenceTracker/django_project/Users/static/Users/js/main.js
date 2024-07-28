const navbarToggler = document.querySelector(".navbar-toggler");
navbarToggler.addEventListener("click", () => {
  const navbarNav = document.getElementById("navbarNav");
  navbarNav.classList.toggle("show");
});
