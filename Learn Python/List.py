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

fruits.count("orange") # 2

fruits.index("cherry") # 5

fruits.clear() # all element clear




fruits["apple", "mango","orange", "banana", "cherry", "blueberry"]

fruits2 = fruits.copy() # by value

fruits["apple", "mango","orange", "banana", "cherry", "blueberry"]

fruits3 = fruits

fruits3["apple", "mango","orange", "banana", "cherry", "blueberry"]

fruits.append("newfruit")
fruits3["apple", "mango","orange", "banana", "cherry", "blueberry", "newfruit"]
fruits2["apple", "mango","orange", "banana", "cherry", "blueberry"]

# removing an item from a list {del, remove}

del fruits2[1]
fruits["apple", "orange", "banana", "cherry", "blueberry"]

fruits.remove("blueberry")
fruits["apple", "orange", "banana", "cherry",]




cities = ["Karachi", "Lahore", "Islamabad", "Quetta"]

poppedCity = cities.pop()

print(f"This city is popped from list {poppedCity}")
print(f"The remining cities are {cities}")

#This city is popped from list quetta
#The remining cities are ["Karachi", "Lahore", "Islamabad"]


poppedCity = cities.pop(2)
poppedCity # Islamabad


cities.sort()
cities = ["Islamabad", "Karachi", "Lahore", "Quetta"]


cities.sort(reverse = True)
cities = ["Quetta", "Lahore", "Karachi", "Islamabad"]


cities.reverse()
cities = ["Karachi", "Lahore", "Islamabad", "Quetta"]








