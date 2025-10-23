def down(n):
    if(n == 0):
        return
    print(n)
    down(n-1)


down(10)