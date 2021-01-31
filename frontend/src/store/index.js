import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    access: localStorage.getItem("accessToken"),
    refresh: localStorage.getItem("refreshToken"),
  },
  mutations: {
    setTokens(state, tokens) {
      state.access = tokens.access;
      state.refresh = tokens.refresh;
      if (state.access === null ){
        localStorage.removeItem("accessToken");
      } else {
        localStorage.setItem("accessToken", state.access);
      }
      if (state.refresh === null ){
        localStorage.removeItem("refreshToken");
      } else {
        localStorage.setItem("refreshToken", state.refresh);
      }
    },
  },
  actions: {
    login(context, tokens) {
      context.commit("setTokens", tokens);
    },
    logout(context) {
      context.commit("setTokens", {access: null, refresh: null});
    }
  },
  modules: {
  }
})
