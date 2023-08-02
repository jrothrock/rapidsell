resource "aws_s3_bucket" "scanning_bucket" {
  bucket = "${var.app_name}-scanning-photos"
}
