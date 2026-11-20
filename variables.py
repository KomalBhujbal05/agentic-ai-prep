#variables get created once we set a value to them. Unlike other programming languages, we do not need to declare their type. The interpreter will decide the type of variable based on the value we assign to it.
x =5
print(x)
print(type(x))
"""we can even change the type of variable by 
assigning a value of different type to it."""
x="Hello"
print(x)
print(type(x))


#if we want to particulary assign a type we can do it with casting
d = float(5)
print(d)
print(type(d))
d=int(5.7)
print(d)

#String
String = "Hello"
print(String)

#assign multiple values
a,b,c = 4, "MY CODE", 9.0
print(a,b,c)

#one value to multiple variables
x=y=z=10

#unpacking a collection
fruits = ["apple", "banana", "cherry"]
a,b,c = fruits
print(a)
print(b)
print(c)

#global vs local variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#how to create global var inside a function
def fun2():
    global y
    y =45
    
fun2()
print(y)
