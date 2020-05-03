n = int(input())
squares = []
for integer in range(1, n+1):
    squares = integer**2
    if squares > n:
        break
    print(squares)
