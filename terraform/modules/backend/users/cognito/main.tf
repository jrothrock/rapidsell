resource "aws_cognito_user_pool" "user_pool" {
  name = var.cognito_pool_name

  username_attributes = ["email"]
  auto_verified_attributes = ["email"]
  password_policy {
    temporary_password_validity_days = 7
    minimum_length = 8
  }

  verification_message_template {
    default_email_option = "CONFIRM_WITH_CODE"
    email_subject = "Account Confirmation"
    email_message = "Your confirmation code is {####}"
  }

  schema {
    attribute_data_type      = "String"
    developer_only_attribute = false
    mutable                  = true
    name                     = "email"
    required                 = true

    string_attribute_constraints {
      min_length = 1
      max_length = 256
    }
  }
}

resource "aws_cognito_user_pool_client" "client" {
  name = "cognito-client"

  user_pool_id = aws_cognito_user_pool.user_pool.id
  generate_secret = false
  refresh_token_validity = 90
  prevent_user_existence_errors = "ENABLED"
  explicit_auth_flows = [
    "ALLOW_REFRESH_TOKEN_AUTH",
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_ADMIN_USER_PASSWORD_AUTH"
  ]
  
}

resource "aws_cognito_user_pool_domain" "cognito-domain" {
  domain       = var.app_name
  user_pool_id = "${aws_cognito_user_pool.user_pool.id}"
}
