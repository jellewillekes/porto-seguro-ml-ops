import pandas as pd


def extract_single_observation(input_file: str, output_file: str):
    """
    Extracts a single observation (excluding the target column) from a CSV file
    and saves it to a new file.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the single observation as a new CSV file.
    """
    try:
        # Load the dataset
        df = pd.read_csv(input_file)

        # Ensure the file is not empty
        if df.empty:
            raise ValueError("The input file is empty. Cannot extract an observation.")

        # Check if 'target' column exists and drop it
        if 'target' in df.columns:
            df = df.drop(columns=['target'])

        # Extract the first row (single observation)
        single_observation = df.iloc[0:1]

        # Save the single observation to a new file
        single_observation.to_csv(output_file, index=False)

        print(f"Single observation saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Input test file and output file paths
    input_file_path = "data/test.csv"
    output_file_path = "data/observation.csv"

    # Extract and save the single observation
    extract_single_observation(input_file=input_file_path, output_file=output_file_path)
