import { createStore } from "vuex";
import auth from "@/stores/modules/auth";

const store = createStore({
    modules: {
        auth: auth
    }
})

export default store;