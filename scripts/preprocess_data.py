from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("PreprocessPortoSeguro").getOrCreate()

    # Example: read raw data, fill nulls, write processed
    df = spark.read.csv('data/train.csv', header=True, inferSchema=True)
    df = df.na.fill(0)
    df.write.parquet('data/processed/train.parquet')

    spark.stop()


if __name__ == "__main__":
    main()
