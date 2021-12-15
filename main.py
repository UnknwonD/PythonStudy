##                   Varibles
#Naming like a_... is called Snake case 
#An implicit promise for very long naming in Python
#all of thing should be named in small letter with '-' besides words
a_int = 3 
a_float = 2.041
a_string = "like this"
a_bloolean = True # Capital Letter differ from JS (true x, True, False)
a_none = None # Something like null in Java Script

print(type(a_none))


##                  Sequece Type
#  1. list ( Mutable )

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print("Mon" in days)  # True
print(days[2])  # Wed
print(len(days)) # 5

days.append("Sat")
print(days)

days.reverse()
print(days)

#  2. Tuples ( Immutable )

days_t = ("Mon", "Tue", "Wed", "Thu", "Fri")

#  3. Dictionary ( Key with Value )

daeho = {
  "name" : "Daeho",
  "age" : 22,
  "korean" : True,
  "Fav_Food" : ["Ramen", "Kimchi"]
}

print(daeho)
daeho["handsome"] = True

print(daeho)


##                    Fuction
# 1. Built in Function

print("Hello")
print(type(daeho))

age = "18"
print(type(age))
n_age = int(age)
print(type(n_age))

# 2. Built in Function
# Function in Python can be recognized by indentation ( One Tab )

# 3.1 Positional Argument
# We can set the default argument by '=' operator

def say_hello(who="nothing") :
  print("hello", who) 

say_hello("daeho")
say_hello()

#if function return something, that Fucntion should be shut down
#Only one function one return

def plus(a=0, b=0) :
  return a+b
  print(a, "+", b, "=", a+b)

print(plus(1, 5))
print(plus())

# 3.2 Keyword Argument
#If too many argument are in function, Keyword Argument is better than Positional

print(plus(b=5000, a=100))

def call(name, age) :
  print(f"Hello {name} you are {age} years old") #format
  return "Hello" + name + "you are" + age + "years old"

call(age="12", name="LeeDaeHo")

##                    Conditioanl Part One
# 1. If - else ==============================================
#   <, >, <=, >=, ==, !=,   ->  greater than, equal ...
#   & (and), | (or), ^ (exclusive or ?) 
# -----------------------------------------------------------
#   is, is not              ->  object identity
#   and, or, not            ->  Boolean Operator

def plus_(a, b) :
  if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
    return a + b
  else :
    return None

a = float(input("a : "))
b = float(input("b : "))

print(plus(a, b))

# 2. elif
# else if = elif
# cannot use both of all ( else if, elif only one grammar )

def age_check(age) :
  print(f"your age is {age}")

  if age < 19 :
    print("you can't drink")
  elif age == 19 :
    print("you are new to this")
  else :
    print("you can drink")

##                   Loop Conditional
# 1. for in ====================================

days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for day in days:
  if day == "Wed":
    break
  else :
    print(day)

for letter in "Daeho" :
  print(letter)

  ##                   Module
  # Python has so many modules for more convenient programming
  # for example, math, numpy, tensorflow

from math import ceil, fsum

print(ceil(2.1))
print(fsum([1, 2, 3, 4, 5, 6, 7]))

# if want to import all of module, 
#     import [module name]
# else if you wanna import specific fuction in module, 
#     from [module name] import [function name]
# and you can name the fuction or module
#     by using "as" the end of import sentence
#      => import tensorflow as tf