def types():
    print(type('ANNA'))

def wages():
    hourly_wage = float(input('Hourly wage: '))
    hours = int(input('Number of hours: '))
    day = str(input('Day: '))

    daily_wages = hourly_wage*hours
    if day == 'Sunday':
        daily_wages*=2

    print(f'Daily wages {daily_wages} euros')

def lucky_nr():
    number = int(input('Enter a number: '))
    if number>100:
        print('more than 100')
        number-=100
        print(f'now number is {number}')
    print(f'number {number} is my lucky number')

def temp():
    temp = float(input('Enter a temp: '))
    print(f'int part is {int(temp)}')
    print(f'dec part is {round(temp - int(temp),2)}')

if __name__ == '__main__':
    temp()