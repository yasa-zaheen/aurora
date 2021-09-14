function categoriesDropdown() {
  const categoryLink = document.querySelector("a.link#categories");
  const categoryDropdown = document.querySelector("div.dropdown");

  categoryLink.addEventListener("mouseover", function () {
    categoryDropdown.style.maxHeight = "100vh";
    categoryDropdown.style.transition = "0.25s ease all";
  });
  window.addEventListener("click", function () {
    categoryDropdown.style.maxHeight = "0vh";
    categoryDropdown.style.transition = "0.25s ease all";
  });
}

categoriesDropdown();
