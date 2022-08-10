<script>
    //import chartjs from "chart.js";
    import { onMount } from "svelte";
    import data from "../../public/data/data.json";

    export let day, month, year;

    let chartValues = [];
    let chartLabels = [];
    let ctx;
    let chartCanvas;

    var fontFamily =
        'ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI"';

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
        // ctx = await chartCanvas.getContext("2d");
        // var chart = await new chartjs(ctx, {
        //     type: "line",
        //     data: {
        //         labels: chartLabels,
        //         datasets: [
        //             {
        //                 label: "Temperature",
        //                 backgroundColor: "#0085ff22",
        //                 borderColor: "#0085ff",
        //                 data: chartValues,
        //                 fill: true,
        //                 lineTension: 0.5,
        //                 AxisID: 0,
        //                 pointRadius: 6,
        //                 pointHoverRadius: 8,
        //                 pointBackgroundColor: "#0085ff",
        //             },
        //         ],
        //     },
        //     options: {
        //         tooltips: {
        //             enabled: true,
        //             intersect: true,
        //             backgroundColor: "#0f0f19",
        //             cornerRadius: 10,
        //             titleFontSize: 15,
        //             titleFontColor: "#ced6ff",
        //             titleFontFamily: fontFamily,
        //             bodyFontSize: 14,
        //             bodyFontColor: "#ced6ff",
        //             bodyFontFamily: fontFamily,
        //             bodyFontStyle: "normal",
        //             yPadding: 10,
        //             xPadding: 10,
        //             caretPadding: 8,
        //             displayColors: false,

        //             callbacks: {
        //                 label: (value) => {
        //                     return "Temperature: " + value.value + " °C";
        //                 },
        //             },
        //         },
        //         responsive: true,
        //         scales: {
        //             yAxes: [
        //                 {
        //                     gridLines: {
        //                         display: true,
        //                         color: "#ced6ff20",
        //                         drawTicks: false,
        //                     },

        //                     ticks: {
        //                         callback: (value) => {
        //                             return value + " °C";
        //                         },
        //                         beginAtZero: true,
        //                         suggestedMax: 40,
        //                     },
        //                 },
        //             ],

        //             xAxes: [
        //                 {
        //                     gridLines: {
        //                         display: false,
        //                     },
        //                 },
        //             ],
        //         },
        //         legend: {
        //             display: true,
        //             labels: {
        //                 fontSize: 15,
        //                 fontColor: "#ced6ffdd",
        //                 fontFamily: fontFamily,
        //                 boxWidth: 8,
        //                 usePointStyle: true,
        //             },
        //         },
        //         animation: {
        //             duration: 1200,
        //         },
        //     },
        // });
    });
</script>

<!-- <canvas bind:this={chartCanvas} id="weatherChart" /> -->
<p class="font-mono text-4xl bg-dark0 py-3 px-8 rounded-lg">Chart is in progress</p>
