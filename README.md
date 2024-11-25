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
#

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
- Captura de datos desde fuentes reales (API pública y MySQL).
- Procesamiento y transformación de datos con Apache Spark en un clúster EMR.
- Almacenamiento de datos procesados en Amazon S3.
- Consulta de datos refinados con Amazon Athena.
- Exposición de resultados mediante una API Gateway integrada con AWS Lambda.
- Documentación detallada y estructura del proyecto en GitHub.

### **1.2. Aspectos no cumplidos**
- *Todos los aspectos del proyecto fueron desarrollados según lo requerido*.
 
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
