# Define a function to rate the student's performance
def rate_performance(grade):
  if grade > 80:
    return "Distinction"
  elif 60 <= grade <= 70:
    return "Credit"
  elif 40 <= grade <= 50:
    return "Fair"
  else:
    return "Fail"
# Get the student's grade
grade = int(input("Enter the student's grade: "))
# Call the function and print the result
print("The student's performance is " + rate_performance(grade))

#And here is a simple calculator program in Python that can perform the operations you mentioned:

# Define a function to add two numbers
def add(x, y):
  return x + y

# Define a function to multiply two numbers
def multiply(x, y):
  return x * y

# Define a function to divide two numbers
def divide(x, y):
  return x / y

# Define a function to subtract two numbers
def subtract(x, y):
  return x - y

# Get the two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print the results
print("Sum: " + str(add(num1, num2)))
print("Product: " + str(multiply(num1, num2)))
print("Quotient: " + str(divide(num1, num2)))
print("Difference: " + str(subtract(num1, num2)))
