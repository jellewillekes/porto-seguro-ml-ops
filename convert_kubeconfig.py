import base64


def convert_kubeconfig_to_base64(file_path):
    try:
        # Open and read the kubeconfig file
        with open(file_path, "rb") as file:
            kubeconfig_data = file.read()

        # Convert the binary data to base64 string
        base64_encoded = base64.b64encode(kubeconfig_data).decode("utf-8")

        print("Base64 Encoded Kubeconfig:")
        print(base64_encoded)

        return base64_encoded
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the path to your kubeconfig.yaml file
file_path = "kubeconfig.yaml"

# Call the function to convert and print the base64 string
convert_kubeconfig_to_base64(file_path)
