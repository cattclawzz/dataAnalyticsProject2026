function readFile(elementID, isScript=false){
    const demo = document.getElementById(elementID);
	const file = demo.getAttribute("data-file");

    fetch(file)
        .then(x => x.text())
        //.then(y => demo.textContent = y);
        .then(y => demo.innerHTML = y);
}