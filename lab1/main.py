import random

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


# 3rd part of the task

random_list = random.sample(range(1, 100), 20)
print("List with random numbers: ", random_list)
even_list = []
for i in range(len(random_list)):
    if random_list[i] % 2 == 0:
        even_list.append(random_list[i])
print("List with even numbers: ", even_list)


