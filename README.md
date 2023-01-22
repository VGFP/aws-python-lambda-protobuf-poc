# AWS python lambda Protocol Buffer PoC

This is a proof of concept for using Protocol Buffers with AWS Lambda and Python.

Project is using terraform for infrastructure deployment

## Description
AWS Python lambda is transforming JSON encoded event to python variable at runtime. So using Protocol Buffers is not needed. But SQS MessageBody is a String so Protocol Buffers can be used to improve data serialization and deserialization (more info: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html). This project is using Protocol Buffers to send data from lambda to lambda using SQS. 

From testing both methods have similar execution time around 1ms. But more complex data structures can be more efficient with Protocol Buffers (needs more testing).

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

## AWS Preformance testing table
Preformance from AWS testing for small and large data structures. I run request for both JSON and Protocol Buffers on my personal aws account. Here are results for small massage (main branch) and large massage (large-message-almbda-sqs-test branch).

> I did not run this test a lot of times (due to monetary costs) so your results can be a bit different. But I think it is enough to show the difference between JSON and Protocol Buffers.

Lambdas settings:
- Region: eu-north-1
- Python version: 3.9
- Architecture: ARM64
- Memory: 128 MB

### Small message (main branch)
| Lambda | Duration [ms] | Billed Duration [ms] | Max Memory Used [MB] | Init Duration [ms] |
| --- | --- | --- | --- | --- |
| get_protobuf_data | 1.08 | 2 | 44 | 203.94 |
| send_protobuf_data | 951.89 | 952 | 69 | 322.5 |
| get_json_data | 1.17 | 2 | 35 | 91.94 |
| send_json_data | 992.33 | 993 | 64 | 214.27 |

### Large message (large-message-almbda-sqs-test branch)
| Lambda | Duration [ms] | Billed Duration [ms] | Max Memory Used [MB] | Init Duration [ms] |
| --- | --- | --- | --- | --- |
| get_protobuf_data | 1.17 | 2 | 44 | 205.79 |
| send_protobuf_data | 959.46 | 960 | 69 | 323.21 |
| get_json_data | 14.87 | 15 | 36 | 95.36 |
| send_json_data | 1079.35 | 1080 | 64 | 219.34 |

### Results analysis
* For smaller messages there is no significant difference between JSON and Protocol Buffers. Duration in protobuf is a bit better (lower) but it is not significant.
* Cold start will be a bit longer for Protocol Buffers because of additional dependencies. But for lambdas running constantly it is not a problem.
* For sending lambdas takes a lot of time more than for getting the data. Difference is most likely because of *'cold start'* of SQS. If you run this test multiple times you will see that sending lambdas will be faster (around 204ms for protobuf and 250ms for json in billed time for small mesages). 
* For large messages Protocol Buffers is better than JSON. Implementing it in your project for messaging systems that require text data like SQS will improve execution time and reduce costs.

## Local preformance testing table
Preformance from local testing for small and large data structures. These are not 'scientific' tests. Just to get a feeling about a difference between JSON and Protocol Buffers decoding and encoding. Devices used: M1 Mac and Orange Pi Zero 2.

Large message (1M requests)
| Processor | Python | JSON encoding | Protocol Buffers encoding | JSON / Protobuf encoding | JSON decoding | Protocol Buffers decoding | JSON / Protobuf decoding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 Core (4 preformance and 4 efficiency) ARM64  | 3.11.1 | 1.9631309509277344 | 1.347931146621704 | 0.6866231445154997 | 3.492576837539673 | 2.019235849380493 | 0.5781507303366683 |
| 4 Core (4 efficiency) ARM64 | 3.11.0rc1 | 21.885425567626953 | 19.293643951416016 | 0.8815749957339319 | 69.38900542259216 | 23.518123388290405 | 0.3389315532779377 |

Small message (1M requests)
| Processor | Python | JSON encoding | Protocol Buffers encoding | JSON / Protobuf encoding | JSON decoding | Protocol Buffers decoding | JSON / Protobuf decoding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 Core (4 preformance and 4 efficiency) ARM64  | 3.11.1 | 1.389113187789917 | 0.7344670295715332 | 0.528730873788674 | 1.161815881729126 | 0.5950100421905518 | 0.5121379829177414 |
| 4 Core (4 efficiency) ARM64 | 3.11.0rc1 | 34.81385159492493 | 14.071361780166626 | 0.4041885955019672 | 28.355868339538574 | 14.50603437423706 | 0.5115708043407113 |

## Additional info
- For more info about Protocol Buffers check: https://protobuf.dev/
- Beating JSON performance with Protobuf from Auth0: https://auth0.com/blog/beating-json-performance-with-protobuf/
- JSON to .proto converter: https://json-to-proto.github.io/