import { createApp } from "vue";
import { createPinia } from "pinia";
import store from "@/stores";

import App from "./App.vue";
// import App_2 from "./App_2.vue"
import router from "./router";

// import "./assets/main.css";
import "bootstrap/dist/js/bootstrap"

import 'bootstrap/dist/css/bootstrap.css'

const app = createApp(App);
app.use(createPinia());
app.use(store)

app.use(router);

app.mount("#app");
