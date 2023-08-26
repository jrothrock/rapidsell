output "scanning_table_name" {
  value = aws_dynamodb_table.scanning_table.id
}

output "scanning_table_arn" {
  value = aws_dynamodb_table.scanning_table.arn
}
