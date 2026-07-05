document.addEventListener("DOMContentLoaded",()=>{

    gsap.from(".dashboard-hero h1",{
        y:50,
        opacity:0,
        duration:1
    });

    gsap.from(".dashboard-hero p",{
        y:30,
        opacity:0,
        duration:1,
        delay:.3
    });

    gsap.from(".dashboard-svg",{
        scale:.8,
        opacity:0,
        duration:1.2
    });

    gsap.from(".dashboard-stat,.prediction-card,.chart-card",{
        y:50,
        opacity:0,
        duration:1,
        stagger:.15
    });

});