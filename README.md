## 1.0 Understanding Bits, Bytes, and Memory Allocation in Python Computation

1. **Difference Between Bit and Byte**

- **Bit (b)**: The smallest unit of data in a computer. It can be **0 or 1**.
- **Byte (B)**: A collection of **8 bits** (e.g., `10110110`).
    - 1 Byte = **8 Bits**
    - 1 Kilobyte (KB) = **1024 Bytes**
    - 1 Megabyte (MB) = **1024 KB**
    - 1 Gigabyte (GB) = **1024 MB**

2. **Memory Allocation in Python**

- Python ***dynamically allocates*** memory.
- Every object in Python consumes some memory based on its **type and size**.
- Larger data types consume more memory, and Python stores them in RAM.

3. Computation Example in Python

_Computation_ means processing data using the CPU, such as performing mathematical operations or logic-based tasks.

Let’s analyze a **basic function** and how memory allocation works during computation.

Example: Memory Usage in Computation

```
import sys

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

OUTPUT:

Memory used by num1: 28 bytes
Memory used by num2: 28 bytes
Memory used by sum_result: 28 bytes

```


### 1.1 How Computation Works Step by Step

1. **Variable Declaration:**
    
    - `num1 = 10` → Stored in memory.
    - `num2 = 20` → Stored in memory.
    - `sys.getsizeof(num1)` shows **how much memory Python allocates** for storing this integer.

2. **Function Execution (`add_numbers(num1, num2)`)**
    
    - The CPU **fetches** values `10` and `20` from memory.
    - Performs an **addition operation (`10 + 20 = 30`)** inside the CPU.
    - Stores the **result (`30`)** back in memory.
    - Returns `30` to `sum_result`.
    
3. **Memory Usage:**
    
    - Python integers are objects, so they take more memory than C/C++.
    - `sys.getsizeof(10)` → **28 bytes** (in Python 3.x).
    - Even a small number takes 28 bytes because Python stores additional metadata.
    - `sys.getsizeof(30)` shows how much memory is allocated for the result.

4. **Memory Allocation in a 32-bit vs. 64-bit System**

| Data Type       | 32-bit Python | 64-bit Python |
| --------------- | ------------- | ------------- |
| Integer (`int`) | 24 bytes      | 28 bytes      |
| Float (`float`) | 16 bytes      | 24 bytes      |
| List (Empty)    | 36 bytes      | 48 bytes      |

**64-bit Python allocates more memory** per object than 32-bit Python.
The difference comes from **pointers** (references to memory locations).


5. Understanding Computation in Simple Terms
	a. **Computation** is the process where the CPU **retrieves, processes, and stores data**.
	b. Example in Python:
	
```
x = 5
y = 10
z = x * y + 2

INTERPRETATION:

1. `x * y` → CPU fetches `5` and `10`, performs multiplication, **stores `50` in memory**.
2. `50 + 2` → CPU adds `2`, stores `52` in memory.
3. `z = 52` → Final result stored.

```

**Computation Process Summary**:

| Step | Action                             |
| ---- | ---------------------------------- |
| 1    | Retrieve `x` from RAM.             |
| 2    | Retrieve `y` from RAM.             |
| 3    | Multiply `x * y` in CPU registers. |
| 4    | Add `2` to result.                 |
| 5    | Store `z` in memory.               |
| 6    | Display output.                    |

### Summary

1. Bits represent data (0s and 1s).
2. Bytes group bits to store meaningful data.
3. Computations work by fetching data, processing it in the CPU, and storing results in memory.
4. Memory allocation varies in 32-bit vs. 64-bit Python.


## 2.0 How Python Handles Memory & Storage

When you run a Python script:

1. **num1 and num2 are stored in RAM** while the program is executing.
2. They exist only in memory (RAM) as long as the script is running.
3. **Once the script ends or VS Code is closed, the RAM is cleared**—and those variables no longer exist.

#### 2.1 RAM vs. Permanent Storage

| Memory Type                             | Stores Data When?                       | Data Persistence                             |
| --------------------------------------- | --------------------------------------- | -------------------------------------------- |
| RAM (Random Access Memory)              | While program is running                | Data is **lost** when program stops          |
| HDD/SSD (Hard Drive, Solid State Drive) | Manually saved (e.g., files, databases) | Data is **permanently stored** until deleted |

### 2.2 What Happens When You Close Python?

1. When you run `num1 = 10` in Python, it gets **allocated in RAM**.
2. When the script stops, RAM **frees up** and the variable is **gone**.
3. If you restart the script, Python **re-creates** the variable in RAM from scratch.

### 2.3 How to Store Data Permanently?

If you want to **keep the values even after the script closes**, you need to **save them to a file or database**.

Example: Save data to a file:
```
# Write to a file
with open("data.txt", "w") as file:
    file.write("num1 = 10\nnum2 = 20\n")

# Later, read from the file
with open("data.txt", "r") as file:
    print(file.read())  # This retrieves the saved data

```

Now, even if you **close Python or VS Code, the values are stored in `data.txt`**.

Example 2: Store Data in a Database

```
import sqlite3

conn = sqlite3.connect("numbers.db")  # Create or open a database
cursor = conn.cursor()

# Create a table if it doesn’t exist
cursor.execute("CREATE TABLE IF NOT EXISTS numbers (num1 INTEGER, num2 INTEGER)")

# Insert data
cursor.execute("INSERT INTO numbers VALUES (10, 20)")
conn.commit()

# Retrieve data
cursor.execute("SELECT * FROM numbers")
print(cursor.fetchall())

conn.close()

```

Now, the numbers are **permanently stored** in a database.

SUMMARY
1. **RAM stores temporary data only while the script runs**  
2. **Closing Python or VS Code clears all variables in RAM**  
3. **To store data permanently, save it to a file or database**

NOTE: This article has been taken from GPT.

## 3.0 How does python store data in variables? (gpt answer)

1. Python stores data in variables as ***objects.***
2. Each **variable** is essentially part of a ***higher-level object***. *Python variable is just a name that is temporarily associated with a higher-level object in memory.*
3. There are 2 types of objects:
	a. **Immutable Objects**
	b. **Mutable Objects**
4. **Immutable Objects:** If you change the value of an immutable object such as *Strings, Integers*, then python creates a ***new object*** to store the new value.
5. **Mutable Objects:** If you create a list and store it in a variable, it becomes an object of ***class list***. 
6. **Reference Count:** A reference count entails how many ***names*** refer or point to the ***initial object*** created that holds a specific value.

**Properties of an Object in Python:**

1. A **unique identity** value.  *This is the memory address where the object is stored.*
2. The ***low-level type*** that matches the hardware. 
3. The specific value (physical bits). 
4. A **reference count** of the number of variables that refer to it.

EXAMPLE

```
import sys

listA = ['Islamabad','Pakistan','Karachi', 100, 200]
print(f"Memory ID: {id(listA)} \n Reference Count: {sys.getrefcount(listA)}\nSize: {sys.getsizeof(listA)}")

OUTPUT:

Memory ID: 2583558530176
 Reference Count: 2
Size: 104
```
#### 3.1 What is a Reference Count?

1. A **Reference count** is a mechanism that is used to keep track of memory allocation and deallocation.
2. Every **object** in python has a reference count, which keeps track of the references pointing to that object.
3. When you ***create a new*** reference for an object, the reference count increase by 1.
4. When you ***delete a reference*** for the same object, the reference count decreases by 1.
5. Python interns small integers and strings, which belong to ***immutable objects category,*** because this helps to make memory allocation more ***efficient*** and ***optimized.***
6. **Reference Counts** starting point:
	a. Lists -> Begins from 2 if there is a single copy of the object in memory.
	b. String -> Begins from 4 if there is a single copy of the Object in memory.
	c. Integers -> Begins from 4 if there is a single copy of the object in memory, on the condition that the value is above 256. Any integer value below 256 will be cached and give a Higher Value as reference count.

#### 3.2 Reference count of integers between -5 and 256 and Strings (Immutable objects)

1. Python uses a technique called ***interning***.
2. ***Object Interning in Python:*** This is a memory optimization technique used in python where an ***immutable object*** is reused, instead of creating a ***new instance of that object.*** *This only happens when you reference an immutable object.*
	a. **String Interning:**
	b. **Integer Interning:**
3. **Does python INTERN Mutable Objects?**: *NO, python does not intern mutable objects because mutable objects can change all the time, therefore require a specific unique Memory ID for each object value, and also has a different reference count, unless the immutable object referencing holds the same values.*

Example:  Below is an example to show the reference point of an IMMUTABLE OBJECT holding values between the range of -5 and 256.

```
import sys

numOne = 40
print(f"\nReference count of numOne(40) -> {sys.getrefcount(numOne)}\nMemory ID-> {id(numOne)}")
numTwo = 70
print(f"Reference count of numOne(70) -> {sys.getrefcount(numTwo)}\nMemory ID-> {id(numTwo)}")
numThree = numTwo
print(f"Reference count of numThree=numTwo -> {sys.getrefcount(numThree)}\nMemory ID-> {id(numThree)}")

OUTPUT:

Reference count of numOne(40) -> 4294967295
Memory ID-> 140713838512264
Reference count of numOne(70) -> 4294967295
Memory ID-> 140713838513224
Reference count of numThree=numTwo -> 4294967295
Memory ID-> 140713838513224

INTERPRETATION:

1. numOne and numTwo reference counts are higher number because their object values are between the range of -5 to 256.
2. numOne and numTwo, both hold different Memory ID's, because they are both new objects created since their values are different.
3. numThree reference count also remains higher and the same as other objects because it too falls between the range of -5 and 256, since numThree is referenced to numTwo.
4. However, numThree holds the same Memory ID as numTwo because python has interned the value of numTwo which is 70, since they are both immutable objects and hold the same integer value, therefore python maintains a SINGLE copy of the integer.
```


4. Python ***interns, caches and reuses*** integer values of immutable objects that range between -5 and 256. This is why sometimes the reference count of such objects can be unreliable and may give you a unexpected higher value.
5. By ***interning objects***, Python can store only one copy of each distinct object in memory reducing memory consumption and speeding up operations that rely on object comparisons.


### 3.3 Integer Intern (Immutable Objects)

```
cA = 1000

print(sys.getrefcount(cA))

cB = 1000

print(f"cA Memory ID: {id(cA)}\ncB Memory ID: {id(cB)}\nREF COUNT cA: {sys.getrefcount(cA)}\nREF COUNT cB: {sys.getrefcount(cB)}")

cXA = 20

cXB = 20

print(f"cXA Memory ID: {id(cXA)}\ncXB Memory ID: {id(cXB)}\nREF COUNT cXA: {sys.getrefcount(cXA)}\nREF COUNT cXB: {sys.getrefcount(cXB)}")

OUTPUT:

4
cA Memory ID: 2928490041808
cB Memory ID: 2928490041808
REF COUNT cA: 5
REF COUNT cB: 5
cXA Memory ID: 140713768912392
cXB Memory ID: 140713768912392
REF COUNT cXA: 4294967295
REF COUNT cXB: 4294967295


```
### 3.4 String Intern (Immutable Objects)

```
bA = "Hello"

bB = "Hello"

bC = "Hello World"

print(f"\nMemory ID bA: {id(bA)}\nMemory ID bB: {id(bB)}\nMemory ID bC: {id(bC)}\n REF COUNT bA: {sys.getrefcount(bA)}\n REF COUNT bB: {sys.getrefcount(bB)}\n REF COUNT bC: {sys.getrefcount(bC)}")

OUTPUT:

Memory ID bA: 2928490384192
Memory ID bB: 2928490384192
Memory ID bC: 2928490366448
 REF COUNT bA: 5
 REF COUNT bB: 5
 REF COUNT bC: 4
```

### 3.5 Lists Memory & Ref count (Mutable Objects)

```
arrA = ['Karachi','Islamabad','Poland','Netherlands']
print(f"\nMemory ID arrA-> {id(arrA)}\nReference Count arrA -> {sys.getrefcount(arrA)}")
arrB = arrA
print(f"Memory of ID arrB=arrA -> {id(arrB)}\nMemoryID arrB -> {sys.getrefcount(arrB)}")
arrC = ['Ireland','Canada', 'Switzerland']
print(f"\nMemory ID arrC-> {id(arrC)}\nReference Count arrC -> {sys.getrefcount(arrC)}")

arrD = ['Karachi','Islamabad','Poland','Netherlands']
print(f"\narrD is a new list by assigning the same values of arrA \nMemory ID arrD -> {id(arrD)}\nReference Count arrD-> {sys.getrefcount(arrD)}")

OUTPUT:

Memory ID arrA-> 1584623721856
Reference Count arrA -> 2
Memory of ID arrB=arrA -> 1584623721856
MemoryID arrB -> 3

Memory ID arrC-> 1584623722112
Reference Count arrC -> 2
2 1584623721344
3 1584623722112 1584623722112

arrD is a new list by assigning the same values of arrA
Memory ID arrD -> 1855307193408
Reference Count arrD-> 2
```

### 3.6 Memory Address (id of the object)

1. **ID** is a ***unique memory address*** of an object.
2. The ID exists as long as an object exists, if the object is deleted, then the ID is also removed from memory.
3. If an object is ***Deleted*** or ***Reassigned***, then a new object may take over that ID, since a new ID is assigned to an object if it is Reassigned.
4. An ID of the same object is **changed** each time you run a Python Script.

Example

```
import sys

boxA = 'Pakistan'
print(f"Memory ID: {id(boxA)}")
boxA = 'America'
print(f"Memory ID (After reassigning new value): {id(boxA)}")

OUTPUT:
Memory ID: 1708450300272
Memory ID (After reassigning new value): 1708450316528

```
#### 3.7 Memory Size

1. The memory size can be determined using the function of sys, known as ***sys.getsizeof()***.
2. The output represents the memory allocated by python for that particular object in ***bytes.***
3. This includes **metadata** (internal structure) + **actual data stored** in the object.
4. An ***empty list*** `sys.getsizeof([])` returns **~88 bytes (or 56)** because an **empty list has internal structure** even before elements are added.
5. Lists store **references to objects, not actual values**

Example

```
import sys

listC: list = []
print(f"\nMemory Size of an empty list: {sys.getsizeof(listC)}")
listC = [100, 200, 400, 300, 900]
print(f"\nMemory size of a list with values: {sys.getsizeof(listC)}")

OUTPUT:

Memory Size of an empty list: 56
Memory size of a list with values: 104
```

#### 3.8 Why does the memory id change each time you run the python script?

1. **Script Execution Starts:**
	a. Python **allocates memory dynamically** for variables at runtime
	b. The **memory address (ID) is assigned to the object** (e.g., an integer or list).
2. **Variable Assignments:**
	a. When you assign `x = 10`, Python ***creates the object `10` in memory*** and assigns `x` to it.
	b. If another variable (`y = x`) refers to it, both share the ***same memory address*** during that execution.
3. **Script Finishes Execution:**
	a. Once the script completes, **Python releases memory back to the OS** (except for some cached objects like small integers).
	b. The memory previously occupied by objects is **deallocated**.
4. **Running the Script Again:**
	a. When you rerun the script, Python **allocates fresh memory locations** for the same variables.
	b. Even though the values remain the same (`x = 10`), their **memory addresses (IDs) may change** because ***Python dynamically manages memory allocation.***

#### Key Takeaways

1. **Yes, memory is allocated in RAM, which is temporary.**  
2. **Each execution is independent, so memory is reassigned.**  
3. **Small immutable objects (like `10, 20`) may be cached, but larger objects get new memory.**  
4. **References inside a running script remain stable, but between runs, they change.**

### 3.9 What is the difference between id() and getrefcount()?

1. `id()` Function
	a. Returns the **unique memory address (identity)** of an object.
	b. The ID remains the same as long as the object exists.
	c. If an object is deleted or reassigned, a new object might take that ID.

2. getrefcount() Function:
	a. Returns the **number of references** to an object.
	b. Each time a variable points to an object, its reference count increases.
	c. When reference count drops to **zero**, Python garbage collects the object.

SUMMARY:

| Feature            | id()                                                | sys.getrefcount()                                         |
| ------------------ | --------------------------------------------------- | --------------------------------------------------------- |
| Purpose            | Returns the memory address (identity) of an object. | Returns the number of references to an object.            |
| Type of Value      | Integer (memory address).                           | Integer (reference count).                                |
| Changes Over Time? | No, remains the same unless object is deleted.      | Yes, increases/decreases as references are added/removed. |
| Garbage Collection | No relation to garbage collection.                  | When count reaches zero, object is garbage collected.     |
| Usage              | Checking if two variables point to the same object. | Checking how many variables reference an object.          |


| Data Type                   | Object Type | Memory ID                                            | REF Count Base Value         | Reference Count                                                                                                                                                                                |
| --------------------------- | ----------- | ---------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| String                      | Immutable   | Unique \| Referenced variable will share the same ID | 2                            | Increases only if another variable is pointing to the Base string object. If the value of string is updated, then the ref count starts from the base again and Memory ID becomes unique again. |
| Integer (between -5 to 256) | Immutable   | Unique \| Referenced variable will share the same ID | Cached (Example: 4294967295) | Reference count remains the same as shown in the number of cached value.                                                                                                                       |
| Integer (256+)              | Immutable   | Unique \| Referenced variable will share the same ID | 4                            | Reference count begins from 4 unless if any other variable is pointing to it. Depending on the number of references, the count increases or decreases.                                         |
| List                        | Mutable     | Unique                                               | 2                            | Increases only if another variable is Referenced to it, otherwise remains the base value.                                                                                                      |

## 4.0 Memory Optimization Behavior in Python Script Vs REPL Interactive Mode

1. Python ***Memory Optimization*** behaves differently when python runs a program as a ***Script*** VS when it runs a python program in ***interactive mode***
2. Difference between ***Python Script*** VS ***Interactive*** Mode

	a. **Python Script:** A python script is run as a single execution process or is run an entire file as a *whole.* This can be achieved when you run a python file in `.py` extension format using the following command on your terminal `python script.py`
	
	b. **Interactive mode:** When you run python through an ***REPL (Read Eval Print Loop) Mode***. This can be acheived when you type `python + enter OR python3 + enter` on the terminal, the shell will become interactive python. *Which means that you can type any line of code on the terminal, and upon pressing enter, it will give you an output without using the Python keyword followed by the filename to run the script.*
	
3. What is **REPL?**
	a. **Read:** Python reads the user input (a command or expression).
	b. **Eval**: Python evaluates the expression or executes the statement.
	c. **Print:** The result is displayed to the user.
	d. **Loop:** The process repeats, allowing continuous interaction.
	
4. **Memory Optimization Behavior:** 

	a. **Python Script Mode:** If you have 2 different variables with the same integer value, even if it falls out of the range of -5 to 256, it will still ***intern*** the object value, because when a python file executes as a single process and as a whole at once, then it forces memory optimization where ever possible. *You can check this by using the keyword **is** to evaluate whether the memory ID is the Same or Different* . Thus, it returns ***False*** in python script.
	
	b. **Interactive mode:** If you run your script through Jupyter or Google Colab or by running your code statements on interactive python mode on your local system, it will avoid **Memory optimization**. It assumes the user might frequently modify objects, so it creates separate memory allocations to prevent unwanted optimizations. *Jupyter/Google Colab/Python interactive mode, all use the REPL strategy in executing the code, therefore when executing each statement line by line, it assigns each variable a new memory address.*

EXAMPLE RUNNING CODE THROUGH PYTHON SCRIPT

```
import sys

a = 100
b = 259
print(f"id of a-> {id(a)}\n refCount -> {sys.getrefcount(a)}")
print(f"id of b-> {id(b)}\n refCount -> {sys.getrefcount(b)}")
print(a is b)

print("\n-----x and y-----")
x = 200
y = 200
print(f"id of x-> {id(x)}\n refCount -> {sys.getrefcount(x)}")
print(f"id of y-> {id(y)}\n refCount -> {sys.getrefcount(y)}")
print(x is y)
print("\n----q and w-----")
q = 1000000
w = 1000000
sum = q + w
print(sum)

print(f"id of q-> {id(q)}\n refCount -> {sys.getrefcount(q)}")
print(f"id of w-> {id(w)}\n refCount -> {sys.getrefcount(w)}")
print(q is w)

print("\n----p and o-----")
p = 70
o = 100
print(f"id of p-> {id(p)}\n refCount -> {sys.getrefcount(p)}")
print(f"id of o-> {id(o)}\n refCount -> {sys.getrefcount(o)}")
print(p is o)

# STRING INTERNING

print('\n---------checking string-------')
strA = 'Pakistan'
strB = 'Pakistan'
print(strA == strB)
print(f'strA is strB -> {strA is strB}\nMemory id strA ->{id(strA)}\nMemory id strB ->{id(strB)}')
strC = "Swiss is of good quality"
strD = "Swiss is of good quality"
print(strC == strD)
print(f'strC is strD -> {strC is strD}\nMemory id strC ->{id(strC)}\nMemory id strD ->{id(strD)}')

OUTPUT:

id of a-> 140714199158792
 refCount -> 4294967295
id of b-> 2914695551472
 refCount -> 4
False

-----x and y-----
id of x-> 140714199161992
 refCount -> 4294967295
id of y-> 140714199161992
 refCount -> 4294967295
True

----q and w-----
2000000
id of q-> 2914698315376
 refCount -> 5
id of w-> 2914698315376
 refCount -> 5
True

----p and o-----
id of p-> 140714199157832
 refCount -> 4294967295
id of o-> 140714199158792
 refCount -> 4294967295
False

---------checking string-------
True

---------checking string-------
True
---------checking string-------
True
True
strA is strB -> True
Memory id strA ->2914698599280
Memory id strB ->2914698599280
True
strC is strD -> True
Memory id strC ->2914698443664
Memory id strD ->2914698443664
```

EXAMPLE RUNNING PYTHON THROUGH INTERACTIVE MODE(Google Colab + Jupyter)

```
import sys

a = 100
b = 259
print(f"id of a-> {id(a)}\n refCount -> {sys.getrefcount(a)}")
print(f"id of b-> {id(b)}\n refCount -> {sys.getrefcount(b)}")
print(a is b)

print("\n-----x and y-----")
x = 200
y = 200
print(f"id of x-> {id(x)}\n refCount -> {sys.getrefcount(x)}")
print(f"id of y-> {id(y)}\n refCount -> {sys.getrefcount(y)}")
print(x is y)
print("\n----q and w-----")
q = 1000000
w = 1000000
sum = q + w
print(sum)

print(f"id of q-> {id(q)}\n refCount -> {sys.getrefcount(q)}")
print(f"id of w-> {id(w)}\n refCount -> {sys.getrefcount(w)}")
print(q is w)

print("\n----p and o-----")
p = 70
o = 100
print(f"id of p-> {id(p)}\n refCount -> {sys.getrefcount(p)}")
print(f"id of o-> {id(o)}\n refCount -> {sys.getrefcount(o)}")
print(p is o)

# STRING INTERNING

print('\n---------checking string-------')
strA = 'Pakistan'
strB = 'Pakistan'
print(strA == strB)
print(f'strA is strB -> {strA is strB}\nMemory id strA ->{id(strA)}\nMemory id strB ->{id(strB)}')
strC = "Swiss is of good quality"
strD = "Swiss is of good quality"
print(strC == strD)
print(f'strC is strD -> {strC is strD}\nMemory id strC ->{id(strC)}\nMemory id strD ->{id(strD)}')

OUTPUT:

id of a-> 140714199158792 
refCount -> 4294967295 
id of b-> 1802703108592 
refCount -> 3 
False 
-----x and y----- 
id of x-> 140714199161992 
refCount -> 4294967295 
id of y-> 140714199161992 
refCount -> 4294967295 
True 
----q and w----- 
2000 
id of q-> 1802703107952 
refCount -> 3 
id of w-> 1802703108464 
refCount -> 3 
False 
----p and o----- 
id of p-> 140714199157832 
refCount -> 4294967295 i
d of o-> 140714199158792 
refCount -> 4294967295 
False 
---------checking string------- 
True 
strA is strB -> True 
Memory id strA ->1802704376624 
Memory id strB ->1802704376624 
True 
strC is strD -> False 
Memory id strC ->1802704312064 
Memory id strD ->1802704424592
```

6. **Differentiating between 'is' and == (Equality sign)**

	a. **is** => is used to evaluate and check whether both the values are stored in the same memory location, if yes, then output will be **true**, otherwise false.
	b. **Equality `==`**: This evaluates if the values of both the variables are the same, if yes, then the output will be true, otherwise false.

#### Why is Memory Optimization Important?

1. When a python program runs, it utilizes the memory of the RAM on your system to save data, evaluate and process it which gives us the output through the ***terminal.***
2. How much RAM is used is the task of Memory Optimization and Management, if your code utilizes minimum memory space to run the program file, it is said to be ***Memory Optimized or Memory efficient.*** Because if memory is utilized in an optimized manner, it makes your code and program efficient, it helps to process your program/code run faster using minimal memory resources.
3. This is where the concept of ***intern*** steps in, where python checks if there are multiple variables referenced to the same object, then it will store that particular object in a single memory block rather than assigning a new object and new memory address for the same Value of the object. *If the value of the object is similar, it is interned and other variables are referenced to the same object, making it more memory efficient.*
4. Python ***interns*** objects automatically as well as manually. To do it manually, you can import the `sys module` and use the `intern method` to intern an object value, which means that it will allocate a ***single memory address/block*** to that interned object and make other variables reference to that object. *When doing it automatically, it usually interns integers valued between the range of -5 to 256, and strings without space.*

#### SUMMARY OUTPUT OF CODE RUN AS SCRIPT VS INTERACTIVE MODE

| Criteria                             | Condition/Operation                      | Interactive Mode | Python Script |
| ------------------------------------ | ---------------------------------------- | ---------------- | ------------- |
| -5 to 256                            | is \| Both variables hold the same value | True             | True          |
| >256                                 | is \| Both variables hold the same value | True             | False         |
| Single Word in String                | is \| Both variables hold the same value | True             | True          |
| Multiple words with spaces in String | is \| Both variables hold the same value | True             | False         |
