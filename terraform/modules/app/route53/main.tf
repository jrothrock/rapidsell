resource "aws_route53_record" "root_domain" {
  zone_id = "${var.main_route53_zone_id}"
  name = "${var.app_subdomain}"
  type = "A"

  alias {
    name = "${var.cloudfront_domain_name}"
    zone_id = "${var.cloudfront_zone_id}"
    evaluate_target_health = false
  }
}
