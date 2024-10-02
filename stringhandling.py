The code includes functions to manipulate strings, such as converting case, replacing substrings, and checking for substrings.
# String handling functions for DevOps and Cloud projects

def convert_to_uppercase(input_string):
    """Convert a string to uppercase."""
    return input_string.upper()

def convert_to_lowercase(input_string):
    """Convert a string to lowercase."""
    return input_string.lower()

def replace_substring(input_string, old, new):
    """Replace occurrences of a substring with another substring."""
    return input_string.replace(old, new)

def check_substring(input_string, substring):
    """Check if a substring exists in the input string."""
    return substring in input_string

def main():
    # Sample input string
    original_string = "Welcome to the Cloud Computing world!"

    # Convert to uppercase
    upper_string = convert_to_uppercase(original_string)
    print(f"Uppercase: {upper_string}")

    # Convert to lowercase
    lower_string = convert_to_lowercase(original_string)
    print(f"Lowercase: {lower_string}")

    # Replace substring
    replaced_string = replace_substring(original_string, "Cloud", "DevOps")
    print(f"Replaced String: {replaced_string}")

    # Check for substring
    exists = check_substring(original_string, "Cloud")
    print(f"Does 'Cloud' exist in the original string? {exists}")

if __name__ == "__main__":
    main()

Explanation of the Code:
Function Definitions:
convert_to_uppercase(input_string): Takes a string and returns it in uppercase using the .upper() method.
convert_to_lowercase(input_string): Takes a string and returns it in lowercase using the .lower() method.
replace_substring(input_string, old, new): Takes a string and replaces all occurrences of the substring old with new using the .replace() method.
check_substring(input_string, substring): Checks if substring exists within input_string and returns True or False.

main() Function:
This function serves as the entry point of the program.
It defines a sample string (original_string) for demonstration.
Calls each string handling function and prints the results to show the transformations.

Execution:
The code runs the main() function when the script is executed, showcasing how to handle strings in simple ways that could be useful in automation scripts or logging in DevOps environments.

Usage in DevOps/Cloud Projects:
Upper and Lowercase Conversions: Useful for standardizing input for scripts or configuration files.
Replacing Substrings: Handy for modifying paths or variable names in configuration files dynamically.
Checking for Substrings: Useful for validating presence or existence of certain keywords in logs or outputs, which can be essential in monitoring or alerting systems.
