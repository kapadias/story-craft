# Start from a Python 3.9 slim image
FROM --platform=linux/amd64 python:3.9.16-slim

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

# Expose the port that Streamlit listens on
EXPOSE 8080

# Run Streamlit when the container launches
ENTRYPOINT ["streamlit", "run", "./app/main.py", "--server.port=8080", "--server.address=0.0.0.0"]