window.onload = function() {
    const demo = document.getElementById("demo");
    const file = demo.getAttribute("data-file");

    fetch(file)
        .then(x => x.text())
        //.then(y => demo.textContent = y);
        .then(y => demo.innerHTML = y);
}