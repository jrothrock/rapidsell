variable "app_subdomain" {
  type = string

  description = "The subdomain for the app."
}

variable "main_route53_zone_id" {
  type = string

  description = "The id for the main route53 zone."
}

variable "cloudfront_domain_name" {
  type = string

  description = "The domain name of the cloudfront instance."
}

variable "cloudfront_zone_id" {
  type = string

  description = "The zone id of the cloudfront instance."
}
