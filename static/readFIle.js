function readFile(elementID, file, isScript=false){
    const demo = document.getElementById(elementID);

    fetch(file)
        .then(x => x.text())
        //.then(y => demo.textContent = y);
        .then(y => demo.innerHTML = y);
}