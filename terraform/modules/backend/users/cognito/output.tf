output "cognito_client_id" {
  value = aws_cognito_user_pool_client.client.id
}

output "cognito_pool_arn" {
  value = aws_cognito_user_pool.user_pool.arn
}
