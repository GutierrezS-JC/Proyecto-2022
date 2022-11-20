import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import App_2 from "./App_2.vue"
import router from "./router";

// import "./assets/main.css";
import "bootstrap/dist/js/bootstrap"

import 'bootstrap/dist/css/bootstrap.css'

const app = createApp(App_2);
app.use(createPinia());

app.use(router);

app.mount("#app");
