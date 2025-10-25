#Program to find if a number is armstrong number
number = int(input("Input your number"))
#Calculate number of digits
digits = len(str(number))
#Initialize the number with 0
result = 0
temp = number
while temp > 0:
    digit = temp%10
    result+=digit**digits
    temp//=10
if number == result:
    print(number," is an armstrong number")
else:

    print("It is not a armstrong number")