output "domain_name_servers" {
  value = module.aws_route53.domain_name_servers
}

output "aws_acm_certificate_arn" {
  value = module.aws_acm.aws_acm_certificate_arn
}
