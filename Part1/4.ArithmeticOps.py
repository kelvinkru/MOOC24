def intdiv():
    x = 3
    y = 2
    print(f"/ gives {x/y}")
    print(f"// gives {x//y}")

def born():
    year  = int(input("Enter year: "))
    print(f"age at end of 2024 is {2024 - year}")

def sums():
    sum = 0
    sum+=int(input("Enter number 1: "))
    sum+=int(input("Enter number 2: "))
    sum+=int(input("Enter number 3: "))
    print(f"sum is {sum}")

def socnds():
    days = int(input("Enter number of days: "))
    print(f"Seconds in days: {days*24*60*60}")

def prod():
    prod = 1
    prod*=int(input("Enter number 1: "))
    prod*=int(input("Enter number 2: "))
    prod*=int(input("Enter number 3: "))
    print(f"sum is {prod}")

def studentgroups():
    total_students = int(input("Enter total students: "))
    group_size = int(input("Enter group size: "))
    if total_students/group_size == total_students//group_size:
        nr_groups = int(total_students/group_size)
    else:
        nr_groups = total_students // group_size +1
    print(f"Number of groups formed: {nr_groups}")

if __name__ == '__main__':
    studentgroups()