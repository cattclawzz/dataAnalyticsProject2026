//Header follows scroll
window.onscroll = function() {stick()};

var header = document.getElementById("nav");
var content = document.getElementById("content");
var sticky = header.offsetTop;

function stick() {

    if (window.pageYOffset > sticky) {
        header.classList.add("sticky"); //Add class when you scroll down
        content.classList.add("adjust");
    }
    
    else {
        header.classList.remove("sticky"); // Remove class when you scroll back up
        content.classList.remove("adjust");
    }
}