# Start from a Python 3.9 slim image
FROM python:3.9-slim

# Update the package repository and install GCC
RUN apt-get update && apt-get install -y \
  gcc \
  # Remove the package lists to free up space
  && rm -rf /var/lib/apt/lists/*

# Create an 'app' directory and copy the necessary files
RUN mkdir /app
copy ./ /app


# Set the working directory to the 'app' directory
WORKDIR /app

# Set the PYTHONPATH environment variable to include the current working directory
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

# Install Poetry and the project dependencies
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root

# Expose port 8080
EXPOSE 8080

# Set the entrypoint command to run 'main.py'
CMD ["streamlit", "run", "--server.port", "8080", "./app/main.py"]