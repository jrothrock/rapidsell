variable "app_name" {
  type = string
  description = "Name of the app."
}

variable "domain_name" {
  type = string
  description = "Domain for the site."
}

variable "api_subdomain" {
  type = string
  description = "Subdomain of the API."
}

variable "app_subdomain" {
  type = string
  description = "Subdomain of the app."
}

variable "cognito_pool_name" {
  type = string
  description = "Name for the cognito pool."
}

variable "serp_api_key" {
  type = string
  description = "API key for serpapi."
  sensitive = true
}
