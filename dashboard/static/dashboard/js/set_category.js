const setCategoryHandler = () => {
  const categories = document.querySelectorAll("div.category");
  const inputs = document.querySelectorAll("input");

  categories.forEach((category) => {
    category.addEventListener("click", () => {
      const input = category.childNodes[5];
      input.checked = true;

      inputs.forEach((input) => {
        if (input.checked) {
          input.parentElement.classList.add("category-toggled");
        } else {
          input.parentElement.classList.remove("category-toggled");
        }
      });
    });
  });
};

setCategoryHandler();
