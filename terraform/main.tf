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
  cognito_pool_name = var.cognito_pool_name
}

module "app" {
  source = "./modules/app"

  app_name = var.app_name
  app_subdomain = var.app_subdomain
  main_route53_zone_id = module.domain.main_route53_zone_id
  certificate_arn = module.domain.aws_acm_certificate_arn
}

module "scanning" {
  source = "./modules/scanning"

  app_name = var.app_name
}

module "core" {
  source = "./modules/core"

  scanning_table_arn = module.scanning.scanning_table_arn
}
# Write certificate and api_domain_name to chalice for API gateway creation.
resource "local_file" "private_key" {
    content = templatefile("${path.module}/../backend/.chalice/config.json.tpl",
      {
        app_subdomain = var.app_subdomain
        api_domain_name = var.api_subdomain
        chalice_iam_role_arn = module.core.chalice_role_arn
        certificate_arn = module.domain.aws_acm_certificate_arn
        cognito_client_id = module.users.cognito_client_id
        cognito_pool_name = var.cognito_pool_name
        cognito_pool_arn = module.users.cognito_pool_arn
        scanning_bucket_name = module.scanning.scanning_bucket_name
        scanning_table_name = module.scanning.scanning_table_name
        serp_api_key  = var.serp_api_key
      }
    )

    filename  = "${path.module}/../backend/.chalice/config.json"
}
