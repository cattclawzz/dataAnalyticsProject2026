const pages = [
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
];

function camelCaseSplitter(str) {
  return str
    .replace(/([A-Z])/g, ' $1')
    .replace(/^./, function(s) { return s.toUpperCase(); });
}

function navBar(pages){
  const nav = document.getElementById("nav");

  pages.forEach((text) => {
    const div = document.createElement("div");
    div.className = "button";
    div.textContent = camelCaseSplitter(text);
    div.id = text + "Button";
    div.onclick = () => togglePage(text);
    nav.appendChild(div);
  });
}
navBar(pages);

function makePages(pages){
  const nav = document.getElementById("content");

  pages.forEach((text) => {
    const div = document.createElement("div");
    div.className = "page " + text;
    div.id = text;
    content.appendChild(div);
    readFile(text, "/static/pages/" + text + ".html");
  });
}

makePages(pages);

function reset(){
  for (let i = 0; i < pages.length; i++) {
    document.getElementById(pages[i]).style.display = "none";
    document.getElementById(pages[i] + "Button").classList.remove("selected");
  }
}

reset();
function togglePage(page) {
    reset();
    window.scrollTo(0,0);
    document.getElementById(page).style.display = "block";
    document.getElementById(page + "Button").classList.add("selected");
}
togglePage("investigation");