'''
factorial(0) = 1  
factorial(1) = 1  
factorial(2) = 2 X 1  
factorial(3) = 3 X 2 X 1  
factorial(4) = 4 X 3 X 2 X 1  
factorial(5) = 5 X 4 X 3 X 2 X 1  
factorial (n) = n X n-1 X...... 3 X 2 X 1

factorial (n) = n * factorial (n-1)
'''

def factorial (n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
        # Base case: factorial of 0 or 1 is 1
    if(n == 1 or n == 0):
        return 1
    
        # Recursive case: n * factorial of (n-1)
    return n * factorial (n - 1)

n = int(input("Enter a number: "))

print(f"The factorial of this number is: {factorial(n)}")