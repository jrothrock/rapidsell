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
      "environment_variables": {
        "AWS_COGNITO_CLIENT_ID": "${cognito_client_id}"
      }
    }
  }
}
