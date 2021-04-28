function square_dom_element(element) {
  element.style.height = element.clientWidth;
}

square_dom_element(document.querySelector("div.wishlist-info"));
square_dom_element(document.querySelector("div.watchlist-info"));
