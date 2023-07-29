# Sets up information related to the domain. Route53, ACM, etc.
module "domain" {
  source = "./modules/domain"

  domain_name = var.domain_name
  api_subdomain = var.api_subdomain
}

# Sets up services related to users. Cognito, SES, and a bucket for the users
module "users" {
  source = "./modules/users"

  app_name = var.app_name
  domain_name = var.domain_name
}

# Write certificate and api_domain_name to chalice for API gateway creation.
resource "local_file" "private_key" {
    content = templatefile("${path.module}/../backend/.chalice/config.json.tpl",
      {
        api_domain_name = var.api_subdomain
        certificate_arn = module.domain.aws_acm_certificate_arn
      }
    )

    filename  = "${path.module}/../backend/.chalice/config.json"
}

module "app" {
  source = "./modules/app"

  app_name = var.app_name
  app_subdomain = var.app_subdomain
  main_route53_zone_id = module.domain.main_route53_zone_id
  certificate_arn = module.domain.aws_acm_certificate_arn
}
