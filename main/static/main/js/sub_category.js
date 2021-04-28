const horizontalScroller = (wrapper, rightBtn, leftBtn) => {
  var translate = 0;

  rightBtn.addEventListener("click", function () {
    translate = wrapper.scrollLeft + 179 + 25;
    wrapper.scroll({
      top: 0,
      left: translate,
      behavior: "smooth",
    });
  });
  leftBtn.addEventListener("click", function () {
    translate = wrapper.scrollLeft - 179 - 25;
    wrapper.scroll({
      top: 0,
      left: translate,
      behavior: "smooth",
    });
  });
};

const prodTypeContWrapper = document.querySelector(
  "div.prod-type-cont-wrapper"
);
const prodTypeContBtnR = document.querySelector("button.prod-type-cont-right");
const prodTypeContBtnL = document.querySelector("button.prod-type-cont-left");

horizontalScroller(prodTypeContWrapper, prodTypeContBtnR, prodTypeContBtnL);
