import pandas as pd
import json
from kafka import KafkaProducer


def main():
    # Initialize producer
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',  # Adjust if not local
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Load data
    df = pd.read_csv('data/train.csv')  # Or data/raw/your_dataset.csv

    # Send each row as a message
    for _, row in df.iterrows():
        producer.send('porto_seguro_topic', row.to_dict())

    producer.close()


if __name__ == "__main__":
    main()
