<script>
    import Hero from "./lib/Hero.svelte";
    import WeatherChart from "./lib/WeatherChart.svelte";
    import DateSwitcher from "./lib/DateSwitcher.svelte";
</script>

<main
    class="text-fg max-w-5xl mx-auto justify-start items-center flex flex-col gap-10 py-16"
>
    <Hero />
    <DateSwitcher />
    <WeatherChart day={1} month={8} year={2022} />
</main>
