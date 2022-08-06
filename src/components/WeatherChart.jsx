import Chart from "chart.js/auto";
import { Line } from "react-chartjs-2";
import { weatherData } from "../Data";

function WeatherChart() {
    console.log();
    return (
        <Line
            width={1200}
            height={600}
            data={{
                labels: weatherData.map((day) => day.date_time),
                datasets: [
                    {
                        label: "temperature",
                        data: weatherData.map((day) => day.temperature),
                        borderWidth: 1,
                        fill: true,
                        tension: 0.5,
                    },
                ],
            }}
        />
    );
}

export default WeatherChart;
