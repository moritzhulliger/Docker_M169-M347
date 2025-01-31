# Use a lightweight base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies defined in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Use a non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Define the command to run the application
CMD ["python", "app.py"]