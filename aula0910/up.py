def up(n):
    if(n == 0):
        return
    up(n-1)
    print(n)

up(10)

