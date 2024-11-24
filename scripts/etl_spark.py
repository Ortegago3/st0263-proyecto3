from pyspark.sql import SparkSession

def etl_spark():
    spark = SparkSession.builder.appName("COVID_ETL").getOrCreate()

    covid_api_data = spark.read.csv("s3://covid-data-pipeline/raw/covid_data.csv", header=True, inferSchema=True)
    mysql_data = spark.read.csv("s3://covid-data-pipeline/raw/mysql_patient_data.csv", header=True, inferSchema=True)

    combined_data = covid_api_data.join(mysql_data, "common_column", "inner")

    combined_data.write.mode("overwrite").parquet("s3://covid-data-pipeline/trusted/covid_combined_data/")
    print("Procesamiento ETL completado y datos cargados en Trusted.")

if __name__ == "__main__":
    etl_spark()
