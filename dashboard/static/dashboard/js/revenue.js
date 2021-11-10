const crmCrmStatusButtonChangeUI = () => {
  const crmCrmStatusButtons = document.querySelectorAll(
    "button.table__statusBtn"
  );

  crmCrmStatusButtons.forEach((crmCrmStatusButton) => {
    crmCrmStatusButton.style.color = "#2f2f2f";

    switch (crmCrmStatusButton.getAttribute("data-status")) {
      case "pending":
        crmCrmStatusButton.style.backgroundColor = "#ef233c2f";
        crmCrmStatusButton.innerText = "Pending";
        break;
      case "delivering":
        crmCrmStatusButton.style.backgroundColor = "#2f2f2f2f";
        crmCrmStatusButton.innerText = "Delivering";
        break;
      case "delivered":
        crmCrmStatusButton.style.backgroundColor = "#2932412f";
        crmCrmStatusButton.innerText = "Delivered";
        break;
    }
  });
};

crmCrmStatusButtonChangeUI();
