#!/bin/bash

# Variables
DATABASE_NAME="default"
QUERY_STRING="SELECT region, total_cases FROM covid_analysis ORDER BY total_cases DESC LIMIT 10;"
OUTPUT_LOCATION="s3://covid-data-pipeline/athena-results/"
QUERY_ID_FILE="query_execution_id.txt"

# Ejecutar consulta en Athena
QUERY_ID=$(aws athena start-query-execution \
  --query-string "$QUERY_STRING" \
  --query-execution-context Database=$DATABASE_NAME \
  --result-configuration OutputLocation=$OUTPUT_LOCATION \
  --output text)

# Guardar Query Execution ID
echo $QUERY_ID > $QUERY_ID_FILE
echo "Consulta ejecutada. Query Execution ID: $QUERY_ID"
