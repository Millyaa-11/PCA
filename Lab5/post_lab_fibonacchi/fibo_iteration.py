def fibo_ite(n):
    fib_lst = []
    fib_lst_final = []
    for i in range(1, n):
        fib_lst.append(i)
        fib_lst_final.append(fib_lst[i] + fib_lst[i+1])
    return fib_lst_final


print(fibo_ite(4))
