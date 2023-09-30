output "emails_bucket_id" {
  value = aws_s3_bucket.emails_bucket.id
}

output "bucket_policy_created" {
  value = {}

  depends_on = [aws_s3_bucket_policy.bucket_policy]
}