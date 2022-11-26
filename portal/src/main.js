import { createApp } from "vue";
import { createPinia } from "pinia";
import store from "@/stores";

import App from "./App.vue";
import router from "./router";

import "bootstrap/dist/js/bootstrap"

import 'bootstrap/dist/css/bootstrap.css'

const app = createApp(App);
app.use(createPinia());
app.use(store)

app.use(router);

app.mount("#app");
