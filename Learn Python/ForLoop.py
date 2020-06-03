for a in range(5):  # 5 will not be included (0, 1, 2, 3, 4)
    print(a, "Shahzaib")


for number in range(10):
    print(number)


for number in range(1, 10):
    print(number)



for number in range(1, 10, 2):
    print(number)

    # 1
    # 3
    # 5
    # 7
    # 9


for number in range(10, 1, -2): # reverse
    print(number)

    # 10
    # 8
    # 6
    # 4
    # 2



cities = ['Karachi', 'Lahore', 'Islamabad']

for city in cities:
    print(f"The city under consideration is {city}")



for num in [11, 22, 33, 44, 55]:
    print(num)

    # 11
    # 22
    # 33
    # 44
    # 55



country = "Pakistan"

for char in country:
    print(char)

    # P
    # a
    # k
    # i
    # s
    # t
    # a
    # n


country = "Pakistan", "America"

for char in country:
    print(char)

    # Pakistan
    # America



#====================== for loop's break and continue ======================#


for number in range(10):
    if number % 3 == 1:
        break
    print(number) # reminder 0




for number in [5, 7, 11, 90]:
    if number % 2 == 0:
        break
    print(number)

    # 5
    # 7
    # 11


for number in range(10):
    if num == 7:
        continue
    print(num)


    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 8
    # 9





for number in range(10):
    if num == 7 or num == 4:
        continue
    print(num)


    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 8
    # 9