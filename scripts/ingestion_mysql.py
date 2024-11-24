import pymysql
import pandas as pd
from io import StringIO
import boto3

BUCKET_NAME = "covid-data-pipeline"
AWS_REGION = "us-east-1"
DB_HOST = "mysql-instance.cq2lxqz6odba.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "password123"
DB_NAME = "covid_database"

def ingestion_mysql():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    query = "SELECT * FROM patient_data"
    
    df = pd.read_sql(query, conn)
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    
    s3 = boto3.client('s3', region_name=AWS_REGION)
    s3.put_object(Bucket=BUCKET_NAME, Key="raw/mysql_patient_data.csv", Body=csv_buffer.getvalue())
    print(f"Datos extraídos y cargados a S3: s3://{BUCKET_NAME}/raw/mysql_patient_data.csv")
    conn.close()

if __name__ == "__main__":
    ingestion_mysql()
