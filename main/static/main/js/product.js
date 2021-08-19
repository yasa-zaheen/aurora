const imgChanger = () => {
  const bigImg = document.querySelector("div.img-container__big-img");
  const smallImgs = document.querySelectorAll("div.img-container__small-img");

  smallImgs.forEach((smallImg) => {
    smallImg.addEventListener("click", function () {
        bigImg.style.backgroundImage = `${smallImg.style.backgroundImage}`
    });
  });
};

imgChanger();
