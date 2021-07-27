const toggleAnimations = () => {
  const toggleBtns = document.querySelectorAll("button.toggle");

  toggleBtns.forEach((toggleBtn) => {
    toggleBtn.addEventListener("click", function () {
      toggleBtn.classList.toggle("toggled");

      if (toggleBtn.classList.contains("toggled")) {
        toggleBtn.style.color = toggleBtn.getAttribute("data-color");
      } else {
        toggleBtn.style.color = "black";
      }
    });
  });
};

// const prodCardBtnAnimations = (buttons, color) => {
//   buttons.forEach((button) => {
//     button.addEventListener("click", function () {
//       button.classList.toggle("toggled");

//       if (button.classList.contains("toggled")) {
//         button.childNodes[1].style.color = color;
//         button.childNodes[1].style.opacity = "1";
//       } else {
//         button.childNodes[1].style.color = "#2f2f2f";
//         button.childNodes[1].style.opacity = "0.5";
//       }
//     });
//   });
// };

// const addToCartBtns = document.querySelectorAll("button.prod-add-to-cart");
// const addToWishlistBtns = document.querySelectorAll(
//   "button.prod-add-to-wishlist"
// );
// const addToWatchlistBtns = document.querySelectorAll(
//   "button.prod-add-to-watchlist"
// );

// const catContWrapper = document.querySelector("div.cat-cont-wrapper");
// const catContBtnR = document.querySelector("button.cat-cont-right");
// const catContBtnL = document.querySelector("button.cat-cont-left");

// horizontalScroller(catContWrapper, catContBtnR, catContBtnL);

// imageResizer();

// prodCardBtnAnimations(addToCartBtns, "#ef233c");
// prodCardBtnAnimations(addToWishlistBtns, "#ee6c4d");
// prodCardBtnAnimations(addToWatchlistBtns, "#3d5a80");
