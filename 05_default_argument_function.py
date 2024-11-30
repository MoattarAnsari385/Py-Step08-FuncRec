# Default Argument

def greet(name, ending = "Thank You"): 
    print(f"Good day, {name}!")
        # Print the ending message (uses default value if not provided)
    print(ending)

# Call the greet function with both arguments (overrides the default value)
greet("Moattar") 
greet("Aashu", "No Thank") 