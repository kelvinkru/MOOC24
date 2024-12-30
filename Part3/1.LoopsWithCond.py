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

if __name__ == '__main__':
    cntdwn()