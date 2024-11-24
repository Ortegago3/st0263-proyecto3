import boto3
import requests

BUCKET_NAME = "covid-data-pipeline"
AWS_REGION = "us-east-1"

def captura_datos_api():
    API_URL = "https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD"
    file_name = "raw/covid_data.csv"
    
    response = requests.get(API_URL)
    if response.status_code == 200:
        s3 = boto3.client('s3', region_name=AWS_REGION)
        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=response.content)
        print(f"Datos cargados exitosamente en S3: s3://{BUCKET_NAME}/{file_name}")
    else:
        print(f"Error al descargar datos: {response.status_code}")

if __name__ == "__main__":
    captura_datos_api()
