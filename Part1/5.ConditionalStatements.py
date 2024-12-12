def absval():
    nr  = int(input("Enter a number: "))
    if nr < 0:
        abs = nr*-1
    else:
        abs = nr
    print(f"Abs value {abs}")

def magn():
    nr = int(input("Enter a number: "))
    if nr < 1000:
        print("Smaller than 1,000")
    if nr < 100:
        print("Smaller than 100")
    if nr < 10:
        print("Smaller than 10")
    print("Thanks")

if __name__ == '__main__':
    magn()