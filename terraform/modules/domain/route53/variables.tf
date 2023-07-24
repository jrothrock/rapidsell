variable "domain_name" {
  type = string
  description = "Domain of the app."
}

variable "cert_resource_record_name" {
  type = string
  description = "The cert resource record name."
}

variable "cert_resource_record_type" {
  type = string
  description = "The cert resource record type."
}

variable "cert_resource_record_value" {
  type = string
  description = "The cert resource record value."
}
