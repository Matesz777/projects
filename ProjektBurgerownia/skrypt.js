const  zmiennetlo = document.getElementById("scroll-bar1");
const przycisyk = document.getElementById("zmow-online-button");
const burgerklick = document.querySelectorAll(".links");
const rollingmenuButton = document.getElementById("rolling-menu");
const dropdownMenuContent = document.getElementById("rolling-content");
const closeButton = document.getElementById("button-closing");
let kolor = false;
let menu = false;
window.addEventListener("scroll", () =>{
    const scrollposition = window.scrollY;
    if (scrollposition > 1){
        zmiennetlo.style.backgroundColor = "black";
        zmiennetlo.style.transition = "0.43s";
    }
    else{
        zmiennetlo.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
        zmiennetlo.style.transition = "0.43s";
    }
});
burgerklick.forEach((element) => {
    element.addEventListener("click", () => {
        if(kolor){
            element.style.border = "none";
            kolor = false;
        }
        else{
            element.style.border = "4px solid green";
            kolor = true;
        }
    })
});
rollingmenuButton.addEventListener("click", () =>{
    dropdownMenuContent.classList.toggle("show");
});
closeButton.addEventListener("click", () =>{
    dropdownMenuContent.classList.remove("show");
});

