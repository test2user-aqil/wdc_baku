<script lang="ts">
    // @ts-nocheck

    import { DateStore, todaysDate } from "../stores/DateStore";

    function decreaseDate() {
        document.getElementById("dateSwitcher").stepDown(1);
        DateStore.set(document.getElementById("dateSwitcher").value);
    }
    function increaseDate() {
        document.getElementById("dateSwitcher").stepUp(1);
        DateStore.set(document.getElementById("dateSwitcher").value);
    }

    document.addEventListener("keydown", (e) => {
        if (e.code == "ArrowRight") {
            increaseDate();
        }
        if (e.code == "ArrowLeft") {
            decreaseDate();
        }
        if (e.code == "Enter" || e.code == "Home") {
            DateStore.set(todaysDate());
        }
        // console.log(e.code);
    });
</script>

<div class="flex flex-col items-center">
    <div class="flex">
        <button on:click={decreaseDate}>
            <div
                class="bg-dark0 rounded-full border-4 border-fg w-16 h-16 text-3xl flex items-center justify-center focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110"
            >
                <div class="w-min">&#x2190;</div>
            </div>
        </button>

        <input
            type="date"
            name="dateSwitcher"
            id="dateSwitcher"
            class="cursor-pointer mx-3 bg-dark0 border-4 border-fg text-fg py-4 px-12 rounded-full font-mono focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110"
            bind:value={$DateStore}
        />

        <button on:click={increaseDate}>
            <div
                class="bg-dark0 rounded-full border-4 border-fg w-16 h-16 text-3xl flex items-center justify-center focus:outline-none outline-none shadow-xl shadow-accent1/10 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover duration-300 hover:brightness-110"
            >
                <div class="w-min">&#x2192;</div>
            </div>
        </button>
    </div>
    <code class="text-xs opacity-70 pt-2 text-center"
        >Use Arrow keys to navigate,<br />Enter to return today's date</code
    >
</div>
