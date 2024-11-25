import pandas as pd
from io import StringIO
import boto3

BUCKET_NAME = "covid-data-pipeline"
AWS_REGION = "us-east-1"

def ingestion_mysql():
    # Simulación de datos
    data = {
        "patient_id": [1, 2, 3],
        "name": ["John Doe", "Jane Smith", "Alice Brown"],
        "age": [30, 25, 35],
        "diagnosis": ["COVID-19", "Recovered", "Vaccinated"]
    }
    df = pd.DataFrame(data)
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    
    # Cargar datos simulados a S3
    s3 = boto3.client('s3', region_name=AWS_REGION)
    s3.put_object(Bucket=BUCKET_NAME, Key="raw/mysql_patient_data.csv", Body=csv_buffer.getvalue())
    print(f"Datos simulados cargados a S3: s3://{BUCKET_NAME}/raw/mysql_patient_data.csv")

if __name__ == "__main__":
    ingestion_mysql()
