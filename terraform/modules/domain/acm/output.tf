output "cert_resource_record_name" {
  value = tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_name
}

output "cert_resource_record_type" {
  value = tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_type
}

output "cert_resource_record_value" {
  value = tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_value
}

output "aws_acm_certificate_arn" {
  value = aws_acm_certificate.cert.arn
}
