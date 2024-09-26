# Importing required modules (keywords)
import os
import time

# Define constants (variables)
DEPLOYMENT_DIRECTORY = "/app/deploy"
SERVICE_NAME = "my-web-app"
IMAGE_VERSION = "v1.0"
HEALTH_CHECK_URL = "http://localhost:5000/health"

# Function to pull latest docker image (using variables and functions)
def pull_latest_image(service_name, version):
  print(f"Pulling latest image for {service_name}:{version}...")
  os.system(f"docker pull {service_name}:{version}")

# Function to deploy the application (function with retunr statement)
def deploy_service(service_name):
  print(f"Deploying {service_name}...")
  os.system(f"docker run -d --name {service_name} {service_name}:{IMAGE_VERSION}")
return True

# Function to check service health (using conditionals and loops)
def check_service_health(url):
  print("checking service health...")
  for attempt in range(3): Loops over health check attempts
  response = os.system(f" curl -s {url}")
  if response == 0: # Conditional check
    print("Service is healthy!")
    return True
  else:
    print("Health check failed. Retrying...")
    time.sleep(5)
  retunr False

  #Main block (using if-else)
  if __name__ == "__main":
    # Pull latest image
    pull_latest_image(SERVICE_NAME, IMAGE_VERSION)

#Deploy the service
if deploy_service(SERVIVE_NAME):
  print("Deployment successfull")

# Verify health status
if check_service_health(HEALTH_CHECK_URL):
  print("Deployment is healthy and complete:")
else:
  print("deployment failed health check")
