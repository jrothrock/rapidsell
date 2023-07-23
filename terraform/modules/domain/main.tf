module "aws_route53" {
  source = "./route53"

  domain_name = var.domain_name
}
