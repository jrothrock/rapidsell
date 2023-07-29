module "aws_app_bucket" {
  source = "./s3"

  app_subdomain = var.app_subdomain
}

module "aws_cloudfront" {
  source = "./cloudfront"

  app_bucket_regional_domain_name = module.aws_app_bucket.app_bucket_regional_domain_name
  certificate_arn = var.certificate_arn
}

module "aws_route53" {
  source = "./route53"

  app_subdomain = var.app_subdomain
  main_route53_zone_id = var.main_route53_zone_id

  cloudfront_domain_name = module.aws_cloudfront.cloudfront_domain_name
  cloudfront_zone_id = module.aws_cloudfront.cloudfront_zone_id
}
