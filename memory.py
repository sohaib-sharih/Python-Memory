import sys, time, dis

# Mutable Objects and practice for determining the size allocated in memory for each object.
print(f"\n-----determining SIZE----")


def add_numbers(a, b):
    result = a + b
    return result

# Define two numbers
num1 = 10
num2 = 20

# Function call
sum_result = add_numbers(num1, num2)

# Checking memory usage
print("Memory used by num1:", sys.getsizeof(num1), "bytes")
print("Memory used by num2:", sys.getsizeof(num2), "bytes")
print("Memory used by sum_result:", sys.getsizeof(sum_result), "bytes")

listA = ['Islamabad','Pakistan','Karachi', 100, 200]
print(f"Memory ID: {id(listA)} \n Reference Count: {sys.getrefcount(listA)}\nSize: {sys.getsizeof(listA)}")
listA.append("England")
print(f"\nAppended England in listA \nMemory ID: {id(listA)} \n Reference Count: {sys.getrefcount(listA)}\nSize: {sys.getsizeof(listA)}")
listB = listA
print(f"listB referring to listA \nMemory ID: {id(listA)} \n Reference Count: {sys.getrefcount(listA)}\nSize: {sys.getsizeof(listA)}")
del listB
print(f"\n Deleted listB \nMemory id of listA: {id(listA)}\nReference Count of listA: {sys.getrefcount(listA)}")
print(type(listA))

print(f"ID: {id(listA)}\nSize: {sys.getsizeof(listA)}\nReference Count: {sys.getrefcount(listA)}\nType: {type(listA)}")

# Reassigning a value of an object and its address
print(f"\n ----------Reassigning a value of an object and its impact on memory ID + Reference Count-------")
boxA = 'Pakistan'
print(f"Memory ID: {id(boxA)}\nReference Count: BoxA-> {sys.getrefcount(boxA)}")
boxA = 'America'
print(f"Memory ID (After reassigning new value): {id(boxA)}\nReference Count: BoxA-> {sys.getrefcount(boxA)}")

# Size of an empty object VS an object with values
print(f"\n -----Size of an Empty object VS an object that holds values ------")
listC: list = []
print(f"\nMemory Size of an empty list: {sys.getsizeof(listC)}")
listC = [100, 200, 400, 300, 900]
print(f"\nMemory size of a list with values: {sys.getsizeof(listC)}")

# Reference count for numbers less than 256
print(f"--------------Reference count for numbers less than 256-------------")
numOne = 40
print(f"\nReference count of numOne(40) -> {sys.getrefcount(numOne)}\nMemory ID-> {id(numOne)}")
numTwo = 70
print(f"Reference count of numOne(70) -> {sys.getrefcount(numTwo)}\nMemory ID-> {id(numTwo)}")
numThree = numTwo
print(f"Reference count of numThree=numTwo -> {sys.getrefcount(numThree)}\nMemory ID-> {id(numThree)}")

# Starting Reference Count of String, List, Integer> 256
newFour = "America"
print(f"string -> {sys.getrefcount(newFour)}\nMemory ID-> {id(newFour)}")
newFourA = newFour
print(f"Refering to newFour -> {sys.getrefcount(newFourA)}\nMemory ID-> {id(newFourA)}")
newFive = ["karachi",'islamabad']

print(f"List -> {sys.getrefcount(newFive)}\nMemory ID-> {id(newFive)}")
newSix = 999
print(f"Integer (999) -> {sys.getrefcount(newSix)}")

# intern reference count, memory optimization for a string
print(f"----Example how Python Interns a value to be reused efficiently------")
strA = sys.intern("Rose")
print(f"value of strA: -> {strA}")
print(f"Ref count of strA:-> {sys.getrefcount(strA)}")
strB = "Rose"
print(f"Ref Count of strA -> {sys.getrefcount(strB)}")
strC = "Rose"
print(f"Ref count of strA -> {sys.getrefcount(strC)}")

# INTEGER INTERNING- IMMUTABLE OBJECT (Each example of the range -5 to 256, and an integer above the range)
print("-----------Integers Intern-------------")
cA = 1000
print(sys.getrefcount(cA))
cB = 1000
print(f"cA Memory ID: {id(cA)}\ncB Memory ID: {id(cB)}\nREF COUNT cA: {sys.getrefcount(cA)}\nREF COUNT cB: {sys.getrefcount(cB)}")

cXA = 20
cXB = 20
print(f"cXA Memory ID: {id(cXA)}\ncXB Memory ID: {id(cXB)}\nREF COUNT cXA: {sys.getrefcount(cXA)}\nREF COUNT cXB: {sys.getrefcount(cXB)}")

#STRING INTERNING (IMMUTABLE OBJECT)

bA = "Hello"
bB = "Hello"
bC = "Hello World"
print(f"\nMemory ID bA: {id(bA)}\nMemory ID bB: {id(bB)}\nMemory ID bC: {id(bC)}\n REF COUNT bA: {sys.getrefcount(bA)}\n REF COUNT bB: {sys.getrefcount(bB)}\n REF COUNT bC: {sys.getrefcount(bC)}")

# MUTABLE OBJECT INTERNING (LISTS)
print(f"\n---------Mutable Object Example LISTS------------")

arrA = ['Karachi','Islamabad','Poland','Netherlands']
print(f"\nMemory ID arrA-> {id(arrA)}\nReference Count arrA -> {sys.getrefcount(arrA)}")
arrB = arrA
print(f"Memory of ID arrB=arrA -> {id(arrB)}\nMemoryID arrB -> {sys.getrefcount(arrB)}")
arrC = ['Ireland','Canada', 'Switzerland']
print(f"\nMemory ID arrC-> {id(arrC)}\nReference Count arrC -> {sys.getrefcount(arrC)}")

arrD = ['Karachi','Islamabad','Poland','Netherlands']
print(f"\narrD is a new list by assigning the same values of arrA \nMemory ID arrD -> {id(arrD)}\nReference Count arrD-> {sys.getrefcount(arrD)}")

# REFERENCE COUNT STARTING POINT of an MUTABLE OBJECT List
print(f"-------------")
strD = "Canada"
print(sys.getrefcount(strD), id(strD))
strE = strD
print(sys.getrefcount(strE), id(strE))
strD = "Mexico"
print(sys.getrefcount(strD), id(strD))
strF = "Africa"
print(sys.getrefcount(strF))
strG = strF
print(sys.getrefcount(strF))


# Example code for deriving time.
result = time.localtime()
print(result, "%S")
print(f"type of result: {type(result)}")
print(result.tm_sec)
timeString = time.strftime("%S %D %d")

print(timeString)
#---------------------------------

# bytecode
def greetA():
    return "Hi, how are you"

dis.dis(greetA)


