# Sets up information related to the domain. Route53, ACM, etc.
module "domain" {
  source = "./modules/domain"

  domain_name = var.domain_name
}

# Sets up services related to users. Cognito, SES, and a bucket for the users
module "users" {
  source = "./modules/users"

  app_name = var.app_name
  domain_name = var.domain_name
}
