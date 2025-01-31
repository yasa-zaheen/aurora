const sellerProdsProdCardBtnPop = () => {
  const addToCartButtons = document.querySelectorAll("button.add-to-cart");
  const shippingButtons = document.querySelectorAll("button.shipping");
  const priceButtons = document.querySelectorAll("button.price");
  const saveButtons = document.querySelectorAll("button.save");
  const accountButtons = document.querySelectorAll("button.account");

  const showHidePop = (buttons) => {
    buttons.forEach((button) => {
      button.addEventListener("mouseover", function () {
        button.previousElementSibling.style.transform = "scale(1, 1)";
      });
      button.addEventListener("mouseout", function () {
        button.previousElementSibling.style.transform = "scale(0, 0)";
      });
    });
  };

  showHidePop(addToCartButtons);
  showHidePop(shippingButtons);
  showHidePop(priceButtons);
  showHidePop(saveButtons);
  showHidePop(accountButtons);
};

sellerProdsProdCardBtnPop();

const imageResizer = () => {
  const visImgs = document.querySelectorAll("img.vis");

  visImgs.forEach((visImg) => {
    if (visImg.clientWidth > visImg.clientHeight) {
      visImg.style.width = "auto";
      visImg.style.height = "100%";
    }
  });
};

imageResizer();

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

const addToCartBtns = document.querySelectorAll("button.prod-add-to-cart");
const addToWishlistBtns = document.querySelectorAll(
  "button.prod-add-to-wishlist"
);
const addToWatchlistBtns = document.querySelectorAll(
  "button.prod-add-to-watchlist"
);

prodCardBtnAnimations(addToCartBtns, "#ef233c");
prodCardBtnAnimations(addToWishlistBtns, "#ee6c4d");
prodCardBtnAnimations(addToWatchlistBtns, "#3d5a80");
