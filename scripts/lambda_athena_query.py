import boto3

def lambda_handler(event, context):
    client = boto3.client('athena', region_name='us-east-1')
    BUCKET_NAME = "covid-data-pipeline"
    query = "SELECT region, total_cases FROM covid_analysis ORDER BY total_cases DESC LIMIT 10;"
    
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': 'default'},
        ResultConfiguration={'OutputLocation': f"s3://{BUCKET_NAME}/athena-results/"}
    )
    
    query_execution_id = response['QueryExecutionId']
    return {
        "statusCode": 200,
        "body": f"Consulta ejecutada. ID: {query_execution_id}"
    }
