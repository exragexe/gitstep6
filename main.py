

def proste(n):
    try:
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    except Exception as ex:
        print(ex)
n = int(input("Enter number: "))
print(proste(n))