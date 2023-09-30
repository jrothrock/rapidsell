# Sets up services related to scanning. Dynamo, buckets, etc.
module "scanning" {
  source = "./scanning"

  app_name = var.app_name
}

# Set up some of the core stuff on the backend, such as the lambda's assummed
# role policy.
module "core" {
  source = "./core"

  scanning_table_arn = module.scanning.scanning_table_arn
}

# Sets up services related to users. Cognito, SES, and a bucket for the users
module "users" {
  source = "./users"

  app_name = var.app_name
  domain_name = var.domain_name
  cognito_pool_name = var.cognito_pool_name
}