resource "aws_s3_bucket" "emails_bucket" {
  bucket = "${var.app_name}-emails-bucket"
}

resource "null_resource" "delay" {
  provisioner "local-exec" {
    command = "sleep 10"
  }
  triggers = {
    "after" = aws_s3_bucket.emails_bucket.id
  }
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = "${aws_s3_bucket.emails_bucket.id}"

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSESPuts",
            "Effect": "Allow",
            "Principal": {
                "Service": "ses.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::${var.app_name}-emails-bucket/*"
        }
    ]
}
POLICY
  depends_on = [
    null_resource.delay
  ]
}
