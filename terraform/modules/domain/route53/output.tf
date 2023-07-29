output "domain_name_servers" {
  value = aws_route53_zone.main.name_servers
}

output "main_route53_zone_id" {
  value = aws_route53_zone.main.zone_id
}
