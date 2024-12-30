def alphcomp():
    word1 = str(input("Enter a word: "))
    word2 = str(input("Enter another word: "))

    if word1 > word2:
        print(f'{word1} comes last')
    elif word2 > word1:
        print(f'{word2} comes last')
    else:
        print('same words')

if __name__ == '__main__':
    alphcomp()