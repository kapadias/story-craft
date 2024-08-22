# Start from a Python 3.9 slim image optimized for the amd64 architecture
FROM --platform=linux/amd64 python:3.9.16-slim

# Update the package repository, install GCC for compiling C/C++ extensions,
# and clean up the package lists afterwards to minimize the image size.
RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Create an application directory inside the container
RUN mkdir /app

# Copy the contents of the current directory on the host to the /app directory in the container
COPY ./ /app

# Set the working directory to /app for subsequent instructions
WORKDIR /app

# Set the PYTHONPATH environment variable to include the current working directory.
# This ensures that Python can find the modules located in /app during runtime.
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

# Install Poetry, a dependency management tool, and configure it:
# 1. Disable the creation of virtual environments since Docker containers are isolated environments.
# 2. Install the project's dependencies excluding development dependencies and the root package itself.
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root

# Expose port 8080, which is the default port that Streamlit listens on.
EXPOSE 8080

# Set the container's entry point to run Streamlit with the specified options:
# 1. Run the main.py script located in /app.
# 2. Bind the server to port 8080 and listen on all interfaces (0.0.0.0).
ENTRYPOINT ["streamlit", "run", "/app/main.py", "--server.port=8080", "--server.address=0.0.0.0"]
