# 1st part of the task

print("Hello world")


# 2nd part of the task
def calculation(num1, num2, op):
    if op == "add":
        return num1 + num2
    elif op == "sub":
        return num1 - num2
    elif op == "mult":
        return num1 * num2
    elif op == "div":
        return num1 / num2


while True:
    try:
        print()
        a = float(str(input("Enter 1st number: ")))
        try:
            b = float(str(input("Enter 2nd number: ")))
            operator = input("Enter math command(add, sub, mult, div): ")
            if str(operator) == "add" or str(operator) == "sub" or str(operator) == "mult" or str(operator) == "div":
                print("The result: " + str(calculation(a, b, operator)), "\n")
                break
            else:
                print("Error!Wrong input!")
                continue
        except ValueError:
            print("Error!Wrong input!")
            continue
    except ValueError:
        print("Error!Wrong input!")
        continue

