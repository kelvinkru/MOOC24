def t1():
    begin = 'ex'
    end = 'amples'
    print(begin+end)
    word = begin + end
    print(word*2)

def pyr(n=10, m = '*'):
    n = n
    m = m
    mark = m
    while n > 0:
        print(' '*n + mark)
        n-=1
        mark+=m*2

def revs():
    string = str(input('Enter a string: '))
    l = len(string)
    for i in range(1, l+1):
        print(string[i*-1])

def right_aligned(n=20):
    string = str(input('Enter a string: '))
    print('*'*(n-len(string))+string)

def subs():
    string = str(input('Enter a string: '))
    l = len(string)
    cnt = 0
    while cnt < l:
        print(string[0:cnt+1])
        cnt+=1

def subs2():
    string = str(input('Enter a string: '))
    l = len(string)
    cnt = l
    while cnt >0:
        print(string[cnt-1:])
        cnt-=1

def subst():
    input = 'test'
    print('t' in input)
    print('x' in input)

def subst2():
    string = str(input('Enter a string: '))
    print('a found') if 'a' in string else print('a not found')
    print('e found') if 'e' in string else print('e not found')
    print('o found') if 'o' in string else print('o not found')

def find_ex():
    string = 'test'
    print(f't is {string.find('t')}')
    print(f'x is {string.find('x')}')
    print(f'tes is {string.find('tes')}')
    print(f's is {string.find('s')}')

def fisrt_subs():
    word = str(input('Type in a word: '))
    char = str(input('Type in a character: '))
    inx = word.find(char)
    if inx != -1:
        if len(word) - inx>3:
            print(word[inx:inx+3])

def all_subs():
    word = str(input('Type in a word: '))
    char = str(input('Type in a character: '))
    for l in range(len(word)):
        if l==0:
            word2 = word[l:]
        else:
            word2 = word[l+inx+1:]
        inx = word2.find(char)
        if inx != -1:
            if len(word2) - inx>3:
                print(word2[inx:inx+3])

if __name__ == '__main__':
    all_subs()