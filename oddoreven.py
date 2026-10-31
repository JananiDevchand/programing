# Odd or Even

# This program checks if a number is odd or even.

def check_odd_even(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

if __name__ == '__main__':
    try:
        num = int(input('Enter a number: '))
        print(f'The number {num} is {check_odd_even(num)}.')
    except ValueError:
        print('Please enter a valid integer.')