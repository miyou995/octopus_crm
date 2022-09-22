"use strict";

$(function () {
  chart1();
    // chart2();
    chart3();
    // chart4();
    // chart5();

    // select all on checkbox click
    $("[data-checkboxes]").each(function () {
        var me = $(this),
            group = me.data('checkboxes'),
            role = me.data('checkbox-role');

        me.change(function () {
            var all = $('[data-checkboxes="' + group + '"]:not([data-checkbox-role="dad"])'),
                checked = $('[data-checkboxes="' + group + '"]:not([data-checkbox-role="dad"]):checked'),
                dad = $('[data-checkboxes="' + group + '"][data-checkbox-role="dad"]'),
                total = all.length,
                checked_length = checked.length;

            if (role == 'dad') {
                if (me.is(':checked')) {
                    all.prop('checked', true);
                } else {
                    all.prop('checked', false);
                }
            } else {
                if (checked_length >= total) {
                    dad.prop('checked', true);
                } else {
                    dad.prop('checked', false);
                }
            }
        });
    });



});


function chart1() {
    var options = {
        chart: {
            height: 230,
            type: "line",
            shadow: {
                enabled: true,
                color: "#000",
                top: 18,
                left: 7,
                blur: 10,
                opacity: 1
            },
            toolbar: {
                show: false
            }
        },
        colors: ["#786BED", "#999b9c"],
        dataLabels: {
            enabled: true
        },
        stroke: {
            curve: "smooth"
        },
        series: [{
            name: "High - 2019",
            data: [5, 15, 14, 36, 32, 32]
        },
        {
            name: "Low - 2019",
            data: [7, 11, 30, 18, 25, 13]
        }
        ],
        grid: {
            borderColor: "#e7e7e7",
            row: {
                colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
                opacity: 0.0
            }
        },
        markers: {
            size: 6
        },
        xaxis: {
            categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],

            labels: {
                style: {
                    colors: "#9aa0ac"
                }
            }
        },
        yaxis: {
            title: {
                text: "Income"
            },
            labels: {
                style: {
                    color: "#9aa0ac"
                }
            },
            min: 5,
            max: 40
        },
        legend: {
            position: "top",
            horizontalAlign: "right",
            floating: true,
            offsetY: -25,
            offsetX: -5
        }
    };

    var chart = new ApexCharts(document.querySelector("#chart1"), options);

    chart.render();
}

// function chart2() {
//     var options = {
//         chart: {
//     height: 170,
//     type: "radialBar"
//   },
  
//   series: [67],

//   plotOptions: {
//     radialBar: {
//       hollow: {
//         margin: 15,
//         size: "50%"
//       },
     
//       dataLabels: {
//         showOn: "always",
//         name: {        
//           show: false,          
//         },
//         value: {   
//             offsetY: 4,           
//           color: "#111",
//           fontSize: "15px",
//           show: true
//         }
//       }
//     }
//   },

//   stroke: {
//     lineCap: "round",
//   },
//   labels: ["Progress"]
//     }

//     var chart = new ApexCharts(
//         document.querySelector("#chart2"),
//         options
//     );

//     chart.render();

// }

function chart3() {
    var options = {
        chart: {
    height: 170,
    type: "radialBar"
  },
  
  series: [67],

  plotOptions: {
    radialBar: {
      hollow: {
        margin: 15,
        size: "50%"
      },
     
      dataLabels: {
        showOn: "always",
        name: {        
          show: false,          
        },
        value: {   
            offsetY: 4,           
          color: "#222",
          fontSize: "15px",
          show: true
        }
      }
    }
  },

  stroke: {
    lineCap: "round",
    color:  ['#546E7A', '#E91E63'],
  },
  labels: ["Progress"]
    }

    var chart = new ApexCharts(
        document.querySelector("#chart3"),
        options
    );

    chart.render();
}

// function chart4() {
//     var options = {
//         chart: {
//     height: 170,
//     type: "radialBar"
//   },
  
//   series: [67],

//   plotOptions: {
//     radialBar: {
//       hollow: {
//         margin: 15,
//         size: "50%"
//       },
     
//       dataLabels: {
//         showOn: "always",
//         name: {        
//           show: false,          
//         },
//         value: {   
//             offsetY: 4,           
//           color: "#111",
//           fontSize: "15px",
//           show: true
//         }
//       }
//     }
//   },

//   stroke: {
//     lineCap: "round",
//   },
//   labels: ["Progress"]
//     }

//     var chart = new ApexCharts(
//         document.querySelector("#chart4"),
//         options
//     );

//     chart.render();
// }

// function chart5() {
//     var options = {
//         chart: {
//     height: 170,
//     type: "radialBar"
//   },
  
//   series: [67],

//   plotOptions: {
//     radialBar: {
//       hollow: {
//         margin: 15,
//         size: "50%"
//       },
     
//       dataLabels: {
//         showOn: "always",
//         name: {        
//           show: false,          
//         },
//         value: {   
//             offsetY: 4,           
//           color: "#111",
//           fontSize: "15px",
//           show: true
//         }
//       }
//     }
//   },
//   stroke: {
//     lineCap: "round",
//   },
//   labels: ["Progress"]
//     }

//     var chart = new ApexCharts(
//         document.querySelector("#chart5"),
//         options
//     );

//     chart.render();
// }


// const ctx = document.getElementById('myChart').getContext('2d');
// const myChart = new Chart(ctx, {
//     type: 'line',
//     data : {
//         tooltip: {
//             enabled: false,
//         },
//         labels: [
          
//         ],
//         datasets: [{
//           label: 'My First Dataset',
//           data: [65, 59, 80, 81, 56, 55, 40],
//           fill: false,
//           borderColor: 'rgb(75, 192, 192)',
//           tension: 0.1
//         }]
//       }
// });


var balance_chart = document.getElementById("chart-1").getContext('2d');

var balance_chart_bg_color = balance_chart.createLinearGradient(0, 0, 0, 70);
balance_chart_bg_color.addColorStop(0, 'rgba(120, 107, 236, .2)');
balance_chart_bg_color.addColorStop(1, 'rgba(120, 107, 236, 0)');

var myChart = new Chart(balance_chart, {
  type: 'line',
  data: {
    labels: ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001'],
    datasets: [{
      label: 'Balance',
      data: [50, 61, 80, 50, 72, 52, 60, 41, 30, 45, 70, 40],
      backgroundColor: balance_chart_bg_color,
      borderWidth: 3,
      borderColor: 'rgba(41, 192, 177, 1)',
      pointBorderWidth: 0,
      pointBorderColor: 'transparent',
      pointRadius: 3,
      pointBackgroundColor: 'transparent',
      pointHoverBackgroundColor: 'rgba(120, 107, 236,1)',
    }]
  },
  options: {
    layout: {
      padding: {
        bottom: -1,
        left: -1
      }
    },
    legend: {
      display: false
    },

    scales: {
      yAxes: [{
        gridLines: {
          display: false,
          drawBorder: false,
        },
        ticks: {
          beginAtZero: true,
          display: false,
          fontColor: "#9aa0ac", // Font Color
        }
      }],
      xAxes: [{
        gridLines: {
          drawBorder: false,
          display: false,
        },
        ticks: {
          display: false,
          fontColor: "#9aa0ac", // Font Color
        }
      }]
    },
  }
});

var sales_chart = document.getElementById("chart-2").getContext('2d');

var myChart = new Chart(sales_chart, {
  type: 'line',
  data: {
    labels: ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001'],
    datasets: [{
      label: 'Sales',
      data: [70, 62, 44, 40, 21, 63, 82, 52, 50, 31, 70, 50],
      borderWidth: 2,
      backgroundColor: balance_chart_bg_color,
      borderWidth: 3,
      borderColor: 'rgba(156, 39, 176, 1)',
      pointBorderWidth: 0,
      pointBorderColor: 'transparent',
      pointRadius: 3,
      pointBackgroundColor: 'transparent',
      pointHoverBackgroundColor: 'rgba(120, 107, 236,1)',
    }]
  },
  options: {
    layout: {
      padding: {
        bottom: -1,
        left: -1
      }
    },
    legend: {
      display: false
    },
    scales: {
      yAxes: [{
        gridLines: {
          display: false,
          drawBorder: false,
        },
        ticks: {
          beginAtZero: true,
          display: false
        }
      }],
      xAxes: [{
        gridLines: {
          drawBorder: false,
          display: false,
        },
        ticks: {
          display: false
        }
      }]
    },
  }
});
var sales_chart = document.getElementById("chart-3").getContext('2d');

var myChart = new Chart(sales_chart, {
  type: 'line',
  data: {
    labels: ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001'],
    datasets: [{
      label: 'Sales',
      data: [63, 82, 52, 50, 31, 70, 50, 70, 62, 44, 40, 21],
      borderWidth: 2,
      backgroundColor: balance_chart_bg_color,
      borderWidth: 3,
      borderColor: 'rgba(76, 175, 80, 1)',
      pointBorderWidth: 0,
      pointBorderColor: 'transparent',
      pointRadius: 3,
      pointBackgroundColor: 'transparent',
      pointHoverBackgroundColor: 'rgba(120, 107, 236,1)',
    }]
  },
  options: {
    layout: {
      padding: {
        bottom: -1,
        left: -1
      }
    },
    legend: {
      display: false
    },
    scales: {
      yAxes: [{
        gridLines: {
          display: false,
          drawBorder: false,
        },
        ticks: {
          beginAtZero: true,
          display: false
        }
      }],
      xAxes: [{
        gridLines: {
          drawBorder: false,
          display: false,
        },
        ticks: {
          display: false
        }
      }]
    },
  }
});
