# x = int(input("aqui: "))
# y = 0

# for i in range(1, x+1):
#     if x % i == 0:
#         y += 1

# if y == 2:
#     print("primo") 
# else:
#     print("não primo")

x = [1, 2, 3, 4 ,5 ,6 ,7 ,8, 9, 13]
z = x[1]
y = 0

for c in range(0, len(x)):
    z = x[c]
    y = 0
    print(z)
    for i in range(1, z+1):
        if z % i == 0:
            y += 1

    if y == 2:
        print("primo") 
    else:
        print("não primo")
