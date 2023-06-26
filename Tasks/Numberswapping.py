a = int(input("Please give the first number a: "))
b = int(input("Please give the second number b: "))

tempvar = a
a = b
b = tempvar

print("After swapping:")
print("Value of a is:", a)
print("Value of b is:", b)
