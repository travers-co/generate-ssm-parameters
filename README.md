# ssm-parameter-generator

This script generates SSM parameters in an AWS account based on the contents of a CSV file.
The CSV file should have the following headers: 
- Name (string)
- Type ("String" | "StringList" | "SecureString")
- Value (string)
- Description (string)

## Installation
First, create a virtual env for python version 3.8+.
Next, download or extract the source code into a working directory.
Then, activate the virtual environment and run:
- "pip install --editable . " 

This will install the script to your virtual environment.

## Usage
To run the script:
- generate-ssm-parameters CSV-FILE-NAME --profile AWS-PROFILE --region AWS-REGION

The script supports the following option:
- profile: specifies the aws profile to use while running the script. Defaults to "default".
- region: specifies the aws region to use while running the script. Defaults to "us-east-1".# generate-ssm-parameters
