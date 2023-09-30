resource "aws_s3_bucket" "scanning_bucket" {
  bucket = "${var.app_name}-scanning-photos"
}

resource "aws_s3_bucket_cors_configuration" "scanning_bucket_cors" {
  bucket = aws_s3_bucket.scanning_bucket.id

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["PUT", "POST"]
    allowed_origins = ["*"]
    expose_headers  = ["ETag"]
    max_age_seconds = 3000
  }
}
