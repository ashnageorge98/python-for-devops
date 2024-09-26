# Here's a simple Python script that showcases various concepts like functions, modules, and packages within the context of a DevOps and cloud project. 
The code simulates a basic workflow for interacting with a cloud service (like AWS) to manage resources.

# cloud_manager.py (Module)

import boto3  # AWS SDK for Python

def create_s3_bucket(bucket_name):
    """Create an S3 bucket."""
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f'Bucket {bucket_name} created.')

def list_s3_buckets():
    """List all S3 buckets."""
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    print("Existing buckets:")
    for bucket in buckets['Buckets']:
        print(f'  {bucket["Name"]}')

def delete_s3_bucket(bucket_name):
    """Delete an S3 bucket."""
    s3 = boto3.client('s3')
    s3.delete_bucket(Bucket=bucket_name)
    print(f'Bucket {bucket_name} deleted.')

# main.py (Entry Point)

from cloud_manager import create_s3_bucket, list_s3_buckets, delete_s3_bucket

def main():
    """Main function to manage cloud resources."""
    print("Welcome to Cloud Resource Manager!")
    
    while True:
        print("\nMenu:")
        print("1. Create S3 Bucket")
        print("2. List S3 Buckets")
        print("3. Delete S3 Bucket")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            bucket_name = input("Enter the S3 bucket name: ")
            create_s3_bucket(bucket_name)
        elif choice == '2':
            list_s3_buckets()
        elif choice == '3':
            bucket_name = input("Enter the S3 bucket name to delete: ")
            delete_s3_bucket(bucket_name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

