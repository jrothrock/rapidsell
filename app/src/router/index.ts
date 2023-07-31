import { createRouter, createWebHistory } from '@ionic/vue-router';
import Home from '../views/Home/Home.vue';

const BASE_URL = "/";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign_in',
    name: 'SignIn',
    component: () => import('../views/SignIn/SignIn.vue')
  },
  {
    path: '/sign_up',
    name: 'SignUp',
    component: () => import('../views/SignUp/SignUp.vue')
  },
  {
    path: '/sign_up/confirm/:email',
    name: 'SignUpConfirm',
    component: () => import('../views/SignUp/SignUpConfirm/SignUpConfirm.vue')
  }
]

const router = createRouter({
  history: createWebHistory(BASE_URL),
  routes,
});

// route guards
router.beforeEach((to, _, next) => {
  const has_access_token = localStorage.getItem('access_token');
  const to_name = to.name;

  if(to_name != "SignUpConfirm" && to_name != "SignUp" && to_name != "SignIn")  {
    if(!has_access_token) {
      next("/sign_in")
    } else {
      next();
    }
  } else {
    next();
  }
})

export default router;