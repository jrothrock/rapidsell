import axios from 'axios';
import type { Router } from 'vue-router';
import type { SignUpRequest, SignUpResponse } from "@/api/users/SignUp";

const SIGN_UP_URL = "https://api.rapidsell.io/users/sign_up";

async function signUp(params: SignUpRequest, router: Router) {
  const response = await axios.post(SIGN_UP_URL, params);
  const data: SignUpResponse = response.data;
  if(data.success) {
    router.push({name: "SignUpConfirm", params:{email: params.email}})
  }
}

export function useSignUp() {
  return {
    signUp: (params: SignUpRequest, router: Router) => signUp(params, router)
  }
}
