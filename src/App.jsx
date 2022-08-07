import "./index.css";
import WeatherChart from "./components/WeatherChart";

function App() {
    return (
        <div className="text-fg max-w-5xl mx-auto justify-start items-center flex flex-col gap-10 py-16">
            <div className="font-mono lg:text-5xl md:text-4xl text-3xl transition-all duration-300">
                Weather Data Collector <span className="underline">Baku</span>
            </div>
        </div>
    );
}

export default App;
