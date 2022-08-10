<script>
    import { DateStore } from "../stores/DateStore";
</script>

<input
    type="date"
    name="dateSwitcher"
    id="dateSwitcher"
    class="cursor-pointer bg-dark0 border-4 border-fg text-fg h-16 py-4 px-12 rounded-full font-mono focus:outline-none outline-none shadow-xl shadow-accent1/5 hover:shadow-accent1/20 hover:text-accent1hover hover:border-accent1hover transition-all duration-300 hover:brightness-110"
    bind:value={$DateStore}
/>
