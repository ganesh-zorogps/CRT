'''
    n=int(input())
    for i in range(n, 0, -1):
        print(" " * (n - i) + "X " * i)
    for i in range(2, n + 1):
        print(" " * (n - i) + "X " * i)
        
    n=int(input())
    for i in range(1, n + 1):
        print(" " * (n - i) + "X " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "X " * i)

    n=int(input())
    for i in range(1, n + 1):
        print("X " * i + "  " * (n - i) * 2 + "X " * i)
    for i in range(n, 0, -1):
        print("X " * i + "  " * (n - i) * 2 + "X " * i)


    n=int(input())
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()

    n=int(input())
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print((i + j) % 2, end=' ')
        print()

    n=int(input())
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print((i + j) % 2, end=' ')
        print()

'''
