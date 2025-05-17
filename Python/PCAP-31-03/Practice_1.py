#####################################################
######### Practice for python certification #########
#####################################################

# Q1: How would you use the map() function to square each element in a list?
print("\nQ1: How would you use the map() function to square each element in a list?\n")
# map(lambda x: x**2,list)
print("R1: map(lambda x: x**2,list)\n")
print("\n____EXPLANATION BELLOW____\n")
print("Using map() we can apply a function to each item in an iterable\n")
print("lambda <NAMEFUNTION> is required to declare inline functionality without declaring a function\n")
# //___________________________________________________________________________________________________

# Q2: What is the output of not (True and False)
print("\nQ2: What is the output of not (True and False)\n")
print("R2: True\n")
print("\n____EXPLANATION BELLOW____\n")
print("not(True and False = False) = True\n")
# //___________________________________________________________________________________________________

# Q3: What is the output of this function call: def subtract(a,b=5): return a-b when substract(7)
def substract(a,b=5):
    return a-b
print("R3: The value resulting is 2\n")
# //___________________________________________________________________________________________________

# Q4: What is the result of the dictionary comprehension d={i:str(i) for i in range(3)}
print("\nQ4: What is the result of the dictionary comprehension d=(i:str(i) for i in range(3))\n")
# d={i:str(i) for i in range(3)}
print("R4: d=(0:0,1:1,2:2)\n")
print("\n____EXPLANATION BELLOW____\n")
print("This is a comprehension. Its the same as for i in range(3): d=(i:str(i))\n")
print("Comprehension is used to concise syntax for creating collections (list, dictionaries, sets)\n")
# Regular loop
d = []
for i in range(100):
    d.append(i)
print(d)
# Comprehension
print("Same result as:")
y = [i for i in range(100)]
print(y)
# //___________________________________________________________________________________________________

# Q5: What is the purpose of garbage collection(GC) in Python?
print("\nQ5: What is the purpose of garbage collection(GC) in Python?\n")
print("R5: Free up memory by removing objects that are no longer in use\n")
# import gc
# gc.collect
# gc.delete
print("\n____EXPLANATION BELLOW____\n")
print(" Python stores all the values as objects in memory. If objects are constantly created without freeing the memory we run out of RAM\n")
print(" If no values or container refer to the object, the reference(pointer) count drops to 0 and python automatically deletes it")
# //___________________________________________________________________________________________________

# Q6: What is the purpose of tell() method?
print("\nQ6: What is the purpose of tell() method?\n")
print("R6: tell() is used when working with files. It gets the file pointer of the file you are at\n")
# with open("example.txt", "r") as file:
#   file.read(5)    first 5 character
#   pos = file.tell()   get current position
#   print("Current position: ", pos)
# //___________________________________________________________________________________________________

# Q7: What happens if a function is defined with default argument and you pass a value for that argument?
print("\nQ7: What happens if a function is defined with default argument and you pass a value for that argument?\n")
print("R7: The default value is ignored\n")
def printvalor(b=5):
    print("B", b)
#printvalor("Esto es un string")
# //___________________________________________________________________________________________________

# Q8: How do you define a static method in a class?
print("\nQ8: How do you define a static method in a class?\n")
print(" R8: @staticmethod def greet(name) \n")
print("\n____EXPLANATION BELLOW____\n")
print(" @staticmethod is like a function but it lives inside the class but doesnot receive a self as argument\n")
# //___________________________________________________________________________________________________

# Q9: What is the result of the following dictionary comprehension ? d = (i:i+1 for i in range(5))
print("\nQ9: What is the result of the following dictionary comprehension ? d = (i:i+1 for i in range(5))\n")
print("R9: The result is d = (0:1,1:2,2:3,3:4)\n")
d = {i:i+1 for i in range(5)}
#print("d",d)
# //___________________________________________________________________________________________________

# Q10: What will happen if you execute the following code: def test(): raise Exception("Custom error")
print("\nQ10: What will happen if you execute the following code: def test(): raise Exception(Custom error)\n")
print("R10: Program raise an exceptiona and shows Custom error message\n")
def test():
    print("Parte 1 de 4")
    print("Parte 2 de 4")
    print("Parte 3 de 4")
    raise Exception("Custom error")
    print("Parte 3 de 4")
#test()
print("\n____EXPLANATION BELLOW____\n")
print(" raise immediately stops execution. Its a manually trigger for an error\n")
print(" Exception(custom msg) creates and exception object with the msg\n")
# //___________________________________________________________________________________________________

# Q11: What happens when you try to use the seek() method on a file that is opened in append mode(a)?
print("\nQ11: What happens when you try to use the seek() method on a file that is opened in append mode(a)?\n")
print("R11: The file pointer is ignored and writes always occu at the end of the file\n")
print("\n____EXPLANATION BELLOW____\n")
print(" seek(number_of_bytes,from the begginig or the current position or at the end) is used to change the position of the file pointer in a file\n")
# //___________________________________________________________________________________________________

# Q12: How do you define a class method 
print("\nQ12: How do you define a class method\n")
print("\nR12: To create a class method is defined by using @classmethod decorator and taking the class as first argument\n")
print("\n____EXPLANATION BELLOW____\n")
print(" Can access and modify the class state using cls parameter. Belog to the class rather than the instance\n")
class Person:
    species = "HUMAN" # Class atribute(shared by all instances)
    def __init__(self, name):
        self.name = name    #instance atributes
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

#p1 = Person("Alice")
#p2 = Person("Bob")

#print(p1.species)  # Human
#print(p2.species)  # Human

#Person.change_species("Cyborg")  # Change class attribute via class method

#print(p1.species)  # Cyborg
#print(p2.species)  # Cyborg
# //___________________________________________________________________________________________________

# Q13: What will be the output of the following code ? for i in range(2): print(i*2)
print("\nQ13: What will be the output of the following code ? for i in range(2): print(i*2)\n")
print("\nR13: (0,2)\n")
# //___________________________________________________________________________________________________

# Q14: What will the following code print? recursive_lambda=(lambda x: x if x == 0 else x + recursive_lambda(x-1)(5))
print("\nQ14: What will the following code print? recursive_lambda=(lambda x: x if x == 0 else x + recursive_lambda(x-1)(5))\n")
print("\nR14: 15\n")
#recursive_lambda=(lambda x: x if x == 0 else x + recursive_lambda(x-1))
#y=5
#print(recursive_lambda(y))
print("\n____EXPLANATION BELLOW____\n")
print(" Written as a not comprehended is easier to understand. Take a look at code\n")
def anom_fun(x):
    if x == 0:
        return 0
    else: 
        return x + anom_fun(x-1)
#print(anom_fun(5))
# //___________________________________________________________________________________________________

# Q15: What is the output of this code: for i in range(2,10,3): print(i)
print("\nQ15: What is the output of this code: for i in range(2,10,3): print(i)")
print("\nR15: (2,5,8)\n")
print("\n____EXPLANATION BELLOW____\n")
print(" Format is range(star,stop,step)")
# //___________________________________________________________________________________________________

# Q16: What is the output of this code: for i in range(2,10,3): print(i)
print("\nQ16: What is the output of this code: x = [1,2,3]; x[0]=4 print(x)")
print("\nR16: x=[4,2,3]\n")
print("\n____EXPLANATION BELLOW____\n")
print(" Acces to index[0:START] and write the value ")
# //___________________________________________________________________________________________________

# Q17: What is the purpose of inheritance
print("\nQ17: What is the purpose of inheritance")
print("\nR17: To allow methods and attributes to be inherited from other class\n")
# //___________________________________________________________________________________________________

# Q18: What will be the output list(map(lambda x:x+5,[1,2,3]))
print("\nQ18: What will be the output list(map(lambda x:x+5,[1,2,3]))")
print("\nR18: list = [6,7,8]\n")
# //___________________________________________________________________________________________________

# Q19: What is the output of the following code: for i in [1,2,3,4]: print(i**2)
print("\nQ19: What is the output of the following code: for i in [1,2,3,4]: print(i**2)")
print("\nR19: (1,4,9,16)\n")
# //___________________________________________________________________________________________________

# Q20: Which of the following is the correct syntax for using the filter() function
print("\nQ20: Which of the following is the correct syntax for using the filter() function")
print("\nR20: filter(function(True or False),iterable(collection))")
print("\n____EXPLANATION BELLOW____\n")
print(" Take a look at code\n")
numbers = [1, 2, 3, 4, 5, 6]
# Function to check even numbers
def is_even(x):
    return x % 2 == 0

#even_numbers = list(filter(is_even, numbers))
#print(even_numbers)  # Output: [2, 4, 6]
# //___________________________________________________________________________________________________

# Q21: What will be the output of print("Hello","Word")
print("\nQ21: What will be the output of print(Hello,Word)")
print("\nR21: Hello Word")
# //___________________________________________________________________________________________________

# Q22: What happens if there is no matching except block for an exception raised in the try block
print("\nQ22: What happens if there is no matching except block for an exception raised in the try block")
print("\nR22: The exception is propagated to higher levels")
print("\n____EXPLANATION BELLOW____\n")
print(" If not matching except block is found, the exception is propagated up the call stack\n")
# //___________________________________________________________________________________________________

# Q23: What is the output of the following code? def factorial(n): return 1 if n == 0 else n*factorial(n-1); print(factorial(4))
print("\nQ23: What is the output of the following code? def factorial(n): return 1 if n == 0 else n*factorial(n-1); print(factorial(4))")
print("\nR23: Its a recursive function. Factorial 4= 4*3*2*1")
# //___________________________________________________________________________________________________

# Q24: Which function from the sys module is used to get command line arguments passed to a python script
print("\nQ24: Which function from the sys module is used to get command line arguments passed to a python script")
print("\nR24: sys.arg")
print("\n____EXPLANATION BELLOW____\n")
print(" sys is a list provided by sys module that contains the command-line arguments\n")
# //___________________________________________________________________________________________________

# Q25: How many arguments __init__ method receive by default?
print("\nQ25: How many arguments __init__ method receive by default?")
print("\nR25: Default receives only 1: selft which is the instance of the class")
# //___________________________________________________________________________________________________

# Q26: What is the correct way to terminate a while loop early
print("\nQ26: What is the correct way to terminate a while loop early")
print("\nR26: Using th command: break")
# //___________________________________________________________________________________________________

# Q27: What is the purpose of using lambda functions?
print("\nQ27: What is the purpose of using lambda functions?")
print("\nR27: to define anonymous function that can be used inline")
# //___________________________________________________________________________________________________

# Q28: Which mode allows you to both read and write a file?
print("\nQ28: Which mode allows you to both read and write a file?")
print("\nR28: The command should be a with open(txt,r+) as file:. If file doesnt exist, raises FileNotFoundError")
# //___________________________________________________________________________________________________

# Q29: What is the correct syntax for an if statement in python?
print("\nQ29: What is the correct syntax for an if statement in python?")
print("\nR29: if: statement else: statemetn")
# //___________________________________________________________________________________________________

# Q30: What does the StopIteration exception indicate in the context of iterators and generators
print("\nQ30: What does the StopIteration exception indicate in the context of iterators and generators")
print("\nR30: The iterator has reached the end of the sequence")
print("\n____EXPLANATION BELLOW____\n")
print(" The iterator or generator has no more items to return\n")
my_list = [1,2,3]
# Iter() build in function that creates an iterator for an iterable
# my_list = is an iterator object. remembers current position and gives the next when asked
my_list = iter(my_list)
# next() retrive the next item from the iterator

#print(next(my_list))
#print(next(my_list))
#print(next(my_list))
#print(next(my_list)) # StopIteration
# //___________________________________________________________________________________________________

# Q31: How can you define a function that takes a variable number of arguments
print("\nQ31: How can ou define a function that takes a variable number of arguments")
print("\nR31: Use def funct(*arg), *arg indicates any number of positional arguments")
print("\n____EXPLANATION BELLOW____\n")
print(" Take a look at the code. greet_all(*names)\n")
def greet_all(*names):
    for name in names:
        print(f"Hola, {name}!")
#greet_all("Luis","Pedro","Carlos")
# //___________________________________________________________________________________________________

# Q32: What is the purpose of the self keyword in a class
print("\nQ32: What is the purpose of the self keyword in a class")
print("\nR32: To refer to current object")
# //___________________________________________________________________________________________________

# Q33: Can an instance method access both instance and class attributes?
print("\nQ33: Can an instance method access both instance and class attributes?")
print("\nR33: YEs, it can access to both.")
# //___________________________________________________________________________________________________

# Q34: What is the result of str(10.5) + "is a float"
print("\nQ34: What is the result of str(10.5) + is a float")
print("\nR34: 10.5 is a float")
# //___________________________________________________________________________________________________

# Q35: What is the result of of using a single underscore(_) before an attribute in python
print("\nQ35: What is the result of of using a single underscore(_) before an attribute in python")
print("\nR35: The attribute is considered protected and intended for internal use")
print("\n____EXPLANATION BELLOW____\n")
print(" Its considered an atribute to treat private for internal use only\n")
print(" Take a look at code to see an example\n")
class person:
    def __init__(self,name):
        self.name=name
        self._secret="For private and internal use"

# Q36: How does Python's garbage collector identify objects that need to be destroyed?
print("\nQ36: How does Python's garbage collector identify objects that need to be destroyed?")
print("\nR36: By tracking the reference count of the object")
# //___________________________________________________________________________________________________

# Q37: How can you ensure that an external file is closed after reading in Python
print("\nQ37: How can you ensure that an external file is closed after reading in Python")
print("\nR37: Using open() as file")
print("\n____EXPLANATION BELLOW____\n")
print(" Using with open() as file: we ensure automatically closing of the file even if an exception is raised\n")
# //___________________________________________________________________________________________________

# Q38: What happens when an object is no longer referenced in python?
print("\nQ38: What happens when an object is no longer referenced in python?")
print("\nR38: The object is marked for garbage collection")
# //___________________________________________________________________________________________________

# Q39: What will be the outcome of opening a file using open("file.txt","a"))
print("\nQ39: What will be the outcome of opening a file using open(file.txt,a))")
print("\nR39: It will append the data to the end of the file")
# //___________________________________________________________________________________________________

# Q40: What is the output of the following code: i in "abcde":print(i.upper())
print("\nQ40: What is the output of the following code: i in abcde:print(i.upper())")
print("\nR40: A B C D E")
#for i in "abcde": print(i.upper())