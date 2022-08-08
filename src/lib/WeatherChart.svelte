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
                        backgroundColor: "#0085ff33",
                        borderColor: "#0085ff",
                        data: chartValues,
                        fill: true,
                        lineTension: 0.5,
                    },
                ],
            },
        });
    });
</script>

<canvas bind:this={chartCanvas} id="myChart" />
