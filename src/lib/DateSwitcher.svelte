<script>
    let date;

    $: console.log(date);
</script>

<input
    type="date"
    name=""
    id=""
    class="bg-dark0 border-4 border-fg text-fg h-16 py-5 px-14 rounded-full font-mono flex items-center justify-center"
    bind:value={date}
/>
