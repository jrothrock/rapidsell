resource "aws_api_gateway_domain_name" "domain_name" {
  domain_name = var.domain_name

  certificate_arn = var.aws_acm_certificate_arn
}
