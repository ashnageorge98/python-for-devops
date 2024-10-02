Here's a simple Python script that uses the boto3 library to interact with AWS. This example demonstrates how to list all EC2 instances in your accoun

import boto3

def list_ec2_instances():
    # Create a session using your AWS credentials and default region
    session = boto3.Session(
        aws_access_key_id='YOUR_ACCESS_KEY',  # Replace with your access key
        aws_secret_access_key='YOUR_SECRET_KEY',  # Replace with your secret key
        region_name='us-west-2'  # Replace with your desired region
    )

    # Create an EC2 resource
    ec2 = session.resource('ec2')

    # List all instances
    print("Listing EC2 instances:")
    for instance in ec2.instances.all():
        print(f'Instance ID: {instance.id}, State: {instance.state["Name"]}, Type: {instance.instance_type}')

if __name__ == '__main__':
    list_ec2_instances()

Explanation
Importing Boto3: The script begins by importing the boto3 library, which is the AWS SDK for Python. This allows Python developers to create, configure, and manage AWS services.

Function Definition: The list_ec2_instances function is defined to encapsulate the logic of listing EC2 instances.

Creating a Session:

A session is created using the boto3.Session() method, where you provide your AWS access key, secret key, and the region you want to interact with.
Important: Replace 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_KEY' with your actual AWS credentials. Consider using IAM roles or AWS profiles for security reasons.
Creating EC2 Resource: The ec2 variable holds a resource object for EC2, allowing you to interact with EC2 services.

Listing Instances:

The script loops through all EC2 instances using ec2.instances.all().
For each instance, it prints the Instance ID, State (like running or stopped), and Instance Type (e.g., t2.micro).
Main Guard: The if __name__ == '__main__': line ensures that the list_ec2_instances function runs only if the script is executed directly, not if it’s imported as a module.

Usage
To run this script, make sure you have the boto3 library installed. You can install it using pip:
bash
Copy code
pip install boto3
Execute the script in a terminal or command prompt where Python is installed. Make sure your AWS credentials have the necessary permissions to list EC2 instances.
Note
Always be cautious with your AWS credentials. It’s a best practice to avoid hardcoding them directly into your scripts. Instead, consider using environment variables or AWS IAM roles for better security.
