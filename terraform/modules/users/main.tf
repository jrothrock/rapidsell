module "aws_cognito" {
  source = "./cognito"

  app_name = var.app_name
  cognito_pool_name = var.cognito_pool_name
}

module "aws_s3" {
  source = "./s3"

  app_name = var.app_name
}

module "aws_ses" {
  source = "./ses"

  domain_name = var.domain_name
  emails_bucket_id = module.aws_s3.emails_bucket_id
  bucket_policy_dependency = module.aws_s3.bucket_policy_created

  depends_on = [module.aws_s3]
}
