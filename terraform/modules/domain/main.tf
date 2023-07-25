module "aws_acm" {
  source = "./acm"

  domain_name = var.domain_name
}

module "aws_route53" {
  source = "./route53"

  domain_name = var.domain_name
  api_subdomain = var.api_subdomain
  
  cert_resource_record_name = module.aws_acm.cert_resource_record_name
  cert_resource_record_type = module.aws_acm.cert_resource_record_type
  cert_resource_record_value = module.aws_acm.cert_resource_record_value
}
