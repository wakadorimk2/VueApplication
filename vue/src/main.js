import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import scrollloader from 'vue-scroll-loader';
import App from './App.vue';
import router from './router';
import vuetify from '@/plugins/vuetify';
import '@babel/polyfill';

Vue.config.productionTip = false;
Vue.use(scrollloader);

new Vue({
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app');
