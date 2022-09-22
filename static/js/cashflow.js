
var data = {
    labels: [
     'payed',
     'not payed',
     'pending'
    ],
    datasets: [
      {
        data: [40, 10, 30],
        backgroundColor: [
          "#6777ef",
          "#F7464A",
          "#ebe6e6"
        ],
        hoverBackgroundColor: [
          "#6777ef",
          "#F7464A",
          "#ebe6e6"
        ]
       
      }]
  };
  
  
  var transChart = new Chart(document.getElementById('dochart'), {
    type: 'doughnut',
    data: data,
    options: {
      
      cutoutPercentage: 75,
        // responsive: true,
      legend: {
        display: false
      }
    }
  });
  
  Chart.pluginService.register({
    beforeDraw: function(chart) {
      var width = chart.chart.width,
          height = chart.chart.height,
          ctx = chart.chart.ctx;
  
      ctx.restore();
      var fontSize = (height / 120).toFixed(2);
      ctx.font = fontSize + "em sans-serif";
      ctx.textBaseline = "middle";
  
      var text = "15000DA",
          textX = Math.round((width - ctx.measureText(text).width) / 2),
          textY = height / 2;
  
      ctx.fillText(text, textX, textY);
      ctx.save();
    }
  });