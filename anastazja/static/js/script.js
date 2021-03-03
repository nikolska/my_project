const links = document.querySelectorAll("a.images");
const lightbox = document.querySelector(".lightbox");
const lightboxCtn = document.querySelector(".lightbox-cnt");
const img = document.querySelector(".lightbox-img");
const button = document.querySelector(".lightbox-close");

links.forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        img.src = link.href;
        lightbox.style.display = 'flex';
    })
});

button.addEventListener('click', e => {
    lightbox.style.display = 'none';
});

lightbox.addEventListener('click', e => {
    lightbox.style.display = 'none';
});

lightboxCtn.addEventListener('click', e => {
    e.stopPropagation();
});


// const prev = document.querySelector("button.prev");
// const next = document.querySelector("button.next");
// const carousel = document.querySelector(".carousel-container");
// const track = document.querySelector(".track");
// let width = carousel.offsetWidth;
// let index = 0;
//
// window.addEventListener("resize", e => {
//     width = carousel.offsetWidth;
// });
//
// next.addEventListener("click", e => {
//     e.preventDefault();
//     index += 1;
//     prev.classList.add("show");
//
//     track.style.transform = "translateX(" + index * -width + "px)";
//     if (track.offsetWidth - index * width < index * width) {
//         next.classList.add("hide");
//     }
// });
//
// prev.addEventListener("click", e => {
//     index -= 1;
//     next.classList.remove("hide");
//     if (index === 0) {
//         prev.classList.remove("show");
//     }
//     track.style.transform = "translateX(" + index * -width + "px)";
//     });
//
