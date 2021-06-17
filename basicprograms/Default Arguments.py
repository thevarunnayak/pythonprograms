# Program to demonstrate default arguments in function

def calc(operand1=100,operand2=200,operator="+"):
    if operator == "+":
        return operand1+operand2
    elif operator == "-":
        return operand1-operand2
    elif operator in "*xX":
        return operand1*operand2
    elif operator == "/":
        return operand1/operand2
    elif operator == "\\":
        return operand1//operand2
    elif operator == "^":
        return operand1**operand2
    else:
        return "Invalid Operator"

print(calc()) #Calling calc function without any arguments
print(calc(1000)) #Calling calc function with one arguments
print(calc(1000,2000,"*")) #Calling calc function with 3 arguments