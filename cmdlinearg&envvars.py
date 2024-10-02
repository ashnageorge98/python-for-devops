Here's a simple Python script that demonstrates how to use command line arguments and environment variables in a DevOps or SRE context. 
The code reads an environment variable to determine the cloud service to use (for example, AWS or Azure) and takes command line arguments
to specify a resource name and its type (like "VM" or "Bucket"). It then prints a message based on these inputs.

import os
import sys

def main():
    # Check if the required environment variable is set
    cloud_service = os.getenv('CLOUD_SERVICE')
    if cloud_service is None:
        print("Error: Please set the CLOUD_SERVICE environment variable.")
        sys.exit(1)

    # Check if enough command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <resource_name> <resource_type>")
        sys.exit(1)

    # Read command line arguments
    resource_name = sys.argv[1]
    resource_type = sys.argv[2]

    # Construct the message based on the inputs
    message = f"Deploying a {resource_type} named '{resource_name}' to {cloud_service}."
    
    # Print the message
    print(message)

if __name__ == "__main__":
    main()

Explanation:
1. Importing Modules:
- os: To access environment variables.
- sys: To handle command line arguments and exit the program if needed.

2.Defining the main Function:
- This function contains the core logic of the script.

3. Checking Environment Variables:
- The script checks for an environment variable called CLOUD_SERVICE. If it’s not set, it prints an error message and exits.

4. Handling Command Line Arguments:
- The script expects two command line arguments:
  - resource_name: The name of the resource to be created.
  - resource_type: The type of the resource (like VM, Bucket, etc.).
- If the correct number of arguments is not provided, it prints usage instructions and exits.

5. Constructing and Printing a Message:
- It constructs a message using the provided resource name, resource type, and the cloud service name, then prints it to the console.

How to Run the Script
1. Set the Environment Variable:
- In your terminal, set the environment variable for the cloud service. For example, 
in Linux:
- export CLOUD_SERVICE=AWS
in Windows:
- set CLOUD_SERVICE=AWS

Execute the script from the terminal with command line arguments:
- python script.py MyResource VM
Output:
- Deploying a VM named 'MyResource' to AWS.
