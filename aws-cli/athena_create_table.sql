CREATE EXTERNAL TABLE IF NOT EXISTS covid_analysis (
    region STRING,
    total_cases BIGINT
)
STORED AS PARQUET
LOCATION 's3://covid-data-pipeline/refined/covid_analysis/';
