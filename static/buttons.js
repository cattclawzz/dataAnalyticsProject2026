const items = [
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
  const container = document.getElementById("nav");

  pages.forEach((text, index) => {
    const div = document.createElement("div");
    div.className = "button"; //+ (index === selectedIndex ? " selected" : "")
    div.textContent = camelCaseSplitter(text);
    container.appendChild(div);
  });
}

navBar(items)