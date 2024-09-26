The code calculates the total cost of cloud resources based on their usage and applies discounts where applicable
Operators in devops scenario:
# Python code demonstrating operators in a DevOps project scenario

# Constants for resource usage
vm_usage_hours = 120  # Total hours a VM is used
storage_usage_gb = 50  # Total GB of storage used
vm_cost_per_hour = 0.5  # Cost per hour for VM
storage_cost_per_gb = 0.1  # Cost per GB for storage

# Arithmetic Operators
total_vm_cost = vm_usage_hours * vm_cost_per_hour  # Multiplication
total_storage_cost = storage_usage_gb * storage_cost_per_gb  # Multiplication
total_cost = total_vm_cost + total_storage_cost  # Addition

# Output total costs
print("Total VM Cost: $", total_vm_cost)
print("Total Storage Cost: $", total_storage_cost)
print("Total Cost: $", total_cost)

# Comparison Operators
if total_cost > 100:  # Greater than comparison
    print("Warning: Total cost exceeds $100.")
else:
    print("Total cost is within budget.")

# Assignment Operators
discount_rate = 0.1  # 10% discount
final_cost = total_cost  # Assigning total cost to final cost
final_cost -= final_cost * discount_rate  # Subtracting discount

# Output final cost after discount
print("Final Cost after Discount: $", final_cost)

# Logical Operators
is_within_budget = final_cost <= 100  # Checking if final cost is within budget
is_discounted = discount_rate > 0  # Checking if there is a discount

# Output final checks
if is_within_budget and is_discounted:  # Logical AND
    print("Great! The project is within budget and has a discount applied.")
else:
    print("Alert! Review the costs.")
