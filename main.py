

def max(x,y):
    try:
        if x > y:
            print(f"{x} Max")
        else:
            print(f"{y} Max")

    except Exception as ex:
        print(ex)
x=int(input("Enter numbers: "))
y=int(input())
print(max(x,y))



