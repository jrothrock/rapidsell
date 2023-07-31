import axios from 'axios';
import type { Router } from 'vue-router';
import type { SignInRequest, SignInResponse } from "@/api/users/SignIn";

const SIGN_UP_CONFIRM_URL = "https://api.rapidsell.io/users/sign_in";

async function signIn(params: SignInRequest, router: Router) {
  const response = await axios.post(SIGN_UP_CONFIRM_URL, params);
  const data: SignInResponse = response.data;
  if(data.access_token) {
    localStorage.setItem("access_token", data.access_token);
    router.push({name: "Home"})
  }
}

export function useSignIn() {
  return {
    signIn: (params: SignInRequest, router: Router) => signIn(params, router)
  }
}