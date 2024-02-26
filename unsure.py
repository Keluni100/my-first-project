print('Welcome to the calculator, enojy..')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
opt = input('Enter symbol, (+,-,*,/) : ')
print('Here is your answer: ')
if opt == '+':

    print(num1 + num2)
elif opt == '-':
    print(num1 - num2)
elif opt == '/':
    print(num1 / num2)
elif opt == '*':
    print(num1 * num2)
else :
    print('Invalid symbol, follow instructions')

print('Try another?')