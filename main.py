

def cube(n):
    try:
        return n * n * n
    except Exception as ex:
        print(ex)
n = int(input("Enter number: "))
print(cube(n))
