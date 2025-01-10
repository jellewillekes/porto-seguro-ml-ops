from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')  # Ensure Kafka is running
producer.send('test-topic', b'Hello, Kafka!')
producer.flush()
print("Message sent to Kafka topic 'test-topic'")
