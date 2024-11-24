#!/bin/bash

# Variables
CLUSTER_NAME="covid-emr-cluster"
LOG_URI="s3://covid-data-pipeline/logs/"
RELEASE_LABEL="emr-6.5.0"
INSTANCE_TYPE="m5.xlarge"
INSTANCE_COUNT=3
KEY_NAME="my-ec2-key"

# Crear clúster EMR
aws emr create-cluster \
  --name "$CLUSTER_NAME" \
  --release-label "$RELEASE_LABEL" \
  --applications Name=Spark Name=Hadoop \
  --ec2-attributes KeyName=$KEY_NAME \
  --instance-type $INSTANCE_TYPE \
  --instance-count $INSTANCE_COUNT \
  --use-default-roles \
  --log-uri $LOG_URI
