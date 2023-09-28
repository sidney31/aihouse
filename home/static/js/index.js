//header animate
var navbar = document.querySelector(".navbar");

if (navbar) {
    window.onwheel = e => {
        if (e.deltaY > 0)
            navbar.style.transform = "translateY(-100px)";
        else
            navbar.style.transform = "translateY(0)";

    }
}

//gallery carousel
var items = document.querySelectorAll(".gallery-carousel-inner .carousel-item");
items.forEach((e) => {
    const slide = 2;
    let next = e.nextElementSibling;
    for (let i = 0; i < slide; i++) {
        if (!next) {
            next = items[0];
        }
        let cloneChild = next.cloneNode(true);
        e.appendChild(cloneChild.children[0]);
        next = next.nextElementSibling;
    }
})