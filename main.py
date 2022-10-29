

def factorial(y):
    try:
        if y == 0 or y == 1:
            return 1
        else:
            fa = 1
            for i in range(1, y + 1):
                fa = fa * i
            return fa
    except Exception as ex:
        print(ex)


def main():
    x = int(input('x->'))
    print(factorial(x))


main()

