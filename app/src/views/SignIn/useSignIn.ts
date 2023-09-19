import axios from 'axios';
import { useAuthStore } from '@/stores';
import type { Router } from 'vue-router';
import type { SignInRequest, SignInResponse } from "@/api/users/SignIn";

const SIGN_UP_CONFIRM_URL = `${import.meta.env.VITE_BASE_URL}/users/sign_in`;

async function signIn(params: SignInRequest, router: Router) {
  const response = await axios.post(SIGN_UP_CONFIRM_URL, params);
  const data: SignInResponse = response.data;
  if(data.access_token) {
    const store = useAuthStore();
    store.loginUser(data.access_token, data.id_token);
    router.push({name: "Home"});
  }
}

export function useSignIn() {
  return {
    signIn: (params: SignInRequest, router: Router) => signIn(params, router)
  };
}