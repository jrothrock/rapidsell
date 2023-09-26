import { createRouter, createWebHistory } from '@ionic/vue-router';
import { useAuthStore } from '@/stores';
import ScanningView from '../views/Scanning/ScanningView.vue';

const BASE_URL = "/";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ScanningView
  },
  {
    path: '/scanning',
    name: 'Scanning',
    component: () => import('../views/Scanning/ScanningView.vue')
  },
  {
    path: '/scanning/new',
    name: 'ScanningNew',
    component: () => import('../views/Scanning/New/NewScanningView.vue')
  },
  {
    path: '/sign_in',
    name: 'SignIn',
    component: () => import('../views/SignIn/SignInView.vue')
  },
  {
    path: '/sign_up',
    name: 'SignUp',
    component: () => import('../views/SignUp/SignUpView.vue')
  },
  {
    path: '/sign_up/confirm/:email',
    name: 'SignUpConfirm',
    component: () => import('../views/SignUp/SignUpConfirm/SignUpConfirmView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(BASE_URL),
  routes,
});

// route guards
router.beforeEach((to, _, next) => {
  const to_name = to.name;

  if(to_name != "SignUpConfirm" && to_name != "SignUp" && to_name != "SignIn")  {
    const store = useAuthStore();

    if(!store.isLoggedIn) {
      next("/sign_in");
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;