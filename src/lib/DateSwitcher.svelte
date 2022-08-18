<script lang="ts">
    // @ts-nocheck

    import { DateStore, todaysDate, yesterdaysDate } from "../stores/DateStore";
    import { afterUpdate } from "svelte";

    let show = false;
    let btn;
    let date_switcher;
    let decrease_btn;
    let increase_btn;

    function decreaseDate() {
        document.getElementById("dateSwitcher").stepDown(1);
        DateStore.set(document.getElementById("dateSwitcher").value);
    }
    function increaseDate() {
        document.getElementById("dateSwitcher").stepUp(1);
        DateStore.set(document.getElementById("dateSwitcher").value);
    }

    document.addEventListener("keydown", (e) => {
        switch (e.code) {
            case "ArrowRight":
                increaseDate();
                break;

            case "ArrowLeft":
                decreaseDate();
                break;

            case "Enter":
            case "Home":
                DateStore.set(todaysDate());
                handleDateSwitcher();
                break;

            case "Space":
                handleDateSwitcher();
                DateStore.set(yesterdaysDate());
                break;

            default:
                console.log(e.code);
                break;
        }
    });

    function handleDateSwitcher() {
        date_switcher = document.getElementById("dateSwitcher");
        increase_btn = document.getElementById("increaseDate");
        decrease_btn = document.getElementById("decreaseDate");
        if (date_switcher.value !== todaysDate && date_switcher.value !== "2022-07-23") {
            increase_btn.classList.remove("invisible");
            decrease_btn.classList.remove("invisible");
        }
        if (date_switcher.value === todaysDate()) {
            increase_btn.classList.add("invisible");
        }
        if (date_switcher.value === "2022-07-23") {
            decrease_btn.classList.add("invisible");
        }
    }

    afterUpdate(() => {
        btn = document.getElementById("keys");
        date_switcher = document.getElementById("dateSwitcher");
        increase_btn = document.getElementById("increaseDate");
        decrease_btn = document.getElementById("decreaseDate");
        if (show) {
            btn.classList.remove("hidden");
        } else {
            btn.classList.add("hidden");
        }

        if (date_switcher.value !== todaysDate && date_switcher.value !== "2022-07-23") {
            increase_btn.classList.remove("invisible");
            decrease_btn.classList.remove("invisible");
        }
        if (date_switcher.value === todaysDate()) {
            increase_btn.classList.add("invisible");
        }
        if (date_switcher.value === "2022-07-23") {
            decrease_btn.classList.add("invisible");
        }
    });

    function date_indicator(a, b) {
        const day__ = 1000 * 60 * 60 * 24;
        const month__ = day__ * 30;
        const year__ = day__ * 365;

        let days = Math.round((b - a) / day__);
        let months = Math.round((b - a) / month__);
        let years = Math.round((b - a) / year__);

        if (days < 0) {
            return "This app can't predict the future";
        }
        if (days === 0) {
            return "Today";
        }
        if (days === 1) {
            return "Yesterday";
        }
        if (days < 30) {
            return days + " days ago";
        }
        if (days > 35 && days % 30 > 5 && months < 12) {
            return months + " months, " + (days % 30) + " days ago";
        }
        if (days >= 30 && months < 12) {
            return months + " months ago";
        }
        if (months >= 12 && months % 12 > 1) {
            return years + " years, " + (months % 12) + " months ago";
        }
        if (months >= 12) {
            return years + " years ago";
        } else {
            return days;
        }
    }
</script>

<div class="flex flex-col items-center">
    <code class="text-xs opacity-70 pb-1 text-center"
        >{date_indicator(new Date($DateStore), new Date(todaysDate()))}</code
    >
    <div class="flex">
        <button id="decreaseDate" on:click={decreaseDate}>
            <div
                class="bg-dark0 rounded-full rounded-r-none translate-x-7 border-4 border-fg w-[70px] h-12 text-3xl flex items-center justify-start px-3 focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110 transition-shadow-color"
            >
                <div class="w-min">&larr;</div>
            </div>
        </button>

        <input
            type="date"
            name="dateSwitcher"
            id="dateSwitcher"
            min="2022-07-23"
            max={todaysDate()}
            class="z-50 cursor-pointer 3 bg-dark0 border-4 border-fg text-fg py-4 px-8 rounded-full font-mono focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110"
            bind:value={$DateStore}
        />

        <button id="increaseDate" on:click={increaseDate}>
            <div
                class="bg-dark0 rounded-full rounded-l-none -translate-x-7 border-4 border-fg w-[70px] h-12 text-3xl flex items-center justify-end px-3 focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110 transition-shadow-color"
            >
                <div class="w-min">&rarr;</div>
            </div>
        </button>
    </div>
    <button
        on:click={() => {
            show = !show;
        }}>&bull;&bull;&bull;</button
    >
    <code id="keys" class="text-xs opacity-70 pt-1 text-center hidden"
        >Use Arrow keys to navigate,<br />Enter to return today's date<br />Space to return
        yesterday's date</code
    >
</div>
