// Navbar Scroll
window.addEventListener("scroll", () => {

    const navbar = document.getElementById("mainNavbar");

    if (window.scrollY > 40) {

        navbar.classList.add("scrolled");

    } else {

        navbar.classList.remove("scrolled");

    }

});

// Hero Animation

window.onload = () => {

    gsap.from("h1",{

        y:60,

        opacity:0,

        duration:1

    });

    gsap.from(".lead",{

        y:40,

        opacity:0,

        duration:1,

        delay:.4

    });

    gsap.from(".btn",{

        y:30,

        opacity:0,

        duration:1,

        delay:.7,

        stagger:.2

    });

    gsap.from("#heroLogo",{

        scale:.5,

        opacity:0,

        rotation:20,

        duration:1.4,

        ease:"back.out(1.7)"

    });

};