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

toggleAnimations();

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

const filterPrice = () => {
  const filterPriceInput = document.querySelector("input.filter-price");
  const filterPriceText = document.querySelector("p.filter-price");
  filterPriceText.innerText = `Price: USD ${filterPriceInput.value}.00`;

  filterPriceInput.addEventListener("input", function () {
    filterPriceText.innerText = `Price: USD ${filterPriceInput.value}.00`;
  });
};

filterPrice();

const filterSellerRatings = () => {
  const filterSellerRatingsInput = document.querySelector(
    "input.filter-seller-ratings"
  );
  const filterSellerRatingsText = document.querySelector(
    "p.filter-seller-ratings"
  );
  filterSellerRatingsText.innerText = `Seller rating: ${filterSellerRatingsInput.value}/5`;

  filterSellerRatingsInput.addEventListener("input", function () {
    filterSellerRatingsText.innerText = `Seller rating:  ${filterSellerRatingsInput.value}/5`;
  });
};

filterSellerRatings();

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
