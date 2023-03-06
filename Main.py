num1= 0 
num2 = 1
while True:
    num1 = int(input('enter a number: '))
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(num2, num1)
        break

    num2 = num1