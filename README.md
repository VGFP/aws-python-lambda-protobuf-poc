# AWS python lambda Protocol Buffer PoC

This is a proof of concept for using Protocol Buffers with AWS Lambda and Python.

Project was created using terraform

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
  pip install -r requirements.txt --target ./python/get_protobuf_data
  ```

- Deploy lambdas
```bash
  terraform apply
  ```