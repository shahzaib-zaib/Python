# myDict = {key:value, key:value, key:value}

myDict = {"name":"Shahzaib", "age":30, "gender": "Male"}

len(myDict) # 3

# Adding a new key to an exiting Dictionary

myDict["email"] = "shahzaibux@gmail.com"

myDict # {"name":"Shahzaib", "age":30, "gender": "Male", "email":"shahzaibux@gmail.com"}



#=================== Access a key value ===================#

myDict["age"] # 30
myDict["email"] # "shahzaibux@gmail.com"
myDict["name"] # "Shahzaib"



newDict = {1:"Faizan", 2:"Saad"}
newDict[1] # "Faizan"
newDict[2] # "Saad"




#===================== Deleting a key =====================#

del newDict[2] # "Saad"





#===================== Updating a key value =====================#

myDict = {"name":"Shahzaib", "age":30, "gender": "Male", "email":"shahzaibux@gmail.com"}

myDict["email"] = "shahzaib@gmail.com" 

# {"name":"Shahzaib", "age":30, "gender": "Male", "email":"shahzaib@gmail.com"}


aDict = {1:100, 2:200, 3:300, 4:400, 1:1000}

# {1:1000, 2:200, 3:300, 4:400}

1 in aDict # True


"age" in myDict # True