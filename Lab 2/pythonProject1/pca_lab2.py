print("1 : from dec \n2 : to dec")
f = input()
if any(not i.isnumeric() for i in f):
    print("Invalid Selection")
    exit(1)
try:
    f = int(f)
except ValueError:
    print("Invalid Selection")
    exit(1)


def from_dec(b, n):
    ans = []

    while n >= 1:
        r = n % b
        n = n // b  # r is remainder, n is input number, b is input base
        if b >= 16 and r > 9:
            x = chr(r + 55)  # translate from decimal to ascii
            ans.append(x)
        else:
            ans.append(r)
    ans.reverse()  # reverse the ans list order
    return ans


def to_dec(b, s):
    d = 0
    lst = [*str(s)]  # split string s to list
    if len(lst) == 0:
        print("Invalid list empty")
        exit(1)
    lst.reverse()
    for i in range(len(lst)):
        if lst[i].isalpha():
            lst[i].capitalize()
        elif ord(lst[i]) - 55 > b:  # if dec more than base
            print("Invalid Input")
            exit(1)
        elif ord(lst[i]) >= 65:  # (A is 65 in dec)
            x = ord(lst[i]) - 55  # translate num --> ascii --> dec
            d += x * (b ** i)
        else:
            d += int(lst[i]) * (b ** i)  # d = d + reverse int s list * (b power i)
    return d


if f == 1:
    try:
        print("Enter base : ")
        b = int(input())
        if b <= 1 or b > 36:
            print("Invalid Input")
            exit(1)  # exit programme
        print("Enter decimal : ")
        n = int(input())
        if n < 0:
            print("Invalid Input")
            exit(1)
        print(from_dec(b, n))
    except ValueError:
        print("Invalid Input")
        exit(1)

elif f == 2:
    try:
        print("Enter base : ")
        b = int(input())
        if b <= 1 or b > 36:
            print("Invalid Input")
            exit(1)
        print("Enter string : ")
        s = str(input())
        print(to_dec(b, s))
    except ValueError:
        print("Invalid Input")
        exit(1)
else:
    print("Invalid Selection")
    exit(1)
