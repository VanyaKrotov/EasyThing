import Vue from "vue";
import Vuex from "vuex";
import user from "./models/user";
import company from "./models/company";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isLoading: true,
  },
  mutations: {
    setStatusLoading(state, status) {
      state.isLoading = status;
    },
  },
  getters: {
    statusLoading(state) {
      return state.isLoading;
    },
  },
  modules: {
    user,
    company,
  },
});
