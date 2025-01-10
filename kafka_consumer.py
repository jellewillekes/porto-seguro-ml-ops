from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Start reading from the beginning
    enable_auto_commit=True
)
print("Listening for messages on 'test-topic'...")
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
