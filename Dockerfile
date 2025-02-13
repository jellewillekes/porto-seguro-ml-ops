FROM python:3.10-slim

WORKDIR /app

# Copy serving script and model files
COPY serving/ /app/serving
COPY models/ /app/models

RUN pip install --upgrade pip

# Install dependencies
COPY serving/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port for the FastAPI app
EXPOSE 8080

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "serving.predict:app", "--host", "0.0.0.0", "--port", "8080"]
