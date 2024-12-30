def fizzbuzz():
    nr = int(input("Enter a number: "))
    if nr%3 == 0 and nr%5 == 0:
        print('fizzbuzz')
    elif nr%3 == 0:
        print('fizz')
    elif nr%5 == 0:
        print('buzz')

if __name__ == '__main__':
    fizzbuzz()