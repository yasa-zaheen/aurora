const showSearchContainer = () => {
  const searchContainer = document.querySelector("div.search-cont");
  const showSearchButton = document.querySelector("button.show-search");

  showSearchButton.addEventListener("click", function () {
    showSearchButton.style.opacity = "0";
    searchContainer.style.width = "calc(100% - 25px)";
    searchContainer.style.opacity = "1";
    searchContainer.style.pointerEvents = "all";
  });
};

showSearchContainer();
