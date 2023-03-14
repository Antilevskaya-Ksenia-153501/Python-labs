import random

# 1st part of the task

print("Hello world")


# 2nd part of the task

addOp, subOp, multOp, divOp = "add", "sub", "mult", "div"


def calculation(num1, num2, op):
    if op == addOp:
        return num1 + num2
    elif op == subOp:
        return num1 - num2
    elif op == multOp:
        return num1 * num2
    elif op == divOp:
        return num1 / num2


while True:
    try:
        print()
        a = float(str(input("Enter 1st number: ")))
        try:
            b = float(str(input("Enter 2nd number: ")))
            operator = input("Enter math command(add, sub, mult, div): ")
            if str(operator) == addOp or str(operator) == subOp or str(operator) == multOp or str(operator) == divOp:
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


# 3rd part of the task

random_list = random.sample(range(1, 100), 20)
print("List with random numbers: ", random_list)
even_list = []
for i in range(len(random_list)):
    if random_list[i] % 2 == 0:
        even_list.append(random_list[i])
print("List with even numbers: ", even_list)
