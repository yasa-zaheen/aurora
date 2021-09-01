const uploadedImgThumbnailHandler = () => {
  const coverImg = document.querySelector("div.settings__cover-image");
  const coverImgUploadBtn = document.querySelector(
    "div.cover-image__upload-btn input"
  );

  coverImgUploadBtn.addEventListener("change", function () {
    const file = coverImgUploadBtn.files[0];
    const reader = new FileReader();

    reader.readAsDataURL(file);
    reader.addEventListener("load", function () {
      coverImg.style.backgroundImage = `url('${reader.result}')`;
    });
  });
};

uploadedImgThumbnailHandler();
