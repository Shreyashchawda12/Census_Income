## End To End ML Project

### created a environment
```
conda create -p "census" python==3.8

conda activate E:\Census_Income\census\
```
### Install all necessary libraries
``
pip install -r requirements.txt

### Deployment
1. Docker Build checked
2. Github Workflow
3. Iam User in AWS

## DOcker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## Configure EC2 as self-hosted runner:

### Setup github secrets:

AWS_ACCESS_KEY_ID = 

AWS_SECRET_ACCESS_KEY = 

AWS_REGION = ap-southeast-2

AWS_ECR_LOGIN_URL = 536633663342.dkr.ecr.ap-southeast-2.amazonaws.com

ECR_REPOSITORY_NAME = credit_card_prediction





