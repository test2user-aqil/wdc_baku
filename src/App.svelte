<script>
    import Hero from "./lib/Hero.svelte";
    import WeatherChart from "./lib/WeatherChart.svelte";
    import DateSwitcher from "./lib/DateSwitcher.svelte";

    let day = 23;
</script>

<main
    class="text-fg max-w-5xl mx-auto justify-start items-center flex flex-col gap-10 py-16"
>
    <Hero />
    <DateSwitcher />

    <button
        on:click={() => {
            day++;
            console.log(day);
        }}>+++</button
    >

    <WeatherChart {day} month={7} year={2022} />
</main>
