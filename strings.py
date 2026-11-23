#built in python string methods 

a = "This is a string"
print(a.upper()) # converts to uppercase
print(a.lower()) # converts to lowercase

b = "   Hello, World!   "
print(b.strip()) # removes whitespace from both ends
print(b.lstrip()) # removes whitespace from the left end
print(b.rstrip()) # removes whitespace from the right end


c = "   Meow, Woof, Quack   "
print(c.lstrip())
print(c.rstrip())

d = "Quak Quak"
print(d)
print("after replacing Q with D: " + d.replace("Q", "D")) # replaces Q with D

e = "Meow, Woof, Quack"
print(e.split(",")) #splits the string into a list

age = 36
#This will produce an error:
txt = f"My name is John, I am {age}"
print(txt)

#format strings
ab = 67
print(f"Dadus age was {ab}")
