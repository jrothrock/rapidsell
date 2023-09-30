###
# Core
###
output "chalice_role_arn" {
  value = module.core.chalice_role_arn
}

###
# Scanning
###
output "scanning_bucket_name" {
  value = module.scanning.scanning_bucket_name
}

output "scanning_table_name" {
  value = module.scanning.scanning_table_name
}

output "scanning_table_arn" {
  value = module.scanning.scanning_table_arn
}

###
# Users
###

output "cognito_client_id" {
  value = module.users.cognito_client_id
}

output "cognito_pool_arn" {
  value = module.users.cognito_pool_arn
}

