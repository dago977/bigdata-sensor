import json
import csv
from kafka import KafkaConsumer

consumer = KafkaConsumer('sensor_data', bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))

with open('sensor_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['sensor_id','temperature','humidity','timestamp'])
    writer.writeheader()
    count = 0
    for msg in consumer:
        writer.writerow(msg.value)
        count += 1
        print(f"Guardado: {msg.value}")
        if count >= 100:
            break

print("CSV generado con 100 registros.")
