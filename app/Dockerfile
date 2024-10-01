# Use Python 3.9-slim base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the local directory to the container
COPY . .

# Install dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to the host machine
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "app.py"]