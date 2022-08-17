<script lang="ts">
    import Hero from "./lib/Hero.svelte";
    import WeatherChart from "./lib/WeatherChart.svelte";
    import DateSwitcher from "./lib/DateSwitcher.svelte";
    import Footer from "./lib/Footer.svelte";

    import { DateStore } from "./stores/DateStore";
</script>

<main class="text-fg max-w-5xl mx-auto justify-start items-center flex flex-col gap-10 pt-16">
    <Hero />
    <DateSwitcher />

    <WeatherChart
        day={parseInt($DateStore.slice(8, 10))}
        month={parseInt($DateStore.slice(5, 7))}
        year={parseInt($DateStore.slice(0, 4))}
    />

    <Footer />
</main>
