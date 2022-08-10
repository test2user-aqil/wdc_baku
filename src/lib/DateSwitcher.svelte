<script>
    import { DateStore } from "../stores/DateStore";
</script>

<input
    type="date"
    name="dateSwitcher"
    id="dateSwitcher"
    class="cursor-pointer bg-dark0 border-4 border-fg text-fg h-16 py-4 px-12 rounded-full font-mono flex items-center justify-center outline-0"
    bind:value={$DateStore}
/>
