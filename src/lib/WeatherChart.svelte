<script lang="ts">
    import chartjs from "chart.js";
    import { onMount, beforeUpdate } from "svelte";
    import data from "../../public/data/data.json";

    export let day, month, year;

    let chartValuesTemperature = [];
    let chartValuesDescription = [];
    let chartLabels = [];
    let ctx;
    let chartCanvas;
    let chart;
    let updates = 0;

    let fontFamily =
        'ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI"';

    const get = async () => {
        data.map((i) => {
            if (
                parseInt(i.date_time.slice(6, 10)) === year &&
                parseInt(i.date_time.slice(3, 5)) === month &&
                parseInt(i.date_time.slice(0, 2)) === day
            ) {
                var desc_ =
                    i.description.charAt(0).toUpperCase() +
                    i.description.slice(1);
                chartValuesTemperature.push(i.temperature);
                chartValuesDescription.push(desc_);
                chartLabels.push(i.date_time.slice(10, 16));
            }
        });
    };
    beforeUpdate(async () => {
        chartLabels = [];
        chartValuesTemperature = [];
        chartValuesDescription = [];
        ctx = null;
        await get();

        if (updates > 1) {
            chart.data.labels = chartLabels;
            chart.data.datasets[0].data = chartValuesTemperature;
            chart.update();
        }
        // console.log(updates, " (before update)");
        updates++;
    });

    onMount(async () => {
        ctx = await chartCanvas.getContext("2d");
        chart = await new chartjs(ctx, {
            type: "line",
            data: {
                labels: chartLabels,
                datasets: [
                    {
                        label: "Temperature",
                        backgroundColor: "#0085ff4f",
                        borderColor: "#0085ff",
                        data: chartValuesTemperature,
                        fill: true,
                        lineTension: 0.5,
                        AxisID: 0,
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        pointBackgroundColor: "#0085ff",
                    },
                ],
            },
            options: {
                tooltips: {
                    enabled: true,
                    intersect: true,
                    backgroundColor: "#0f0f19",
                    cornerRadius: 10,
                    titleFontSize: 15,
                    titleFontColor: "#ced6ff",
                    titleFontFamily: fontFamily,
                    bodyFontSize: 14,
                    bodyFontColor: "#ced6ff",
                    bodyFontFamily: fontFamily,
                    bodyFontStyle: "normal",
                    footerFontFamily: fontFamily,
                    footerFontStyle: "normal",
                    footerFontColor: "#ced6ff",
                    footerFontSize: 13,
                    yPadding: 10,
                    xPadding: 10,
                    caretPadding: 8,
                    displayColors: false,

                    callbacks: {
                        label: (value) => {
                            return "Temperature: " + value.value + " °C";
                        },
                        footer: (value) => {
                            return chartValuesDescription[value[0].index];
                        },
                    },
                },
                responsive: true,
                scales: {
                    yAxes: [
                        {
                            scaleLabel: {
                                display: false,
                                labelString: "Temperature (°C)",
                                fontFamily: fontFamily,
                                fontColor: "#ced6ffdd",
                            },
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
                                fontColor: "#ced6ff90",
                            },
                        },
                    ],

                    xAxes: [
                        {
                            gridLines: {
                                display: false,
                            },
                            ticks: {
                                fontColor: "#ced6ff90",
                            },
                        },
                    ],
                },
                legend: {
                    display: true,
                    labels: {
                        fontSize: 15,
                        fontColor: "#ced6ffdd",
                        fontFamily: fontFamily,
                        boxWidth: 8,
                        usePointStyle: true,
                    },
                },
                animation: {
                    duration: 1200,
                },
            },
        });
    });
</script>

<canvas bind:this={chartCanvas} id="weatherChart" width="5" height="2" />
