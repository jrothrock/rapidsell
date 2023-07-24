module "aws_acm" {
  source = "./acm"

  domain_name = var.domain_name
}

module "aws_route53" {
  source = "./route53"

  domain_name = var.domain_name
  
  cert_resource_record_name = module.aws_acm.cert_resource_record_name
  cert_resource_record_type = module.aws_acm.cert_resource_record_type
  cert_resource_record_value = module.aws_acm.cert_resource_record_value
}

module "aws_api_gateway" {
  source = "./api_gateway"

  domain_name = var.domain_name

  aws_acm_certificate_arn = module.aws_acm.aws_acm_certificate_arn
}