const imageResizer = () => {
  const visImgs = document.querySelectorAll("img.vis");

  visImgs.forEach((visImg) => {
    if (visImg.clientWidth > visImg.clientHeight) {
      visImg.style.width = "auto";
      visImg.style.height = "100%";
    }
  });
};

const prodCardBtnAnimations = (buttons, color) => {
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      button.classList.toggle("toggled");

      if (button.classList.contains("toggled")) {
        button.childNodes[1].style.color = color;
        button.childNodes[1].style.opacity = "1";
      } else {
        button.childNodes[1].style.color = "#2f2f2f";
        button.childNodes[1].style.opacity = "0.5";
      }
    });
  });
};

const catContainerScrollingBtns = () => {
  const categoryContainerWrapper = document.querySelector(
    "div.cat-cont-wrapper"
  );
  const catContainerBtnRight = document.querySelector("button.cat-cont-right");
  const catContainerBtnLeft = document.querySelector("button.cat-cont-left");

  var translate = 0;

  catContainerBtnRight.addEventListener("click", function () {
    translate = categoryContainerWrapper.scrollLeft + 144 + 25;
    categoryContainerWrapper.scroll({
      top: 0,
      left: translate,
      behavior: "smooth",
    });
  });
  catContainerBtnLeft.addEventListener("click", function () {
    translate = categoryContainerWrapper.scrollLeft - 144 - 25;
    categoryContainerWrapper.scroll({
      top: 0,
      left: translate,
      behavior: "smooth",
    });
  });

  // if (Math.abs(translate) > scrollingLimit) {
  //   catContainerBtnRight.addEventListener("click", function () {
  //     translate -= 0;
  //     categoryContainer.style.transform = `translateX(${translate}px)`;
  //   });
  //   catContainerBtnLeft.addEventListener("click", function () {
  //     translate += 0;
  //     categoryContainer.style.transform = `translateX(${translate}px)`;
  //   });
  // } else {
  //   catContainerBtnRight.addEventListener("click", function () {
  //     translate -= 144 + 25;
  //     categoryContainer.style.transform = `translateX(${translate}px)`;
  //     console.log(Math.abs(translate));
  //     console.log(scrollingLimit);
  //   });
  //   catContainerBtnLeft.addEventListener("click", function () {
  //     translate += 144 + 25;
  //     categoryContainer.style.transform = `translateX(${translate}px)`;
  //     console.log(Math.abs(translate));
  //     console.log(scrollingLimit);
  //   });
  // }
};

catContainerScrollingBtns();

const addToCartBtns = document.querySelectorAll("button.prod-add-to-cart");
const addToWishlistBtns = document.querySelectorAll(
  "button.prod-add-to-wishlist"
);
const addToWatchlistBtns = document.querySelectorAll(
  "button.prod-add-to-watchlist"
);

imageResizer();

prodCardBtnAnimations(addToCartBtns, "#ef233c");
prodCardBtnAnimations(addToWishlistBtns, "#ee6c4d");
prodCardBtnAnimations(addToWatchlistBtns, "#3d5a80");
