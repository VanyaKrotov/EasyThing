import Vue from "vue";
import Vuex from "vuex";
import user from "./models/user";
import company from "./models/company";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    company,
  },
});
