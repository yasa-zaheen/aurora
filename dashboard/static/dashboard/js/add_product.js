const uploadedImgThumbnailHandler = () => {
  const imgUploadBtns = document.querySelectorAll(
    "input.addProduct__uploadBtn"
  );

  imgUploadBtns.forEach((imgUploadBtn) => {
    imgUploadBtn.addEventListener("change", function () {
      const file = imgUploadBtn.files[0];
      const image = imgUploadBtn.parentElement.childNodes[1];
      const icon = imgUploadBtn.parentElement.childNodes[3];

      const reader = new FileReader();
      reader.readAsDataURL(file);

      reader.addEventListener("load", function () {
        image.src = reader.result;
        icon.style.display = "none";
        if (image.clientWidth > image.clientHeight) {
          image.style.width = "auto";
          image.style.height = "100%";
        } else if (image.clientWidth < image.clientHeight) {
          image.style.height = "auto";
          image.style.width = "100%";
        }
      });
    });
  });
};

uploadedImgThumbnailHandler();
