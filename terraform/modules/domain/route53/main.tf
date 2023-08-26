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

resource "aws_route53_record" "api" {
  name = var.api_subdomain
  type = "CNAME"
  zone_id = aws_route53_zone.main.zone_id
  records = ["${jsondecode(file("${path.root}/../backend/.chalice/deployed/dev.json"))["resources"][4]["alias_domain_name"]}"]
  count = fileexists("${path.root}/../backend/.chalice/deployed/dev.json") ? 1 : 0
  ttl  = 60
}
