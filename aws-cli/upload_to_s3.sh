#!/bin/bash

# Variables
S3_BUCKET="covid-data-pipeline"

# Subir scripts
aws s3 cp ../scripts/captura_datos_api.py s3://$S3_BUCKET/scripts/
aws s3 cp ../scripts/ingestion_mysql.py s3://$S3_BUCKET/scripts/
aws s3 cp ../scripts/etl_spark.py s3://$S3_BUCKET/scripts/
aws s3 cp ../scripts/analysis_spark.py s3://$S3_BUCKET/scripts/
aws s3 cp ../scripts/lambda_athena_query.py s3://$S3_BUCKET/scripts/

# Subir SQL
aws s3 cp athena_create_table.sql s3://$S3_BUCKET/scripts/
