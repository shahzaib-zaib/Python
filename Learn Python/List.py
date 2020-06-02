alist = ["Shahzaib", "Faizan", "Faisal"]
#index      0           1           2

alist[1] # Faizan


cities = ["Karachi", "Lahore", "Islamabad", "Quetta"]

cities[2] # Islamabad
len[cities] # 4




#================= Adding a member to the list =================#

fruits = []

fruits.append["apple"]
fruits.append["orange"] 

fruits ["apple", "orange"]

fruits.insert(1, "mango")

fruits["apple", "mango", "orange", "orange"]

fruits.extend(["banana", "cherry", "blueberry"])

fruits["apple", "mango", "orange","orange", "banana", "cherry", "blueberry"]




#================= Count and Index =================#

fruits.count("orange") # 2

fruits.index("cherry") # 5

fruits.clear() # all element clear




#================= Copy by value and Reference =================#

fruits["apple", "mango","orange", "banana", "cherry", "blueberry"]

fruits2 = fruits.copy() # by value

fruits2["apple", "mango","orange", "banana", "cherry", "blueberry"]

fruits3 = fruits # by reference

fruits3["apple", "mango","orange", "banana", "cherry", "blueberry"]

fruits.append("newfruit")
fruits3["apple", "mango","orange", "banana", "cherry", "blueberry", "newfruit"]
fruits2["apple", "mango","orange", "banana", "cherry", "blueberry"]




#================= Delete and Remove Value =================#

# removing an item from a list {del, remove}

del fruits2[1]
fruits["apple", "orange", "banana", "cherry", "blueberry"]

fruits.remove("blueberry")
fruits["apple", "orange", "banana", "cherry",]





#========================= Pop Values =========================#

cities = ["Karachi", "Lahore", "Islamabad", "Quetta"]

poppedCity = cities.pop()

print(f"This city is popped from list {poppedCity}")
print(f"The remining cities are {cities}")

#This city is popped from list quetta
#The remining cities are ["Karachi", "Lahore", "Islamabad"]


poppedCity = cities.pop(2)
poppedCity # Islamabad






#========================= Sort and Reverse Values ====================#

cities.sort()
cities = ["Islamabad", "Karachi", "Lahore", "Quetta"]


cities.sort(reverse = True)
cities = ["Quetta", "Lahore", "Karachi", "Islamabad"]


cities.reverse()
cities = ["Karachi", "Lahore", "Islamabad", "Quetta"]





#========================= Search and Find Values ====================#

cities = ["Karachi", "Lahore", "Islamabad", "Quetta"]

cities.index("Islamabad") # 2
cities.index("Multan") # no result




#========================= Slicing Values ====================#

arr = [1, 4, 2, 78, 45, 23, 89]

print(arr[1: 4]) # [4, 2, 78]

print(arr[-2: -1]) # [23]

print(arr[1: : 2]) # [4, 78, 23]



students = ["Ali", "Faisal", "Salman", "Hamza", "Kashif"]

students[3] # 'Hamza'



# index      -5       -4       -3        -2       -1
students = ["Ali", "Faisal", "Salman", "Hamza", "Kashif"]
# index       0        1        2          3        4

print(students[1])  # ['Faisal']
print(students[-4])  # ['Faisal']


# student[start : end + 1]
students[1 : 2] # ['Faisal']
students[1 : 3] # ['Faisal', 'Salman']



students[-4 : -2] # ['Faisal', 'Salman']

students[:] # ["Ali", "Faisal", "Salman", "Hamza", "Kashif"]
students[3:] # ["Hamza", "Kashif"]
students[:3] # ["Ali", "Faisal", "Salman"]

students[2 : -1] # ["Salman", "Hamza"]

students[2 : -5] # []



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

nums[0 : 16 : 1] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nums[0 : 16 : 2] # [1, 3, 5, 7, 9, 11, 13, 15]
nums[: : 5] # [1, 6, 11, 16]



