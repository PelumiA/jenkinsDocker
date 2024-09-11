# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Make port 8000 available outside the container
EXPOSE 8000

# Run the Python script when the container launches
CMD ["python", "app.py"]