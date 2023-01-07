terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-north-1"
}

data "archive_file" "zip_protobuf_data_code" {
  type        = "zip"
  source_dir  = "python/get_protobuf_data"
  output_path = ".python/get_protobuf_data/get_protobuf_data.zip"
}

resource "aws_lambda_function" "get_protobuf_data" {
  function_name    = "get_protobuf_data"
  role             = aws_iam_role.lambda_role.arn
  handler          = "get_protobuf_data.lambda_handler"
  runtime          = "python3.9"
  filename         = ".python/get_protobuf_data/get_protobuf_data.zip"
  source_code_hash = filebase64sha256(".python/get_protobuf_data/get_protobuf_data.zip")
  publish          = true
  architectures    = ["arm64"]
}

data "archive_file" "zip_json_data_code" {
  type        = "zip"
  source_dir  = "python/get_json_data"
  output_path = ".python/get_json_data/get_json_data.zip"
}

resource "aws_lambda_function" "get_json_data" {
  function_name    = "get_json_data"
  role             = aws_iam_role.lambda_role.arn
  handler          = "get_json_data.lambda_handler"
  runtime          = "python3.9"
  filename         = ".python/get_json_data/get_json_data.zip"
  source_code_hash = filebase64sha256(".python/get_json_data/get_json_data.zip")
  publish          = true
  architectures    = ["arm64"]
}

resource "aws_iam_role" "lambda_role" {
  name               = "basic-lambda-function-role"
  assume_role_policy = <<EOF
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": "sts:AssumeRole",
          "Principal": {
            "Service": "lambda.amazonaws.com"
          },
          "Effect": "Allow",
          "Sid": ""
        }
      ]
    }
  EOF
}

resource "aws_iam_role_policy" "lambda_role_policy" {
  name   = "basic-lambda-function-role-policy"
  role   = aws_iam_role.lambda_role.id
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}
EOF
}

