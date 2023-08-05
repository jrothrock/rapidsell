export type SignInRequest = {
  email: string
  password: string
}

export type SignInResponse = {
  access_token: string
  id_token: string
}
