variable "app_name" {
  type = string
  description = "Name of the app."
}

variable "app_subdomain" {
  type = string

  description = "The subdomain for the app."
}

variable "main_route53_zone_id" {
  type = string

  description = "The id for the main route53 zone."
}

variable "certificate_arn" {
  type = string

  description = "The id arn for the certificate."
}
