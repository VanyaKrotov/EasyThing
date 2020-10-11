import Vue from 'vue';
import Vuex from 'vuex';
import user from './models/user';
import company from './models/company';
import service from './models/service';
import serviceType from './models/serviceType';
import workShedudle from './models/workShedudle';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    company,
    service,
    serviceType,
    workShedudle
  }
});
