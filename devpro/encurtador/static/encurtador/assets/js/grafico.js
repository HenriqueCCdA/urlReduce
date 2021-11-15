function plota(x, y){

    let multipleBarChart = document.getElementById('multipleBarChart').getContext('2d')

    let myMultipleBarChart = new Chart(multipleBarChart, {
        type: 'bar',

        // Como usar a Lib ChartJS com Django -> https://medium.com/code-rocket-blog/trabalhando-com-gr%C3%A1ficos-no-django-usando-chart-js-495aa6abbe0f 

        data: {
            labels: x,
            datasets: [{
                label: "Total de Cliques por Dia",
                backgroundColor: '#005490',
                borderColor: '#005490',
                data: y,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'bottom'
            },
            title: {
                display: true,
                //text: 'Gráfico de Cliques por Dia'
            },
            tooltips: {
                mode: 'index',
                intersect: false
            },
            responsive: true,
            scales: {
                xAxes: [{
                    stacked: true,
                }],
                yAxes: [{
                    stacked: true
                }]
            }
        }
    });
}