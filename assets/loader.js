const loader = document.querySelector('.loader-background');
const main = document.querySelector('.');


function init() {
    setTimeout(() => {
        loader.style.opacity = 0;
        loader.className.add("hidden");
    }, 4000);
}