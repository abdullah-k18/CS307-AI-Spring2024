num = int(input("Enter a number:"))
factorial = 1
if num < 0:
    print("Please Enter a correct number.")
elif num == 0:
    print(f"Factorial of {num} = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"Factorial of {num} = {factorial}")