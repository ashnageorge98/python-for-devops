Here’s a simple Python script that demonstrates the basic concepts of loops—for loop, while loop, and nested loops
# A simple DevOps project to check server statuses using loops

# List of server names
servers = ["server1", "server2", "server3", "server4"]

# Dictionary to hold server statuses
server_statuses = {
    "server1": "up",
    "server2": "down",
    "server3": "up",
    "server4": "down"
}

# For loop to print server names and their statuses
print("Checking server statuses using a for loop:")
for server in servers:
    status = server_statuses.get(server, "unknown")
    print(f"{server} is {status}")

# While loop to check for any down servers
print("\nChecking for any down servers using a while loop:")
index = 0
while index < len(servers):
    server = servers[index]
    if server_statuses[server] == "down":
        print(f"Alert! {server} is down!")
    index += 1

# Nested loop to simulate restarting down servers
print("\nRestarting down servers:")
for server in servers:
    if server_statuses[server] == "down":
        print(f"Attempting to restart {server}...")
        # Simulate restart process
        server_statuses[server] = "up"  # Change status to up
        print(f"{server} has been restarted successfully.")

# Final status check
print("\nFinal server statuses:")
for server in servers:
    print(f"{server} is {server_statuses[server]}")

Explanation:
List of Server Names:
We define a list called servers containing the names of four servers.
  
Dictionary for Statuses:
We create a dictionary server_statuses to hold the status of each server ("up" or "down").
  
For Loop:
We use a for loop to iterate through each server in the servers list and print its status. We use the get method to handle cases where a server might not be found, defaulting to "unknown".
  
While Loop:
The while loop checks each server's status to see if any are down. If a server is down, it prints an alert message. The loop continues until it has checked all servers.
  
Nested Loop:
We use a for loop to identify down servers and a nested operation to simulate restarting them. When a server is down, we print a message and update its status to "up".
                                                                                                                    
Final Status Check:
After the restart attempts, we again loop through the servers to print their final statuses.
                                                                                                                    
Use Case in DevOps
This code illustrates how loops can be used to automate the monitoring and management of servers, which is a common task in DevOps environments. 
By iterating through lists and checking statuses, you can efficiently manage resources and respond to issues in your infrastructure.

