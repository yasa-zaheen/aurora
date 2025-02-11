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

const subCategoryContainerWrapper = document.querySelector(
  "div.sub-cat-cont-wrapper"
);
const subCatContBtnR = document.querySelector("button.sub-cat-cont-right");
const subCatContBtnL = document.querySelector("button.sub-cat-cont-left");

horizontalScroller(subCategoryContainerWrapper, subCatContBtnR, subCatContBtnL);
