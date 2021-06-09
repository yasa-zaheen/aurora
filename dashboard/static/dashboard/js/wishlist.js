const wishlistProductImageSquare = () => {
  const wishlistProductImages = document.querySelectorAll(
    "div.wishlist__product__image"
  );

  wishlistProductImages.forEach((wishlistProductImage) => {
    wishlistProductImage.style.width = wishlistProductImage.clientHeight;
  });
};

wishlistProductImageSquare();
