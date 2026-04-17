function readScript(elementID, file){
    const demo = document.getElementById(elementID);

    fetch(file)
        .then(x => x.text())
        .then(y => demo.textContent = y);
}