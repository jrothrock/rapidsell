# Sets up information related to the domain. Route53, ACM, etc.
module "domain" {
  source = "./modules/domain"

  domain_name = var.domain_name
  api_subdomain = var.api_subdomain
}

# Contains various modules for setting up services related to backend.
module "backend" {
  source = "./modules/backend"

  app_name = var.app_name
  domain_name = var.domain_name
  cognito_pool_name = var.cognito_pool_name
}

# Sets up services related to Vue app. Cloudfront, s3, route53, etc.
module "app" {
  source = "./modules/app"

  app_name = var.app_name
  app_subdomain = var.app_subdomain
  main_route53_zone_id = module.domain.main_route53_zone_id
  certificate_arn = module.domain.aws_acm_certificate_arn
}

# Write certificate and api_domain_name to chalice for API gateway creation.
resource "local_file" "private_key" {
    content = templatefile("${path.module}/../backend/.chalice/config.json.tpl",
      {
        app_subdomain = var.app_subdomain
        api_domain_name = var.api_subdomain
        chalice_iam_role_arn = module.backend.chalice_role_arn
        certificate_arn = module.domain.aws_acm_certificate_arn
        cognito_client_id = module.backend.cognito_client_id
        cognito_pool_name = var.cognito_pool_name
        cognito_pool_arn = module.backend.cognito_pool_arn
        scanning_bucket_name = module.backend.scanning_bucket_name
        scanning_table_name = module.backend.scanning_table_name
        serp_api_key  = var.serp_api_key
      }
    )

    filename  = "${path.module}/../backend/.chalice/config.json"
}
