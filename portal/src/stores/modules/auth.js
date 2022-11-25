import { apiService } from "@/api";

const namespaced = true;

const state = {
    user:{},
    isLoggedIn: false
}

const getters = {
    isLoggedIn: state => state.isLoggedIn,
    user: state => state.user
};

const actions = {
    async loginUser({dispatch}, user){
        await apiService.post('api/auth/login_jwt', user)
        await dispatch('fetchUser')
        // alert('logined')
    },
    async fetchUser({commit}){
        await apiService.get('api/auth/user_jwt')
            .then(({data}) => commit('setUser', data))
    },
    async logoutUser({commit}){
        await apiService.get('api/auth/logout_jwt');
        commit('logoutUserState')
        // alert('logout')
    }
};

const mutations = {
    setUser(state, user){
        state.isLoggedIn = true;
        state.user = user;
    },
    logoutUserState(state){
        state.isLoggedIn = false;
        state.user = {}
    }
}

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations
}