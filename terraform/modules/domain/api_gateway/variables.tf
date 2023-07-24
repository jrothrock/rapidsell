variable "domain_name" {
  type = string
  description = "Domain of the app."
}

variable "aws_acm_certificate_arn" {
  type = string
  description = "ARN of the acm certificate."
}
