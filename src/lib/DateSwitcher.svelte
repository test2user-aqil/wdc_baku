<script lang="ts">
    // @ts-nocheck

    import { DateStore, todaysDate, yesterdaysDate } from "../stores/DateStore";
    import { beforeUpdate } from "svelte";

    let updates = 0;
    let show = false;

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
                break;

            case "Space":
                DateStore.set(yesterdaysDate());
                break;

            default:
                console.log(e.code);
                break;
        }
    });

    beforeUpdate(() => {
        let btn = document.getElementById("keys");
        if (updates > 0) {
            if (show) {
                btn.classList.remove("hidden");
            } else {
                btn.classList.add("hidden");
            }
        }
        updates++;
    });
</script>

<div class="flex flex-col items-center">
    <div class="flex">
        <button on:click={decreaseDate}>
            <div
                class="bg-dark0 rounded-full rounded-r-none translate-x-7 border-4 border-fg w-[70px] h-12 text-3xl flex items-center justify-start px-3 focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110"
            >
                <div class="w-min">&larr;</div>
            </div>
        </button>

        <input
            type="date"
            name="dateSwitcher"
            id="dateSwitcher"
            class="z-50 cursor-pointer 3 bg-dark0 border-4 border-fg text-fg py-4 px-8 rounded-full font-mono focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110"
            bind:value={$DateStore}
        />

        <button on:click={increaseDate}>
            <div
                class="bg-dark0 rounded-full rounded-l-none -translate-x-7 border-4 border-fg w-[70px] h-12 text-3xl flex items-center justify-end px-3 focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110"
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
