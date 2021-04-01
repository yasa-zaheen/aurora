const filterSelect = () => {
  const filterCards = document.querySelectorAll("a.filter-card");

  filterCards.forEach((filterCard) => {
    filterCard.addEventListener("click", function () {
      filterCard.classList.toggle("filter-card-toggled");
    });
  });
};

filterSelect();

const filterColors = () => {
  const filterCards = document.querySelectorAll("a.filter-card");

  filterCards.forEach((filterCard) => {
    filterCard.style.backgroundColor = filterCard.getAttribute("data-bgColor");
    filterCard.style.color = filterCard.getAttribute("data-fgColor");

    if (filterCard.getAttribute("data-type") === "Color") {
      filterCard.style.minWidth = "calc((14vw + 5px) / 2 - 12.5px)";
      filterCard.style.maxWidth = "calc((14vw + 5px) / 2 - 12.5px)";

      // max-width: calc(14vw + 5px);

      filterCard.childNodes[1].style.opacity = "0";

      filterCard.addEventListener("mouseover", function () {
        filterCard.style.minWidth = "174px";
        filterCard.style.maxWidth = "174px";
        filterCard.childNodes[1].style.opacity = "1";
      });
      filterCard.addEventListener("mouseout", function () {
        filterCard.style.minWidth = "77px";
        filterCard.style.maxWidth = "77px";
        filterCard.childNodes[1].style.opacity = "0";
      });
      filterCard.addEventListener("click", function () {
        filterCard.classList.toggle("filter-card-color-selected");
      });

      const filterColor = filterCard.getAttribute("data-name");

      if (filterColor === "Beige") {
        filterCard.style.backgroundColor = "#eae0d5df";
      }
      if (filterColor === "Black") {
        filterCard.style.backgroundColor = "#2f2f2fdf";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Blue") {
        filterCard.style.backgroundColor = "#0466c8df";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Brown") {
        filterCard.style.backgroundColor = "#c38e70df";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Clear") {
        filterCard.style.backgroundColor = "#edf6f9df";
      }
      if (filterColor === "Gold") {
        filterCard.style.backgroundColor = "#fdc500df";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Gray") {
        filterCard.style.backgroundColor = "#8e9aafdf";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Green") {
        filterCard.style.backgroundColor = "#52b788df";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Multicolor") {
        filterCard.style.backgroundImage =
          "linear-gradient(90deg, #ff1b6bdf, #45caffdf)";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Orange") {
        filterCard.style.backgroundColor = "#ff930fdf";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Pink") {
        filterCard.style.backgroundColor = "#ff5d8fdf";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Purple") {
        filterCard.style.backgroundColor = "#a100f2df";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Red") {
        filterCard.style.backgroundColor = "#ef233cdf";
        filterCard.style.color = "#ffffff";
      }
      if (filterColor === "Silver") {
        filterCard.style.backgroundColor = "#e5e5e5df";
      }
      if (filterColor === "White") {
        filterCard.style.backgroundColor = "#ffffffdf";
      }
      if (filterColor === "Yellow") {
        filterCard.style.backgroundColor = "#f3d213df";
        filterCard.style.color = "#ffffff";
      }
    }
  });
};

filterColors();

const filterGender = () => {
  const filterCards = document.querySelectorAll("a.filter-card");

  filterCards.forEach((filterCard) => {
    if (filterCard.getAttribute("data-type") === "Gender") {
      if (filterCard.getAttribute("data-name") === "Boys") {
        filterCard.style.backgroundImage =
          "linear-gradient(45deg, #0061ff5f, #60efff5f)";
      }
      if (filterCard.getAttribute("data-name") === "Girls") {
        filterCard.style.backgroundImage =
          "linear-gradient(45deg, #f492f05f, #a18dce5f)";
      }
      if (filterCard.getAttribute("data-name") === "Unisex") {
        filterCard.style.backgroundImage =
          "linear-gradient(45deg, #ebf4f55f, #b5c6e05f)";
      }
    }
  });
};

filterGender();

const filterContainerTransitition = () => {
  const filterBtn = document.querySelector("button.filter");
  const filterContainer = document.querySelector("div.filter-container");
  const auroraFilterContainer = document.querySelector(
    "div.filter-container-aurora"
  );

  filterBtn.addEventListener("click", function () {
    filterContainer.classList.toggle("filter-container-hide");
    auroraFilterContainer.classList.toggle("filter-container-aurora-hide");
  });
};

filterContainerTransitition();

const collapsibleFilterContainer = () => {
  const collapsibleFilterContainers = document.querySelectorAll(
    "div.collapsible-filter-container"
  );
  const showHideFiltersBtns = document.querySelectorAll(
    "button.show-hide-filters"
  );

  showHideFiltersBtns.forEach((showHideFiltersBtn) => {
    showHideFiltersBtn.addEventListener("click", function () {
      showHideFiltersBtn.classList.toggle("show-hide-filters-active");

      collapsibleFilterContainers.forEach((collapsibleFilterContainer) => {
        if (
          collapsibleFilterContainer.getAttribute("data-filter-category") ===
          showHideFiltersBtn.getAttribute("data-filter-category")
        ) {
          collapsibleFilterContainer.classList.toggle(
            "collapsible-filter-container-hide"
          );
        }
      });
    });
  });
};

collapsibleFilterContainer();
