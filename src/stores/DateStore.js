import { writable } from "svelte/store";

let today = new Date();

let day = today.getDay().toString();
if (day.length == 1) {
    day = "0" + day;
}

let month = today.getMonth().toString();
if (month.length == 1) {
    month = "0" + month;
}

let year = today.getFullYear().toString();

let date = year + "-" + month + "-" + day;

export const DateStore = writable(date);
