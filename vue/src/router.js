import Vue from 'vue';
import Router from 'vue-router';
import Viewer from './components/Viewer.vue';
import TestComponents from './components/TestComponents.vue';

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
      path: '/test',
      name: 'TestComponents',
      component: TestComponents,
    },
  ],
});
