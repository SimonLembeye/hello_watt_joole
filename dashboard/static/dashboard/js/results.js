// ----> YOUR CODE HERE <----
$( document ).ready(function() {
  // Traitement des données pour les utiliser en js
  var data = document.getElementById("stock").innerHTML;
  document.getElementById("stock").innerHTML = "";
  var array = data.substring(1,data.length-1).split(', ');

  // Graphique réalisé grâce à graph.js
  var ctx = document.getElementById("myChart").getContext('2d');
  var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"],
            datasets: [{
                label: 'Consommation en kWh',
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
