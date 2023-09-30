resource "aws_dynamodb_table" "scanning_table" {
  name           = "Scanning"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "pk"
  range_key      = "sk"

  attribute {
    name = "pk"
    type = "S"
  }

  attribute {
    name = "sk"
    type = "S"
  }

  ttl {
    attribute_name = "ttl"
    enabled        = true
  }

  global_secondary_index {
    name               = "InvertedIndex"
    hash_key           = "sk"
    range_key          = "pk"
    projection_type    = "ALL"
  }
}
