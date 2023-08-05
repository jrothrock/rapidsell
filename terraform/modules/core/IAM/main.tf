resource "aws_iam_role" "chalice_role" {
  name = "chalice_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "chalice_policy" {
  name = "chalice_policy"
  role = aws_iam_role.chalice_role.id


  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
				  "logs:CreateLogStream",
				  "logs:PutLogEvents"
        ]
        Effect   = "Allow"
        Resource = "arn:*:logs:*:*:*"
      },
      {
        Action  = [
          "s3:PutObject"
        ]
        Effect  = "Allow"
        Resource = ["arn:aws:s3:::rapidsell-scanning-photos/*"]
      }
    ]
  })
}