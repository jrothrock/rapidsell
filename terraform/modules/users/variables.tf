variable "app_name" {
  type = string
  description = "Name of the app."
}

variable "domain_name" {
  type = string
  description = "Domain of the app."
}

variable "cognito_pool_name" {
  type = string
  description = "Name for the cognito pool."
}
