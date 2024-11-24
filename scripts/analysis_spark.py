from pyspark.sql import SparkSession

def analysis_spark():
    spark = SparkSession.builder.appName("COVID_Analysis").getOrCreate()

    trusted_data = spark.read.parquet("s3://covid-data-pipeline/trusted/covid_combined_data/")

    trusted_data.createOrReplaceTempView("covid_data")
    result = spark.sql("SELECT region, SUM(cases) as total_cases FROM covid_data GROUP BY region ORDER BY total_cases DESC")
    
    result.write.mode("overwrite").parquet("s3://covid-data-pipeline/refined/covid_analysis/")
    print("Análisis completado y resultados cargados en Refined.")

if __name__ == "__main__":
    analysis_spark()
