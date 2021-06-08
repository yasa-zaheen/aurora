const cartProductImageSquare = () => {
  const cartProductImages = document.querySelectorAll(
    "div.cart__product__image"
  );

  cartProductImages.forEach((cartProductImage) => {
    cartProductImage.style.width = cartProductImage.clientHeight;
  });
};

cartProductImageSquare();
