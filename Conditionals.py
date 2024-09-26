# Define the service status
service_status = "running"  # Possible values: "running", "stopped", "failed"

# Check the status of the service and take action
if service_status == "running":
    print("The service is running smoothly.")
elif service_status == "stopped":
    print("The service is stopped. Starting the service...")
    # Here you would include code to start the service
else:
    print("The service has failed. Please check the logs.")
    # Here you would include code to handle the failure, like alerting or restarting


Explanation
Service Status Definition:

We define a variable service_status that holds the current status of a service. This could be set based on real checks in a production environment.
Conditional Statements:

if statement: This checks if the service status is "running". If it is, it prints a confirmation message.
elif statement: This checks if the service status is "stopped". If true, it prints a message indicating that it will start the service. You can later add actual code to start the service here.
else statement: If the service is neither running nor stopped (for example, if it has "failed"), this block will execute, printing a message to check the logs. This is where you might include error handling or notifications
