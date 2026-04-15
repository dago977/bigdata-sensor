# bigdata-sensor
 Procesamiento de Datos con Apache Spark

## Descripción
Análisis de datos en tiempo real y batch usando Apache Spark, Kafka y Python.
Los datos simulan lecturas de sensores (temperatura, humedad) generadas en tiempo real.

## Requisitos
- Ubuntu 22.04
- Python 3.x
- Apache Spark 3.5.3
- Apache Kafka 3.8.0
- Librerías: kafka-python, matplotlib, pandas

## Instalación
```bash
pip install kafka-python matplotlib pandas
```

## Archivos
- `kafka_producer.py` — Genera datos simulados de sensores y los envía a Kafka
- `kafka_to_csv.py` — Captura 100 registros de Kafka y los guarda en CSV
- `spark_streaming_consumer.py` — Consume datos de Kafka en tiempo real con Spark Streaming
- `spark_batch.py` — Carga el CSV y realiza análisis exploratorio con PySpark

## Ejecución

### 1. Iniciar ZooKeeper y Kafka
```bash
sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties &
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties &
```

### 2. Crear el topic
```bash
/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor_data
```

### 3. Terminal 1 - Ejecutar producer
```bash
python3 kafka_producer.py
```

### 4. Terminal 2 - Ejecutar Spark Streaming
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_consumer.py
```

### 5. Terminal 3 - Capturar datos a CSV
```bash
python3 kafka_to_csv.py
```

### 6. Terminal 3 - Ejecutar análisis batch
```bash
spark-submit spark_batch.py
```

## Resultados
- Estadísticas por sensor (temperatura y humedad promedio, máxima y mínima)
- Filtro de sensores con temperatura mayor a 27°C
- Gráfica guardada en `resultado_batch.png`
