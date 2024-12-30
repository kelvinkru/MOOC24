def even():
    for i in range(2,31):
        if i %2 ==0:
            print(i)

def cntdwn():
    nr = int(input("Enter a number: "))
    while nr > 0:
        print(nr)
        nr-=1
    print('Now!')

def nr1():
    number = int(input("Enter a number: "))
    i = 1
    while i <= number-1:
        print(i)
        i+=1

def powr_two():
    limit = int(input("Enter Upper Limit: "))
    i = 1
    while i<=limit:
        print(i)
        i*=2

def base():
    limit = int(input("Enter Upper Limit: "))
    base = int(input("Enter Base Number: "))
    i = 1
    while i<=limit:
        print(i)
        i*=base

if __name__ == '__main__':
    base()