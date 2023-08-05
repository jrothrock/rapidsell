{
  "version": "2.0",
  "app_name": "backend",
  "stages": {
    "dev": {
      "api_gateway_stage": "api",
      "api_gateway_custom_domain": {
        "domain_name": "${api_domain_name}",
        "tls_version": "TLS_1_2|TLS_1_0",
        "certificate_arn": "${certificate_arn}"
      },
      "manage_iam_role": false,
      "iam_role_arn": "${chalice_iam_role_arn}",
      "environment_variables": {
        "APP_SUBDOMAIN": "${app_subdomain}",
        "AWS_COGNITO_CLIENT_ID": "${cognito_client_id}",
        "AWS_COGNITO_POOL_NAME": "${cognito_pool_name}",
        "AWS_COGNITO_POOL_ARN": "${cognito_pool_arn}",
        "AWS_SCANNING_BUCKET_NAME": "${scanning_bucket_name}"
      }
    }
  }
}
