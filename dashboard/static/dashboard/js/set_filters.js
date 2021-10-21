const selectBoxes = document.querySelectorAll("select");
const button = document.querySelector("button.bg-red");

selectBoxes.forEach((selectBox) => {
  selectBox.addEventListener("click", () => {
    let x = [];

    selectBoxes.forEach((selectBox) => {
      if (selectBox.options[selectBox.selectedIndex].value === "none") {
        x.push(selectBox);
      }
    });
    if (x.length === 0) {
      button.disabled = false;
    } else {
      button.disabled = true;
    }
  });
});
