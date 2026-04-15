from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count
import matplotlib.pyplot as plt

spark = SparkSession.builder.appName("SensorBatch").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)

# Limpieza
df = df.dropna().dropDuplicates()

print("=== Schema ===")
df.printSchema()

print("=== Total registros ===")
df.select(count("*")).show()

print("=== Estadisticas por sensor ===")
stats = df.groupBy("sensor_id").agg(
    avg("temperature").alias("avg_temp"),
    avg("humidity").alias("avg_humidity"),
    max("temperature").alias("max_temp"),
    min("temperature").alias("min_temp")
).orderBy("sensor_id")
stats.show()

print("=== Sensores con temperatura mayor a 27 ===")
df.filter(df.temperature > 27).groupBy("sensor_id").count().orderBy("sensor_id").show()

# Visualizacion
stats_pd = stats.toPandas()
plt.figure(figsize=(10, 5))
plt.bar(stats_pd["sensor_id"], stats_pd["avg_temp"], color="tomato", label="Temp Promedio")
plt.bar(stats_pd["sensor_id"], stats_pd["avg_humidity"], color="steelblue", label="Humedad Promedio", alpha=0.7)
plt.xlabel("Sensor ID")
plt.ylabel("Valor Promedio")
plt.title("Temperatura y Humedad Promedio por Sensor")
plt.legend()
plt.savefig("resultado_batch.png")
print("Grafica guardada como resultado_batch.png")
