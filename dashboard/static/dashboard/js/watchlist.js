const watchlistWatchlistTextChangeUI = () => {
  const watchlistWatchlistTextChanges = document.querySelectorAll(
    "p.watchlist__watchlist__text__change"
  );

  // Dynamic Icon
  watchlistWatchlistTextChanges.forEach((watchlistWatchlistTextChange) => {
    //  Creating Icon
    const watchlistWatchlistTextChangeIcon = document.createElement("span");
    watchlistWatchlistTextChangeIcon.classList.add(
      "material-icons-outlined",
      "s-m",
      "w-m"
    );
    watchlistWatchlistTextChangeIcon.style.marginLeft = "6.25px";

    // Modifying Icon According to Change
    if (
      watchlistWatchlistTextChange.getAttribute("data-change") == "decrease"
    ) {
      watchlistWatchlistTextChangeIcon.innerText = "keyboard_arrow_down";
      watchlistWatchlistTextChange.appendChild(
        watchlistWatchlistTextChangeIcon
      );
    } else if (
      watchlistWatchlistTextChange.getAttribute("data-change") == "increase"
    ) {
      watchlistWatchlistTextChangeIcon.innerText = "keyboard_arrow_up";
      watchlistWatchlistTextChange.appendChild(
        watchlistWatchlistTextChangeIcon
      );
    }
  });

  // Dynamic BG
  watchlistWatchlistTextChanges.forEach((watchlistWatchlistTextChange) => {
    // Price
    if (watchlistWatchlistTextChange.getAttribute("data-type") == "price") {
      // Increase
      if (
        watchlistWatchlistTextChange.getAttribute("data-change") == "increase"
      ) {
        watchlistWatchlistTextChange.style.backgroundColor = "#ef233c2f";
      }
      // Decrease
      else if (
        watchlistWatchlistTextChange.getAttribute("data-change") == "decrease"
      ) {
        watchlistWatchlistTextChange.style.backgroundColor = "#e0fbfc";
      }
    }
    // Stock
    else if (
      watchlistWatchlistTextChange.getAttribute("data-type") == "stock"
    ) {
      // Increase
      if (
        watchlistWatchlistTextChange.getAttribute("data-change") == "decrease"
      ) {
        watchlistWatchlistTextChange.style.backgroundColor = "#ef233c2f";
      }
      // Decrease
      else if (
        watchlistWatchlistTextChange.getAttribute("data-change") == "increase"
      ) {
        watchlistWatchlistTextChange.style.backgroundColor = "#e0fbfc";
      }
    }
  });
};

watchlistWatchlistTextChangeUI();
