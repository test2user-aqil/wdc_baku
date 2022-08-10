/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: "jit",
    content: ["./index.html", "./src/**/*.{svelte,vue,js,ts,jsx,tsx}"],
    theme: {
        extend: {
            colors: {
                bg: "#1a1a24",
                fg: "#ced6ff",
                dark0: "#0f0f19",
                accent1: "#0085ff",
                accent1hover: "#6cb7fc",
            },
        },
    },
    plugins: [],
};
