#!/bin/bash

# Get the current date and time in the format YYYYMMDDHHMMSS.
# This timestamp will be used to uniquely tag the Docker image.
dte=$(date +'%Y%m%d%H%M%S')

# Define the container registry image name.
# The image will be tagged with the current timestamp to ensure uniqueness.
CONTAINER_REGISTRY_IMAGE="us-east1-docker.pkg.dev/inspired-skill-371914/ar-personal-streamlit-apps/story-craft:$dte"

# Build the Docker image using the Dockerfile in the current directory.
# The image is tagged with the registry image name that includes the timestamp.
docker build -t "$CONTAINER_REGISTRY_IMAGE" -f Dockerfile .

# Push the tagged Docker image to the specified Google Container Registry.
# This makes the image available for deployment.
docker push "$CONTAINER_REGISTRY_IMAGE"

# Remove the local Docker image to free up disk space.
# This is important in CI/CD pipelines or local development environments with limited storage.
docker rmi "$CONTAINER_REGISTRY_IMAGE"

# Deploy the Docker image to Google Cloud Run.
# The service is deployed to the specified region with the managed platform.
# The --allow-unauthenticated flag allows the service to be publicly accessible.
gcloud run deploy cr-personal-streamlit-na-story-craft \
  --allow-unauthenticated \
  --image="$CONTAINER_REGISTRY_IMAGE" \
  --region=us-east1 \
  --platform=managed
