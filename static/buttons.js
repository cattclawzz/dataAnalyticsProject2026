const items = [
  "Investigation",
  "Data collection & cleaning",
  "Mean, Median, Mode",
  "Line Graph",
  "Scatter Graph",
  "Bar Graph",
  "Pie Chart",
  "Linear Regression",
  "Conclusion",
  "References"
];

const selectedIndex = 0;

const container = document.getElementById("nav");

items.forEach((text, index) => {
  const div = document.createElement("div");
  div.className = "button" + (index === selectedIndex ? " selected" : "");
  div.textContent = text;
  container.appendChild(div);
});