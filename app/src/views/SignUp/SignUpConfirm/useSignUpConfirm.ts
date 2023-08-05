import axios from 'axios';
import type { Router } from 'vue-router';
import type { SignUpConfirmRequest, SignUpConfirmResponse } from "@/api/users/SignUpConfirm";

const SIGN_UP_CONFIRM_URL = `${import.meta.env.VITE_BASE_URL}/users/sign_up/confirm`;

async function signUpConfirm(params: SignUpConfirmRequest, router: Router) {
  const response = await axios.post(SIGN_UP_CONFIRM_URL, params);
  const data: SignUpConfirmResponse = response.data;
  if(data.success) {
    router.push({name: "SignIn"});
  }
}

export function useSignUpConfirm() {
  return {
    signUpConfirm: (params: SignUpConfirmRequest, router: Router) => signUpConfirm(params, router)
  }
}