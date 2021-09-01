const coverImg = document.querySelector("div.settings__cover-image");
const coverImgUploadBtn = document.querySelector(
  "div.cover-image__upload-btn input"
);

const profileImg = document.querySelector("div.settings__profile-image");
const profileImgUploadBtn = document.querySelector(
  "div.profile-image__upload-btn input"
);

const uploadedImgThumbnailHandler = (btn, img) => {
  btn.addEventListener("change", function () {
    const file = btn.files[0];
    const reader = new FileReader();

    reader.readAsDataURL(file);
    reader.addEventListener("load", function () {
      img.style.backgroundImage = `url('${reader.result}')`;
    });
  });
};

uploadedImgThumbnailHandler(coverImgUploadBtn, coverImg);
uploadedImgThumbnailHandler(profileImgUploadBtn, profileImg);
