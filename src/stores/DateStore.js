import { writable } from "svelte/store";

export function todaysDate() {
    let today = new Date();

    let day = today.getDate().toString();
    if (day.length == 1) {
        day = "0" + day;
    }

    let month = (today.getMonth() + 1).toString();
    if (month.length == 1) {
        month = "0" + month;
    }

    let year = today.getFullYear().toString();

    let date = year + "-" + month + "-" + day;
    return date;
}

let date = todaysDate();

export const DateStore = writable(date);
