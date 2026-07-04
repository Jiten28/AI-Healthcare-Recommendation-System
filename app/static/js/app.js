gsap.registerPlugin(ScrollTrigger);

/* ===========================
        NAVBAR
=========================== */

window.addEventListener("scroll",()=>{

    const nav=document.getElementById("mainNavbar");

    nav.classList.toggle("scrolled",window.scrollY>40);

});

/* ===========================
        HERO
=========================== */

window.addEventListener("load",()=>{

    gsap.from(".display-2",{

        y:80,

        opacity:0,

        duration:1

    });

    gsap.from(".lead",{

        y:40,

        opacity:0,

        delay:.35,

        duration:1

    });

    gsap.from(".hero-buttons", {
    opacity: 0,
    y: 30,
    duration: 1,
    delay: 0.7,
    ease: "power3.out"
    });

    gsap.from("#heroLogo",{

        opacity:0,

        scale:.65,

        rotation:15,

        duration:1.6,

        ease:"back.out(1.8)"

    });

    /* Floating Animation */

    gsap.to("#heroLogo",{

        y:-18,

        duration:2.6,

        repeat:-1,

        yoyo:true,

        ease:"power1.inOut"

    });

    gsap.to("#heroLogo",{

        rotation:3,

        duration:4,

        repeat:-1,

        yoyo:true,

        ease:"sine.inOut"

    });

    /* Glows */

    gsap.to(".hero-glow-1",{

        scale:1.2,

        duration:5,

        repeat:-1,

        yoyo:true

    });

    gsap.to(".hero-glow-2",{

        scale:0.8,

        duration:4,

        repeat:-1,

        yoyo:true

    });

    gsap.to(".hero-glow-3",{

        scale:1.3,

        duration:6,

        repeat:-1,

        yoyo:true

    });

});