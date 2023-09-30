output "scanning_bucket_name" {
  value = module.aws_s3.scanning_bucket_name
}

output "scanning_table_name" {
  value = module.aws_dynamo.scanning_table_name
}

output "scanning_table_arn" {
  value = module.aws_dynamo.scanning_table_arn
}
