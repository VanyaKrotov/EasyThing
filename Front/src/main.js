import Vue from 'vue';
import App from './App.vue';
import store from './store';
import ElementUI from 'element-ui';
import router from './router';
import Router from 'vue-router';
import Vue2Editor from 'vue2-editor';
import YmapPlugin from 'vue-yandex-maps';

import lang from 'element-ui/lib/locale/lang/en';
import locale from 'element-ui/lib/locale';

import 'element-ui/lib/theme-chalk/index.css';
import './styles/index.css';

Vue.config.productionTip = false;

const settings = {
  apiKey: '6eae48fe-cd83-408a-a2e5-c11bb62da1cf',
  lang: 'ru_RU',
  coordorder: 'latlong'
};

locale.use(lang);

Vue.use(ElementUI);
Vue.use(Router);
Vue.use(Vue2Editor);
Vue.use(YmapPlugin, settings);

new Vue({
  store,
  router,
  render: (h) => h(App),
  beforeCreate() {
    // init requests

    store.dispatch('authUser');
    store.dispatch('fetchAllServiceTypes');
    store.dispatch('fetchWorkShedudles');
  }
}).$mount('#app');
