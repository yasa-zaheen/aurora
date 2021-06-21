var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
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
