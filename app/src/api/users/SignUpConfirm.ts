export type SignUpConfirmRequest = {
  email: string;
  confirmation_code: string;
}

export type SignUpConfirmResponse = {
  success: boolean;
}
