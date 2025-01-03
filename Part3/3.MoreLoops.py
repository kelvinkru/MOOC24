def t1():
    ...

def cont():
    sum = 0
    nr = 0
    while nr != -1:
        nr = int(input('Enter a number. -1 to exit: '))
        if nr>10:
            continue
        if nr != -1:
            sum+=nr

    print(f'sum is {sum}')

def nested_loop():
    while True:
        nr = int(input('Enter a number. -1 to exit: '))
        if nr == -1:
            break
        while nr > 0:
            print(nr)
            nr-=1

def pyr():
    nr = int(input('Enter a number: '))
    while nr >=0:
        nr-=1
        i = 0
        while i<=nr:
            print(i, end=" ")
            i+=1
        print("")

def mult():
    nr = int(input('Enter a number: '))
    i = 1
    while i<=nr:
        j=1
        while j<=nr:
            print(f"{i} x {j} = {i*j}")
            j+=1
        i+=1

def first_l():
    sent = input('Enter a sentence: ')
    for word in sent.split():
        print(word[0])

def fact():
    nr = int(input('Enter a number. -1 to exit: '))
    nr_o = nr
    prod = 1
    i = 1
    while nr > 0:
        prod*=i
        i+=1
        nr-=1
    if nr_o >0:
        print(prod)

def fact_rec(n):
    if n ==0 or n ==1:
        return 1
    return n*fact_rec(n-1)

def flip_pairs():
    nr = int(input('Enter a number: '))
    i = 1
    j = nr // 2
    k = nr % 2
    while i < nr:
        sw = 1
        for m in range(j):
            for it in range(2):
                if sw == 1:
                    print(i+1)
                    sw+=1
                    i+=1
                if sw == 2:
                    print(i-1)
                    sw+=1
                    i+=1
    if k == 1:
        print(nr)

def taking_turns():
    nr = int(input('Enter a number: '))
    i = 1
    j = nr // 2
    k = nr % 2
    itt = 0
    nrt = 1
    while nrt < nr:
        sw = 1
        for m in range(j):
            for it in range(2):
                if sw == 1:
                    print(i)
                    sw+=1
                    i+=1
                    nrt+=1
                if sw == 2:
                    print(nr - itt)
                    sw+=1
                    nrt += 1
        itt+=1
    if k == 1:
        print(int((nr+1)/2))

if __name__ == '__main__':
    taking_turns()