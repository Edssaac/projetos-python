# fahrenheit = input("What is the temperature in fahrenheit? ")

# if fahrenheit.isnumeric() == False:
#     print("Input is not a number.")
#     exit()

# celsius = (int(fahrenheit) - 32) * 5/9
# celsius = int(celsius)

# print ("Temperature in celsius is " + str(celsius))

print("Simple calculator!")

a = input("First number? ")
op = input("Operation? ")
b = input("Second number? ")

if a.isnumeric() == False or b.isnumeric() == False:
    print("Please input just numbers!")
    exit() 

a = int(a)
b = int(b)
if op == "+":
    resul = (a + b)     
elif op == "-":
    resul = (a - b) 
elif op == "*":
    resul = (a * b) 
elif op == "/":
    resul = (a / b)
elif op == "%":
    resul = (a % b) 
elif op == "**":
    resul = (a ** b)  
else:
    print("Operation not recognized.")
    exit()            

print("product of " + str(a), op, str(b) + " equals " + str(resul))