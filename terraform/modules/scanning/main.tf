module "aws_s3" {
  source = "./s3"

  app_name = var.app_name
}
