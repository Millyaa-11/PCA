import numpy as np
import matplotlib.pyplot as plt
import timeit


def m01(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        sumit += 1
        rounds += 1
    return sumit


def m02(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        sumit += 1
        rounds += 2
    return sumit


def m03(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        rounds2 = 0
        while rounds2 < n:
            sumit += 1
            rounds2 += 1
        rounds += 1
    return sumit


def m04(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        rounds2 = 0
        while rounds2 < n:
            sumit += 1
            rounds2 += 10
        rounds += 20
    return sumit


def m05(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        sumit += 1
        rounds += 1
    rounds2 = 0
    while rounds2 < n:
        sumit += 1
        rounds2 += 1
    return sumit


def m06(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        rounds2 = 0
        while rounds2 < n * n:
            sumit += 1
            rounds2 += 1
        rounds += 1
    return sumit


def m07(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        rounds2 = 0
        while rounds2 < n * n:
            sumit += 1
            rounds2 += 1
        rounds += 1
    return sumit


def m08(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        rounds2 = 0
        while rounds2 < 100 * rounds:
            sumit += 1
            rounds2 += 1
        rounds += 1
    return sumit


def m09(n):
    rounds = 0
    sumit = 0

    while rounds < n:
        rounds2 = 0
        while rounds2 < n * n:
            rounds3 = 0
            while rounds3 < rounds2:
                sumit += 1
                rounds3 += 1
            rounds2 += 1
        rounds += 1
    return sumit


def m10(n):
    rounds = 1
    sumit = 0

    while rounds < n:
        sumit += 1
        rounds = rounds * 2
    return sumit


def m11(n):
    sumit = 0
    i = n

    while i > 0:
        sumit += 1
        i = i / 2
    return sumit


def m12(n):
    rounds = 1
    sumit = 0

    while rounds < n:
        sumit += 1
        rounds = rounds * 10
    return sumit


n = []  # y-axis
runtime = []  # x-axis
colours = ["red", "orange", "yellow", "brown", "black", "blue", "green", "purple", "pink", "cyan", "lightgreen", "magenta"]


numN = int(input("Input n : "))

for x in range(1, 12):
    storerun = []
    for i in range(0, numN, 10):  # increment to numN by 100
        if x == 1:
            n.append(i)
            start = timeit.default_timer()
            m01(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 2:
            start = timeit.default_timer()
            m02(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 3:
            start = timeit.default_timer()
            m03(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 4:
            start = timeit.default_timer()
            m04(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 5:
            start = timeit.default_timer()
            m05(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 6:
            start = timeit.default_timer()
            m06(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 7:
            start = timeit.default_timer()
            m07(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 8:
            start = timeit.default_timer()
            m08(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 9:
            start = timeit.default_timer()
            m09(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 10:
            start = timeit.default_timer()
            m10(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 11:
            start = timeit.default_timer()
            m11(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
        if x == 12:
            start = timeit.default_timer()
            m12(i)
            end = timeit.default_timer()
            run = end - start
            storerun.append(run)
    runtime.append(storerun)
nArray = np.array(n)
runTimeArray = np.array(runtime)
for i in range(len(colours)):
    print(f"m{i+1} colour is {colours[i]}")

for i in range(len(runtime)):
    plt.plot(nArray, runTimeArray[i], color=colours[i])
    plt.xlabel("n")
    plt.ylabel("Run Time")
plt.grid()
plt.show()
