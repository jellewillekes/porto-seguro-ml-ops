from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("StreamPortoSeguro").getOrCreate()

    kafka_stream = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("subscribe", "porto_seguro_topic")
        .load()
    )

    # Example: just print to console
    query = kafka_stream.writeStream.format("console").start()
    query.awaitTermination()


if __name__ == "__main__":
    main()
