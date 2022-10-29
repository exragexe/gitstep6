

def truu(x):
    try:
        if x > 0:
            return "true"
        else:
            return "false"

    except Exception as ex:
        print(ex)
x=int(input("Enter numbers: "))
print(truu(x))