const mainFilters = () => {
  const filterCategoriesBtns = document.querySelectorAll(
    "button.filter-categories__btn"
  );
  const filters = document.querySelectorAll("div.filters-container__filters p");

  const exitbtn = document.querySelector("button.main-filters__exit-btn");
  const filterBtn = document.querySelector("button.search__filterBtn");

  const nav = document.querySelector("nav");
  const body = document.querySelector("body");
  const mainFiltersContainer = document.querySelector(
    "div.product-type__main-filters"
  );

  // Exit Button Functionality

  exitbtn.addEventListener("click", function () {
    nav.style.display = "flex";
    nav.style.height = "10vh";

    body.style.overflow = "scroll";

    mainFiltersContainer.style.transform = "scale(0, 0)";
  });

  // Filter Button Functionality

  filterBtn.addEventListener("click", function () {
    nav.style.height = "0vh";
    nav.style.display = "none";

    body.style.overflow = "hidden";

    mainFiltersContainer.style.transform = "scale(1,1)";
  });

  // Viewing filters from the first filter category

  filters.forEach((filter) => {
    if (
      filter.getAttribute("data-filter-category") ===
      filterCategoriesBtns[0].innerText
    ) {
      filter.style.display = "block";
    }
  });

  // Viewing filters from categories after they are clicked

  filterCategoriesBtns.forEach((filterCategoriesBtn) => {
    filterCategoriesBtn.addEventListener("click", function () {
      filters.forEach((filter) => {
        filter.style.display = "none";

        if (
          filter.getAttribute("data-filter-category") ===
          filterCategoriesBtn.innerText
        ) {
          filter.style.display = "block";
        }
      });
    });
  });
};

mainFilters();
