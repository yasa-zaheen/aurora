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

const prodDisImgChanger = () => {
  const prodSelImgBtns = document.querySelectorAll("button.prod-sel-img");
  const prodDisImg = document.querySelector("div.prod-dis-img img.vis");

  prodSelImgBtns.forEach((prodSelImgBtn) => {
    prodSelImgBtn.addEventListener("click", function () {
      prodDisImg.style.transform = "scale(0.95,0.95)";
      prodDisImg.style.opacity = "0.5";
      prodDisImg.style.transition = "0.1s ease all";

      prodDisImg.addEventListener("transitionend", function () {
        prodDisImg.src = prodSelImgBtn.childNodes[1].src;
        prodDisImg.style.opacity = "1";
        prodDisImg.style.transform = "scale(1, 1)";
      });
    });
  });
};

prodDisImgChanger();

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

const prodCardBtnAnimations = (button, color) => {
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
};

const prodCartBtn = document.querySelector("button.prod-cart");
const prodBuyNowBtn = document.querySelector("button.prod-buy-now");
const prodSaveBtn = document.querySelector("button.prod-save");
const prodWatchlistBtn = document.querySelector("button.prod-watchlist");

const addToCartBtns = document.querySelectorAll("button.prod-add-to-cart");
const addToWishlistBtns = document.querySelectorAll(
  "button.prod-add-to-wishlist"
);
const addToWatchlistBtns = document.querySelectorAll(
  "button.prod-add-to-watchlist"
);

prodCardBtnAnimations(prodCartBtn, "#2f2f2f");
prodCardBtnAnimations(prodBuyNowBtn, "#293241");
prodCardBtnAnimations(prodSaveBtn, "#ef233c");
prodCardBtnAnimations(prodWatchlistBtn, "#3d5a80");

addToCartBtns.forEach((addToCartBtn) => {
  prodCardBtnAnimations(addToCartBtn, "#ef233c");
});
addToWishlistBtns.forEach((addToWishlistBtn) => {
  prodCardBtnAnimations(addToWishlistBtn, "#ee6c4d");
});
addToWatchlistBtns.forEach((addToWatchlistBtn) => {
  prodCardBtnAnimations(addToWatchlistBtn, "#3d5a80");
});
