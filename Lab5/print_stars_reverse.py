def stars(n):
    if n > 0:
        print("*" * n)
        stars(n - 1)
        print("*" * n)
    return n + 1


n = int(input("Input n : "))
stars(n)


def num_down(n):
    print("*" * n)
    if n > 1:
        num_down(n - 1)

def num_up(n):
    if n > 1:
        num_up(n - 1)
    print("*" * n)


def reverse_star(n):
    num_up(n)
    num_down(n)


n = int(input("Input n2 : "))
reverse_star(n)
