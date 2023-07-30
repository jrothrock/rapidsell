output "domain_name_servers" {
  value = module.domain.domain_name_servers
}

output "cognito_client_id" {
  value = module.users.cognito_client_id
}
