//header animate
var scrollPosition = 0;
window.addEventListener('scroll', () => {
    let navbar = document.querySelector(".navbar");

    if (window.scrollY > scrollPosition) {
        navbar.style.transform = "translateY(-100px)";
    } else {
        navbar.style.transform = "translateY(0)";
    }
    scrollPosition = window.scrollY;
});

//cards carousel

var cards = document.querySelectorAll(".card-carousel > .carousel-item")
cards[0].classList.add("active")

var carouselIndicators = document.querySelector("#carousel > .carousel-indicators")
cards.forEach((el, i) => {
    if (i === 0) {
        carouselIndicators.innerHTML +=
            `<button type="button" data-bs-target="#carousel" data-bs-slide-to="${i}" 
        class="active" aria-label="Slide ${Number(i) + 1}" aria-current="true"></button>`
    } else {
        carouselIndicators.innerHTML +=
            `<button type="button" data-bs-target="#carousel" data-bs-slide-to="${i}"
        class aria-label="Slide ${Number(i) + 1}"></button>`
    }
})


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

//animation appearance
var animatedItems = document.querySelectorAll(".appear-right, .appear-left, .appear-center")
var stateItems = new Map(); // <element: e, bool: visited>
animatedItems.forEach((e) => {
    stateItems.set(e, false);
})


window.addEventListener('scroll', () => {
    scrollTracking();
})

window.addEventListener('load', () => {
    scrollTracking();
})

function scrollTracking() {
    var wt = window.scrollY;
    var wh = window.innerHeight;

    for (let [item, visited] of stateItems) {
        if (!visited && wt + wh >= item.getBoundingClientRect().top) {
            animateItem(item);
            stateItems.set(item, true)
        }
    }
}

function animateItem(item) {
    if (item.classList.contains("appear-center")) {
        item.animate(
            [
                {opacity: 0},
                {opacity: 1},
            ],
            {
                duration: 2000
            }
        );
    } else if (item.classList.contains("appear-right")) {
        item.animate(
            [
                {transform: "translateX(-100px)"},
                {transform: "translateX(0px)"},
            ],
            {
                duration: 300
            }
        );
    } else if (item.classList.contains("appear-left")) {
        item.animate(
            [
                {transform: "translateX(100px)"},
                {transform: "translateX(0px)"},
            ],
            {
                duration: 300
            }
        );
    }
}