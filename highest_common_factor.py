
# Program to calculate the Highest Common Factor of two numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

while num2 != 0:
    rem = num1 % num2
    num1 = num2
    num2 = rem
    factor = num1
    print("Common Factor: ",factor)
    
print("The Highest Common Factor is:", factor)
