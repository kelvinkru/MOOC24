from math import sqrt

def tst():
    while True:
        number = int(input('Enter a number. Put -1 to exit: '))
        if number == -1:
            print('chao')
            break
        print(number**2)

def cont():
    cont = 1
    while cont == 1:
        print('hi')
        cont = str(input('Shall we continue?'))
        if cont == 'no':
            print('okay then')
            break
        else:
            cont = 1

def nmbrs():
    while True:
        nr = int(input('Enter a number. Put 0 to exit: '))
        if nr == 0:
            print('chao')
            break
        elif nr <0:
            print('Invalid number')
        else:
            print(sqrt(nr))

def cntdwn():
    number = 5
    print('Countdown')
    while number > 0:
        print(number)
        number -= 1
    print('Now!')

def password():
    p1 = str(input('Enter your password: '))
    while True:
        p2 = str(input('Enter your password again: '))
        if p1 == p2:
            print('Account created!')
            break
        print('Passwords do not match')

def codes():
    pin = 4321
    attempts = 0
    while True:
        pin_u = int(input('Enter pin number: '))
        attempts += 1
        if pin_u == pin:
            print(f'Correct and you took {attempts} attempts')
            break
        print('Wrong pin number')

def leap_year():
    year_i = int(input('Enter a year: '))
    year = year_i + 1
    while True:
        if year %4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False
        if leap:
            print(f'Next leap year after {year_i} is {year}')
            break
        year+=1

def numbers():
    i = 0
    j = 0
    p = 0
    n = 0
    while True:
        number = int(input('Enter a number. Put 0 to exit: '))
        if number == 0:
            break
        i += 1
        j+= number
        if number >0:
            p+=1
        if number <0:
            n+=1

    print(f'Numbers typed {i}')
    print(f'Sum of Numbers {j}')
    print(f'Mean is {j/i}')
    print(f'Positive nr {p}')
    print(f'Negative nr {n}')

if __name__ == '__main__':
    numbers()