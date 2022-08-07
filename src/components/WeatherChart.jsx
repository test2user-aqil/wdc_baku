import { useEffect, useState} from "react";
import Chart from "chart.js/auto";
import { Line } from "react-chartjs-2";

function WeatherChart({ day, month, year }) {
    console.log('rendered')
    const [data, setData] = useState(null);
    const [_, set_] = useState(0);


    var picked = [];
    var picked_temperature = [];
    var picked_date_time = [];

    useEffect(() => {
        fetch("/data/data.json")
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                // year -> i.date_time.slice(6, 10)
                // month -> i.date_time.slice(3, 5)
                // day -> i.date_time.slice(0, 2)

                data.map((i) => {
                    if (
                        parseInt(i.date_time.slice(6, 10)) === year &&
                        parseInt(i.date_time.slice(3, 5)) === month &&
                        parseInt(i.date_time.slice(0, 2)) === day
                    ) {
                        
                        picked.push(i);
                        picked_temperature.push(parseInt(i.temperature));
                        picked_date_time.push(i.date_time);
                    }
                });
            })
            .catch((err) => console.error(err));
    }, []);



    return (
        <div>
            <Line
            width={1200}
            height={600}
            data={{
                labels: [1, 2, 3, 4],
                datasets: [
                    {
                        label: "temperature",
                        data: picked_temperature,
                        borderWidth: 1,
                        fill: true,
                        tension: 0.5,
                    },
                ],
            }}
        />
        </div>
    );
}

export default WeatherChart;
