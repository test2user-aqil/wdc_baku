<script>
    import Chart from "chart.js";
    import { onMount } from "svelte";
    import data from "../../public/data/data.json";

    export let day, month, year;

    let chartValues = [];
    let chartLabels = [];
    let ctx;
    let chartCanvas;

    const get = async () => {
        data.map((i) => {
            if (
                parseInt(i.date_time.slice(6, 10)) === year &&
                parseInt(i.date_time.slice(3, 5)) === month &&
                parseInt(i.date_time.slice(0, 2)) === day
            ) {
                chartValues.push(i.temperature);
                chartLabels.push(i.date_time.slice(10, 16));
            }
        });
    };

    onMount(async () => {
        await get();
        ctx = await chartCanvas.getContext("2d");
        var chart = await new Chart(ctx, {
            type: "line",
            data: {
                labels: chartLabels,
                datasets: [
                    {
                        label: "Temperature",
                        backgroundColor: "#0085ff22",
                        borderColor: "#0085ff",
                        data: chartValues,
                        fill: true,
                        lineTension: 0.5,
                        AxisID: 0,
                        pointRadius: 5,
                        pointHoverRadius: 7,
                        pointBackgroundColor: "#0085ff",
                    },
                ],
            },
            options: {
                tooltips: {
                    enabled: true,
                },
                responsive: true,
                scales: {
                    yAxes: [
                        {
                            gridLines: {
                                display: true,
                                color: "#ced6ff20",
                                drawTicks: false,
                            },

                            ticks: {
                                callback: (value) => {
                                    return value + " °C";
                                },
                                beginAtZero: true,
                                suggestedMax: 40,
                            },
                        },
                    ],

                    xAxes: [
                        {
                            gridLines: {
                                display: false,
                            },
                        },
                    ],
                },
                legend: {
                    display: false,
                    labels: {
                        fontSize: 14,
                        fontColor: "#ced6ffaa",
                        boxWidth: 20,
                        usePointStyle: false,
                    }
                },
                animation: {
                    duration: 1200,
                    onProgress: (animation) => {
                        console.log(animation.currentStep)
                    },
                },
            },
        });
    });
</script>

<canvas bind:this={chartCanvas} id="weatherChart" />
