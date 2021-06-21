const revenueSalesGraph = () => {
  let ctx = document.getElementById("revenueSales__graph").getContext("2d");
  let myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00"],
      datasets: [
        {
          label: "Revenue",
          data: [6, 2, 8, 7, 3, 10],
          backgroundColor: "#ee6c4d",
          borderRadius: 15,
          barThickness: 15,
        },
        {
          label: "Sales",
          data: [6, 2, 8, 7, 3, 10],
          backgroundColor: "#293241",
          borderRadius: 15,
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
          grid: {
            display: true,
          },
          display: false,
        },
      },
    },
  });

  Chart.defaults.font.family = "Poppins";
  Chart.defaults.font.weight = "600";
  Chart.defaults.font.size = 12.5;
};

revenueSalesGraph();

const trafficGraph = () => {
  let ctx = document.getElementById("traffic__graph").getContext("2d");
  let myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00"],
      datasets: [
        {
          label: "Product Views",
          data: [6984, 2234, 8098, 7092, 3142, 10120],
          backgroundColor: "#ee6c4d",
          borderColor: "#ee6c4d2f",
        },
        {
          label: "Unique Viewers",
          data: [152, 235, 481, 326, 911],
          backgroundColor: "#293241",
          borderColor: "#2932412f",
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
};

trafficGraph();
