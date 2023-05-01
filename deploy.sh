# Get the current date and time in the format YYYYMMDDHHMMSS
dte=$(date +'%Y%m%d%H%M%S')

# Set the container registry image name with the current date and time variable
CONTAINER_REGISTRY_IMAGE=us-east1-docker.pkg.dev/inspired-skill-371914/ar-personal-streamlit-apps/story-craft:$dte

# Build a Docker image using the Dockerfile in the current directory, tag it with the registry image name and push it to the container registry
docker build -t $CONTAINER_REGISTRY_IMAGE -f Dockerfile .
docker push $CONTAINER_REGISTRY_IMAGE

# Remove the local Docker image to free up disk space
docker rmi $CONTAINER_REGISTRY_IMAGE

# Deploy the image to Google Cloud Run with the specified configuration
gcloud run deploy cr-personal-streamlit-na-story-craft \
  --allow-unauthenticated \
  --image=$CONTAINER_REGISTRY_IMAGE \
  --region=us-east1 \
  --platform=managed
