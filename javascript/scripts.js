function elementDisapear(elementID){
    let element = document.getElementById(elementID);
    element.style.display = "none";
}

function elementAppear(elementID){
    let element = document.getElementById(elementID);
    element.style.display = "block";
}

function elementSwapIn(elementID1, elementID2, elementID3){
    elementAppear(elementID1);
    elementAppear(elementID2);
    elementDisapear(elementID3);
}

function elementSwapOut(elementID1, elementID2, elementID3){
    elementAppear(elementID1);
    elementDisapear(elementID2);
    elementDisapear(elementID3);
}



const savedTheme = localStorage.getItem("theme") || "style1";

/* Inject floating toggle */
document.getElementById("theme-toggle-root").innerHTML = `
  <div class="theme-toggle-wrapper">
    <label class="theme-switch">
      <input type="checkbox" id="themeToggle">
      <span class="slider"></span>
    </label>
  </div>
`;

/* Apply saved theme immediately */
const themeLink = document.getElementById("themeStylesheet");
themeLink.href = `css/${savedTheme}.css`;

const toggle = document.getElementById("themeToggle");
toggle.checked = savedTheme === "style2";

/* Toggle handler */
toggle.addEventListener("change", () => {
  const next = toggle.checked ? "style2" : "style1";
  themeLink.href = `css/${next}.css`;
  localStorage.setItem("theme", next);
});
