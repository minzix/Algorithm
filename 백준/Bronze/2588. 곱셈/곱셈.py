num1 = input()
num2 = input()

a = num2[0]
b = num2[1]
c = num2[2]

third = int(num1) * int(c)
fourth = int(num1) * int(b)
fifth = int(num1) * int(a)
sixth = int(third) + int(fourth)*10 + int(fifth)*100

print(third)
print(fourth)
print(fifth)
print(sixth)