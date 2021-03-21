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

