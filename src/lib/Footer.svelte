<script lang="ts">
</script>

<footer
    class="font-display bg-dark0 shadow-xl shadow-accent1/5 w-full h-10 lg:rounded-2xl box-shadow flex justify-center items-center font-medium mt-auto lg:my-4 rounded-none transition-all duration-300"
>
    <div class="flex w-full justify-around items-center sm:mx-8 mx-4 text-fg relative">
        <!-- VERSION TEXT -->
        <code class="text-sm text-slate-500 min-w-fit sm:flex hidden justify-center">v</code>

        <!-- COPYRIGHT TEXT -->
        <div class="flex justify-around w-full min-w-fit">
            <div
                class="after:absolute after:inset-0 after:-z-10 after:blur-[1000px] after:bg-accent1 after:-translate-y-10 after:rounded-full  after:h-[80px] after:w-72 after:left-1/2 after:-translate-x-1/2"
            >
                Copyright &copy; <span id="copyrightYear">{new Date().getFullYear()}</span>
                <a
                    target="_blank"
                    href="https://test2user-aqil.github.io/"
                    class="font-mono tracking-tight text-accent1hover hover:brightness-125 duration-300"
                    >test2user-aqil</a
                >
            </div>
        </div>

        <!-- GITHUB LINK -->
        <a
            href="https://github.com/test2user-aqil/weatherdatacollector_baku"
            target="_blank"
            class="opacity-90 font-mono tracking-tight text-sm text-accent1hover hover:brightness-125 duration-300 min-w-fit sm:flex hidden"
            >View on Github</a
        >
        <div />
    </div>
</footer>
