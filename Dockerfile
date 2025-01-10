# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the serving app and model files into the container
COPY serving/ /app
COPY models/ /app/models

# Install serving-specific dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port for the FastAPI application
EXPOSE 8080

# Command to run the FastAPI application
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8080"]
