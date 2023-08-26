module "aws_iam" {
  source = "./IAM"

  scanning_table_arn = var.scanning_table_arn
}
