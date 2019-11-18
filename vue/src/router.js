import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Viewer from './components/Viewer.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Viewer',
      component: Viewer,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
