# operators { + , - , * , / }

print(23 + 34) # 57

a = 23
b = 34
c = a + b
print(c) # 57


value1 = 100
value2 = 10.5

sum = value2 - value1
print(sum) # -89.5


value1 = 100
value2 = 100

sum = value2 / value1  # python by default floating point division
print(sum) # 1.0


value1 = 100
value2 = 100

sum = value2 // value1  # integer division
print(sum) # 1


value1 = 100
value2 = 200

sum = value1 // value2  # integer division
# 0.5
print(sum) # 0


# in string + is not additional but it is concatenation

a = "23"
b = "45"
print(a + b) # 2345