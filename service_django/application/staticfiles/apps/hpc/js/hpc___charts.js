var hpc_nodes_chart_reload = function(snapshot){
    var ctxDoughnutMem = document.getElementById("DoughnutMem").getContext("2d");
    var DoughnutMemChart, percent_free_mem;

    var ctxDoughnutCPU = document.getElementById("DoughnutCPU").getContext("2d");
    var DoughnutCPUChart, percent_cpu_alloc;

    percent_free_mem = Math.round(100 * parseInt(free_mem) / parseInt(real_mem));
    DoughnutMemChart = new Chart(ctxDoughnutMem, {
        type: 'doughnut',
        data: {
            labels: [
                gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_1_Used_mem') + (100 - percent_free_mem) + '%',
                gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_1_Free_mem') + percent_free_mem + '%'
            ],
            datasets: [
                {
                    data: [parseInt(real_mem) - parseInt(free_mem), parseInt(free_mem)],
                    backgroundColor: [
                        "#FF6384", "#36A2EB"
                    ],
                    hoverBackgroundColor: [
                        "#FF6384", "#36A2EB"
                    ]
                }
            ]
        },
        options: {
            responsive: true
        }
    });

    percent_cpu_alloc = Math.round(100 * parseInt(cpu_alloc) / parseInt(cpu_tot));
    DoughnutCPUChart = new Chart(ctxDoughnutCPU, {
        type: 'doughnut',
        data: {
            labels: [
                gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_2_Assigned_CPUs') + percent_cpu_alloc + '%',
                gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_2_Free_CPUs') + (100 - percent_cpu_alloc) + '%'
            ],
            datasets: [
                {
                    data: [parseInt(cpu_alloc), parseInt(cpu_tot) - parseInt(cpu_alloc)],
                    backgroundColor: [
                        "#FF6384", "#FF9933"
                    ],
                    hoverBackgroundColor: [
                        "#FF6384", "#FF9933"
                    ]
                }
            ]
        },
        options: {
            responsive: true
        }
    });
    var myTimer = setInterval(function () {
        var $nodes___content = $('#nodes___content');
        var data_snapshot = $nodes___content.attr('data-snapshot');
        if (typeof data_snapshot !== 'undefined' && snapshot === data_snapshot) {
            $.ajax({
                url: $nodes___content.attr('data-url'),
                type: 'get',
                cache: false,
                dataType: 'json',
                success: function (response) {
                    //DoughnutMemChart
                    var free_mem = response.statistics.free_mem;
                    var real_mem = response.statistics.real_mem;
                    percent_free_mem = Math.round(100 * free_mem / real_mem);
                    DoughnutMemChart.data.labels[0] = gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_1_Assigned_mem') + (100 - percent_free_mem) + '%';
                    DoughnutMemChart.data.labels[1] = gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_1_Free_mem') + percent_free_mem + '%';
                    DoughnutMemChart.data.datasets[0].data[0] = real_mem - free_mem;
                    DoughnutMemChart.data.datasets[0].data[1] = free_mem;
                    DoughnutMemChart.update(0);

                    //DoughnutCPUChart
                    var cpu_alloc = response.statistics.cpu_alloc;
                    var cpu_tot = response.statistics.cpu_tot;
                    percent_cpu_alloc = Math.round(100 * cpu_alloc / cpu_tot);
                    DoughnutCPUChart.data.labels[0] = gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_2_Assigned_CPUs') + percent_cpu_alloc + '%';
                    DoughnutCPUChart.data.labels[1] = gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_2_Free_CPUs') + (100 - percent_cpu_alloc) + '%';
                    DoughnutCPUChart.data.datasets[0].data[0] = cpu_alloc;
                    DoughnutCPUChart.data.datasets[0].data[1] = cpu_tot - cpu_alloc;
                    DoughnutCPUChart.update(0);
                },
                error: function (response) {
                }
            });
        }
        else {
            clearInterval(myTimer);
        }
    }, 5000);
};