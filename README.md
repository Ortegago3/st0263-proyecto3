# **Proyecto 3**
#
# ST0263 Tópicos Especiales en Telemática
#
# Estudiante(s): 
- Holmer Ortega Gomez
- Moises David Arrieta Hernandez
- Alberto Andres Diaz Mejia
- Andres Felipe Rua Ortega
#
# Link Videosustentacion: https://youtu.be/3oob617JI9w?si=GWUtA0Zr0-f30JQi

---

# COVID Data Pipeline: Automatización del Proceso de Gestión de Datos de COVID

## **1. Breve descripción de la actividad**
El objetivo del proyecto es diseñar e implementar un pipeline de datos para capturar, procesar y analizar información sobre el COVID en Colombia. Utilizando herramientas de AWS y tecnologías de Big Data, el pipeline incluye:
1. Captura automática de datos desde una API pública y una base de datos MySQL.
2. Almacenamiento de datos en Amazon S3.
3. Procesamiento ETL con Apache Spark en un clúster EMR.
4. Análisis descriptivo y consulta de datos con Amazon Athena.
5. Exposición de resultados mediante una API basada en Lambda y API Gateway.

### **1.1. Aspectos cumplidos de la actividad**
1. **Captura de datos desde una API pública:**
   - Se implementó y ejecutó exitosamente el script `captura_datos_api.py`, que descarga datos desde la API de COVID-19 y los almacena en la carpeta `raw/` del bucket S3.
2. **Simulación de datos adicionales:**
   - Se creó y cargó un dataset simulado (`mysql_patient_data.csv`) a la carpeta `raw/` del bucket S3 utilizando el script `ingestion_mysql.py`.
3. **Configuración de Amazon S3:**
   - Se organizaron las carpetas `raw/`, `trusted/` y `refined/` en el bucket S3.
   - Los datos capturados se almacenaron correctamente en la estructura del bucket.
4. **Entorno configurado para Spark:**
   - Se configuraron Spark y las dependencias necesarias para el procesamiento distribuido de datos.

### **1.2. Aspectos no cumplidos**
1. **Procesamiento de datos con `etl_spark.py`:**
   - No fue posible ejecutar correctamente el script de ETL debido a problemas con la configuración del conector de Hadoop para S3 (`UnsupportedFileSystemException: No FileSystem for scheme "s3"`). Esto impidió mover los datos de la carpeta `raw/` a `trusted/`.
2. **Análisis de datos con `analysis_spark.py`:**
   - Debido a que el procesamiento ETL no se completó, no se pudieron realizar los análisis definidos en el script.
3. **Consulta automatizada con `lambda_athena_query.py`:**
   - El script no se ejecutó porque los datos analizados no estaban disponibles en la carpeta `refined/`.
4. **Integración completa con AWS Athena:**
   - No se logró configurar correctamente AWS Athena para consultar los datos procesados debido a la falta de datos en las etapas previas.
 
---

## **2. Información general de diseño de alto nivel**
### Arquitectura
El pipeline sigue una arquitectura basada en datos con las siguientes etapas:
1. **Captura de datos**: Descarga desde una API pública y extracción desde MySQL.
2. **Almacenamiento**: Datos almacenados en Amazon S3 en tres zonas (`raw`, `trusted`, `refined`).
3. **Procesamiento ETL**: Realizado en Apache Spark sobre EMR.
4. **Análisis y consultas**: Resultados accesibles mediante Amazon Athena y API Gateway.

### Mejores prácticas utilizadas
- Uso de herramientas nativas de AWS para escalabilidad y facilidad de integración.
- Separación de datos en zonas de almacenamiento (`raw`, `trusted`, `refined`).
- Procesamiento distribuido para manejar grandes volúmenes de datos.
- Implementación de automatización para minimizar la intervención manual.

![image](https://github.com/user-attachments/assets/441a20b5-f42e-487c-bdf9-742fa9010ddf)
![image](https://github.com/user-attachments/assets/27c7010c-c91e-48c4-bb92-b9b59c56493c)

---

## **3. Descripción del ambiente de desarrollo**
### Herramientas utilizadas
- **Lenguaje**: Python 3.9
- **Librerías**:
  - `boto3` (1.28.57): Interacción con servicios AWS.
  - `pymysql` (1.0.3): Conexión a MySQL.
  - `pandas` (2.1.1): Manipulación de datos.
  - `requests` (2.31.0): Solicitudes HTTP.
  - `pyspark` (3.5.0): Procesamiento distribuido.
  
### Cómo se compila y ejecuta
1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Subir scripts y datos a S3**:
```bash 
aws-cli/upload_to_s3.sh
```
3. **Crear clúster EMR y agregar pasos**:
```bash
aws-cli/create_emr_cluster.sh
aws-cli/add_steps_emr.sh
```
4. **Configurar y consultar Athena: Ejecutar las consultas desde la consola de Athena o usar**: 
```bash 
aws-cli/run_athena_query.sh
```

## **4. Descripción del ambiente de ejecución**
### Configuración en AWS
- Amazon S3: Bucket covid-data-pipeline con las zonas raw, trusted y refined.
- Amazon EMR: Clúster con 3 nodos m5.xlarge.
- Amazon Athena: Consultas configuradas en la base default.
- API Gateway y Lambda: Consulta de resultados analíticos.

### Configuración en AWS
- Subir scripts y configurar S3.
- Crear y configurar clúster EMR.
- Configurar Athena para consultas.
- Integrar API Gateway con Lambda para resultados analíticos.

## Referencias
- Ministerio de Salud de Colombia - [Dataset de COVID](https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD)
### Documentación de AWS:
- Amazon S3 - https://aws.amazon.com/s3/
- Amazon EMR - https://aws.amazon.com/emr/
- Amazon Athena - https://aws.amazon.com/athena/
- Guías de PySpark: https://spark.apache.org/docs/latest/api/python/
