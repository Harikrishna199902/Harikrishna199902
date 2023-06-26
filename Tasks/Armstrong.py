

num = int(input("Please Enter a Number: "))
digits = [int(digit) for digit in str(num)]
count = len(digits)
sum = sum([digit ** count for digit in digits])
if num == sum:
    print("Given ", num, "is an Armstrong number")
else:
    print("Given ", num, "is not an Armstrong number")