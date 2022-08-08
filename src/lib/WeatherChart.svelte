<script>
	import chartjs from 'chart.js';
	let chartData;
	import { onMount } from 'svelte';

	let chartValues = [20, 10, 5, 2, 20, 30, 45];
	let chartLabels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
	let ctx;
	let chartCanvas;

	onMount(async (promise) => {
		  ctx = chartCanvas.getContext('2d');
			var chart = new chartjs(ctx, {
				type: 'line',
				data: {
						labels: chartLabels,
						datasets: [{
								label: 'Temperature',
								backgroundColor: '#0085ff',
								borderColor: '#0085ffaa',
								data: chartValues
						}]
				}
		});

	});

</script>

<canvas bind:this={chartCanvas} id="myChart"></canvas>