def add(n1,n2):
    return n1+n2

def subs(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subs,
    "*": multi,
    "/":divide
}

should_continue = True 

num_dict = {"L_num" : None}
new_input = True

while should_continue:
    while new_input == True:
        n1 = int(input("Enter the first number: "))
        num_dict["L_num"] = n1
        break
    op = input("Enter the operator: \n + \n - \n * \n / \n")
    n2 = int(input("Enter the second number: "))

    print(f"The answer is {operations[op](num_dict['L_num'],n2)}")

    same_continue = input(f"Type 'y' to continue calculating with {operations[op](num_dict['L_num'],n2)}, or type anything else to start a new calculation: ")

    if same_continue == "y":
        num_dict["L_num"] = operations[op](num_dict['L_num'],n2)
        new_input = False
    else:
        num_dict["L_num"] = None
        new_input = True





