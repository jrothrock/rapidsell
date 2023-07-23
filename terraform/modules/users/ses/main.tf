resource "aws_ses_domain_identity" "domain" {
  domain = var.domain_name
}

resource "aws_ses_domain_dkim" "domain_dkim" {
  domain = "${aws_ses_domain_identity.domain.domain}"
}

resource "aws_ses_receipt_rule_set" "main" {
  rule_set_name = "default-rule-set"
}

resource "aws_ses_receipt_rule" "store" {
  name          = "store"
  rule_set_name = "default-rule-set"
  enabled       = true
  scan_enabled  = true

  add_header_action {
    header_name  = "Custom-Header"
    header_value = "Added by SES"
    position     = 1
  }

  s3_action {
    bucket_name = var.emails_bucket_id
    object_key_prefix = "incoming"
    position    = 2
  }

  depends_on = [
    aws_ses_receipt_rule_set.main
  ]
}