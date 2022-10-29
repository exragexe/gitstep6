
def user(x,y):
    try:
        for i in range(x):
            for j in range(y):
                if i == 0 or i == x - 1:
                    print("* ", end=" ")
                else:
                    if j == 0 or j == y - 1:
                        print("* ", end=" ")
                    else:
                        print("  ", end=" ")
            print()
    except Exception as ex:
        print(ex)




user(3,5)
