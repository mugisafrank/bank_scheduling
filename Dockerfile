# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the needed.txt file into the container
COPY needed.txt .

# Install dependencies
RUN pip install --no-cache-dir -r needed.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "Bank.py"]