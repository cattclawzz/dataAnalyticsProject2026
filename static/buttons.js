function readFile(elementID, file){
    const demo = document.getElementById(elementID);
    fetch(file)
        .then(x => x.text())
        .then(y => demo.innerHTML = y);
}

function camelCaseSplitter(str) {
  return str
    .replace(/([A-Z])/g, ' $1')
    .replace(/^./, function(s) { return s.toUpperCase(); });
}

function reset(pages){
  pages.forEach((page) => {
    document.getElementById(page).style.display = "none";
    document.getElementById(page + "Button").classList.remove("selected");
  });
}

function togglePage(page, pages) {
    reset(pages);
    window.scrollTo(0,0);
    document.getElementById(page).style.display = "block";
    document.getElementById(page + "Button").classList.add("selected");
}

function buildUI(pages){
  const nav = document.getElementById("nav");
  const content = document.getElementById("content");

  pages.forEach((text) => {
    const button = document.createElement("div");
    button.className = "button";
    button.textContent = camelCaseSplitter(text);
    button.id = text + "Button";
    button.onclick = () => togglePage(text, pages);
    nav.appendChild(button);

    const page = document.createElement("div");
    page.className = "page " + text;
    page.id = text;
    content.appendChild(page);
    readFile(text, "/static/pages/" + text + ".html");
    content.appendChild(page);
  });

  togglePage("investigation", pages);
}

buildUI([
  "investigation",
  "dataCollectionAndCleaning",
  "meanMedianAndMode",
  "lineGraph",
  "scatterGraph",
  "barGraph",
  "pieChart",
  "linearRegression",
  "conclusion",
  "references"
]);