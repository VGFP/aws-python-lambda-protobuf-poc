# AWS python lambda Protocol Buffer PoC

This is a proof of concept for using Protocol Buffers with AWS Lambda and Python.

Project was created using terraform

## Description
AWS Python lambda is transforming JSON encoded event to python variable. So using Protocol Buffers is not needed. But SQS MessageBody is a String so Protocol Buffers can be used to improve data serialization and deserialization (more info: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html). This project is using Protocol Buffers to send data from lambda to lambda using SQS. 

From testing bouth methods have similar execution time around 1ms. But more complex data structures can be more efficient with Protocol Buffers (needs more testing).

## Prerequisites

- Terraform with aws credentials
- Python3

## Setup

- Create a virtualenv 
```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Init terraform
```bash
  cd terraform
  terraform init
  ```

- Install python dependencies
```bash
  pip install -r ./terraform/python/get_protobuf_data/requirements.txt --target ./terraform/python/get_protobuf_data
  pip install -r ./terraform/python/get_protobuf_data/requirements.txt --target ./terraform/python/send_protobuf_data
  ```

- Deploy lambdas
```bash
  terraform apply
  ```