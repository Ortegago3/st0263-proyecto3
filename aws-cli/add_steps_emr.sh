#!/bin/bash

# Variables
CLUSTER_ID="j-3XYZABC123456"  # ID del clúster creado previamente
S3_BUCKET="covid-data-pipeline"
STEP_ETL_SCRIPT="s3://$S3_BUCKET/scripts/etl_spark.py"
STEP_ANALYSIS_SCRIPT="s3://$S3_BUCKET/scripts/analysis_spark.py"

# Agregar paso ETL
aws emr add-steps --cluster-id $CLUSTER_ID \
  --steps Type=Spark,Name="ETL Step",ActionOnFailure=CONTINUE,Args=[s3://$STEP_ETL_SCRIPT]

# Agregar paso de análisis
aws emr add-steps --cluster-id $CLUSTER_ID \
  --steps Type=Spark,Name="Analysis Step",ActionOnFailure=CONTINUE,Args=[s3://$STEP_ANALYSIS_SCRIPT]
