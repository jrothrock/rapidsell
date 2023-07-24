resource "aws_route53_zone" "main" {
  name     = var.domain_name
}

resource "aws_route53_record" "cert_validation" {
  name    = var.cert_resource_record_name
  type    = var.cert_resource_record_type
  zone_id = aws_route53_zone.main.zone_id
  records = ["${var.cert_resource_record_value}"]
  ttl     = 60
}
