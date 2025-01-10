FROM python:3.9-slim

# Create app directory
WORKDIR /app

# Copy contents (including predict.py and requirements.txt)
COPY . /app

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Launch FastAPI with Uvicorn
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8080"]
