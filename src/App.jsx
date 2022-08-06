import "./index.css";
import WeatherChart from "./components/WeatherChart";

function App() {
    return (
        <div className=" min-h-screen text-blue-200 justify-center items-start flex">
            {/* <div className="mt-10 font-mono text-3xl">
                Weather Data Collector <b>Baku</b>
            </div> */}
            <WeatherChart />
        </div>
    );
}

export default App;
