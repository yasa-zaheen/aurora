const setSubCategoryHandler = () => {
  const subCategories = document.querySelectorAll("div.sub-category");
  const inputs = document.querySelectorAll("input");

  subCategories.forEach((subCategory) => {
    subCategory.addEventListener("click", () => {
      const input = subCategory.childNodes[5];
      input.checked = true;

      inputs.forEach((input) => {
        if (input.checked) {
          input.parentElement.classList.add("sub-category-toggled");
        } else {
          input.parentElement.classList.remove("sub-category-toggled");
        }
      });
    });
  });
};

setSubCategoryHandler();
