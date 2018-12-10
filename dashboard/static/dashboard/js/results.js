// ----> YOUR CODE HERE <----

$( document ).ready(function() {
  var data = document.getElementById("stock").innerHTML;
  document.getElementById("stock").innerHTML = "";
  var array = data.substring(1,data.length-1).split(', ');
  console.log(array)
  var ctx = document.getElementById("myChart").getContext('2d');
  var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"],
            datasets: [{
                label: 'Votre consomation en kWh mois par mois en 2017',
                data: array,
                backgroundColor: [
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)',
                    'rgb(30, 145, 53)'
                ],
                borderColor: [
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
  });
});
