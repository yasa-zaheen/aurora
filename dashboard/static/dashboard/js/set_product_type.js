const setProductTypeHandler = () => {
  const productTypes = document.querySelectorAll("div.product-type");
  const inputs = document.querySelectorAll("input");

  productTypes.forEach((productType) => {
    productType.addEventListener("click", () => {
      const input = productType.childNodes[3];
      input.checked = true;

      inputs.forEach((input) => {
        if (input.checked) {
          input.parentElement.classList.add("product-type-toggled");
        } else {
          input.parentElement.classList.remove("product-type-toggled");
        }
      });
    });
  });
};

setProductTypeHandler();
