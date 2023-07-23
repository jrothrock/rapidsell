variable "domain_name" {
  type = string
  description = "Domain of the app."
}

variable "emails_bucket_id" {
  type = string
  description = "ID of the emails bucket"
}

variable "bucket_policy_dependency" {
  type = any
  description = "This value is not used. Used for propogating dependency."
}
