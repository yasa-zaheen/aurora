const revenueSalesGraph = () => {
  const timeRevenues = document.querySelectorAll("div.revenue__timePeriod");

  // Graph
  let ctx = document.getElementById("revenueSales__graph").getContext("2d");
  let revenueGraph = new Chart(ctx, {
    type: "bar",
    data: {
      labels: [
        "",
        "2am",
        "",
        "4am",
        "",
        "6am",
        "",
        "8am",
        "",
        "10am",
        "",
        "12pm",
        "",
        "2pm",
        "",
        "4pm",
        "",
        "6pm",
        "",
        "8pm",
        "",
        "10pm",
        "",
        "12am",
      ],
      datasets: [
        {
          label: "Revenue",
          data: JSON.parse(
            document.getElementById("t_graph_revenue").textContent
          ),
          backgroundColor: "#ee6c4d",
          borderRadius: 5,
          barThickness: 15,
        },
        {
          label: "Sales",
          data: JSON.parse(
            document.getElementById("t_graph_sales").textContent
          ),
          backgroundColor: "#293241",
          borderRadius: 5,
          barThickness: 15,
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          display: false,
        },
      },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: {
            display: false,
          },
        },
        y: {
          display: false,
        },
      },
    },
  });

  Chart.defaults.font.family = "Poppins";
  Chart.defaults.font.weight = "500";
  Chart.defaults.font.size = 12.5;

  const updateRevenueGraph = (chart, labels, revenue, sales) => {
    chart.data.labels = labels;
    chart.data.datasets[0].data = revenue;
    chart.data.datasets[1].data = sales;
    chart.update();
  };

  // Event listeners

  timeRevenues.forEach((timeRevenue) => {
    timeRevenue.addEventListener("click", () => {
      timeRevenues.forEach((timeRevenue) => {
        timeRevenue.style.backgroundColor = "#fafafa";
        timeRevenue.style.color = "#2f2f2f";
      });
      timeRevenue.style.backgroundColor = "#293241";
      timeRevenue.style.color = "#fafafa";

      if (timeRevenue.getAttribute("data-time") === "today") {
        labels = [
          "",
          "2am",
          "",
          "4am",
          "",
          "6am",
          "",
          "8am",
          "",
          "10am",
          "",
          "12pm",
          "",
          "2pm",
          "",
          "4pm",
          "",
          "6pm",
          "",
          "8pm",
          "",
          "10pm",
          "",
          "12am",
        ];

        let revenue = JSON.parse(
          document.getElementById("t_graph_revenue").textContent
        );
        let sales = JSON.parse(
          document.getElementById("t_graph_sales").textContent
        );

        updateRevenueGraph(revenueGraph, labels, revenue, sales);
      } else if (timeRevenue.getAttribute("data-time") === "yesterday") {
        labels = [
          "",
          "2am",
          "",
          "4am",
          "",
          "6am",
          "",
          "8am",
          "",
          "10am",
          "",
          "12pm",
          "",
          "2pm",
          "",
          "4pm",
          "",
          "6pm",
          "",
          "8pm",
          "",
          "10pm",
          "",
          "12am",
        ];

        let revenue = JSON.parse(
          document.getElementById("y_graph_revenue").textContent
        );
        let sales = JSON.parse(
          document.getElementById("y_graph_sales").textContent
        );

        updateRevenueGraph(revenueGraph, labels, revenue, sales);
      } else if (timeRevenue.getAttribute("data-time") === "lastweek") {
        labels = [
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday",
          "Sunday",
        ];

        let revenue = JSON.parse(
          document.getElementById("lw_graph_revenue").textContent
        );
        let sales = JSON.parse(
          document.getElementById("lw_graph_sales").textContent
        );

        updateRevenueGraph(revenueGraph, labels, revenue, sales);
      } else if (timeRevenue.getAttribute("data-time") === "28days") {
        labels = ["This week", "Last week", "3 weeks ago", "4 weeks ago"];

        let revenue = JSON.parse(
          document.getElementById("te_graph_revenue").textContent
        );
        let sales = JSON.parse(
          document.getElementById("te_graph_sales").textContent
        );

        updateRevenueGraph(revenueGraph, labels, revenue, sales);
      }
    });
  });
};

revenueSalesGraph();

const trafficGraphHandler = () => {
  const trafficGraphButtons = document.querySelectorAll("button.traffic__btn");
  const trafficCurrentlyViewingText = document.querySelector(
    "div.traffic__info p.s-l"
  );
  const trafficCurrentlyViewingTextValue = document.querySelector(
    "div.traffic__info p.s-m"
  );

  // Graph
  let ctx = document.getElementById("traffic__graph").getContext("2d");
  let trafficGraph = new Chart(ctx, {
    type: "line",
    data: {
      labels: [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
      ],
      datasets: [
        {
          label: "Product Views",
          data: JSON.parse(
            document.getElementById("lw_graph_views").textContent
          ),
          backgroundColor: "#ee6c4d",
          borderColor: "#ee6c4d2f",
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          display: false,
        },
      },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: {
            display: false,
          },
        },
        y: {
          grid: {
            display: true,
          },
          display: false,
        },
      },
    },
  });

  const updateTimeGraph = (chart, data) => {
    chart.data.datasets[0].data = data;
    chart.update();
  };

  // Event Listeners
  trafficGraphButtons.forEach((trafficGraphButton) => {
    trafficGraphButton.addEventListener("click", () => {
      trafficGraphButtons.forEach((trafficGraphButton) => {
        trafficGraphButton.style.backgroundColor = "#fafafa";
        trafficGraphButton.style.color = "#2f2f2f";
      });
      trafficGraphButton.style.backgroundColor = "#ee6c4d";
      trafficGraphButton.style.color = "#fafafa";

      if (trafficGraphButton.innerText === "Views") {
        data = JSON.parse(
          document.getElementById("lw_graph_views").textContent
        );
        updateTimeGraph(trafficGraph, data);
        trafficCurrentlyViewingText.innerText = "Total products views";
        trafficCurrentlyViewingTextValue.innerText = totalProductViews;
      } else if (trafficGraphButton.innerText === "Added to Carts") {
        data = JSON.parse(document.getElementById("lw_graph_atc").textContent);
        updateTimeGraph(trafficGraph, data);
        trafficCurrentlyViewingText.innerText = "Total products added to carts";
        trafficCurrentlyViewingTextValue.innerText = totalProductsAddedToCart;
      } else if (trafficGraphButton.innerText === "Added to Watchlist") {
        data = JSON.parse(document.getElementById("lw_graph_atwa").textContent);
        updateTimeGraph(trafficGraph, data);
        trafficCurrentlyViewingText.innerText =
          "Total products added to watchlists";
        trafficCurrentlyViewingTextValue.innerText =
          totalProductsAddedToWatchlist;
      }
    });
  });
};

trafficGraphHandler();

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
