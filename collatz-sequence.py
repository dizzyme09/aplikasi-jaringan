def collatz(number):
    try:
        while True:
            if number == 1:
                break
            else:
                if number % 2 == 0:
                    number = number // 2
                    print(number)
                else:
                    number = number * 3 + 1
                    print(number)
    except ZeroDivisionError:
        print('Error: Invalid argument, please input a positive integer')

try:
    inputNumber = int(input("Enter a number: "))
    collatz(inputNumber)
except ValueError:
    print('Error: Invalid argument, please input a number')