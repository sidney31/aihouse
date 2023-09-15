var navbar = document.querySelector(".navbar");

console.log(navbar)

if (navbar) {
    window.onwheel = e => {
        if(e.deltaY > 0)
            navbar.style.transform = "translateY(-100px)";
        else 
            navbar.style.transform = "translateY(0)";
        
    }
}
