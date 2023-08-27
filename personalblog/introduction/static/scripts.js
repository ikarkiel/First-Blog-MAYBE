document.addEventListener("DOMContentLoaded", function() {
    const navBar = document.querySelector("nav"),
        menuBtns = document.querySelectorAll(".menu-icon"),
        overlay = document.querySelector(".overlay"),
        navBtns = document.querySelectorAll(".nav-link");

    menuBtns.forEach(menuBtn => {
        menuBtn.addEventListener("click", () => {
            navBar.classList.toggle("open");
        });
    });

    overlay.addEventListener("click", () => {
        navBar.classList.remove("open");
    });

    navBtns.forEach(navBtn => {
        navBtn.addEventListener("click", () => {
            navBar.classList.toggle("open");
        });
        
    });

    const aboutmyself = document.getElementById('aboutmyself');
    const content = document.getElementById('content');

    AboutMyself.addEventListener('click', () => {
        fetch('path/to/aboutme')
        .then(response => response.text())
        .then(data => {
            content.innerHTML = data;
        });
    });
});