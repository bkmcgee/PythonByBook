#Chapter 4 Questions
#1: write a function that takes a number and returns it squared

a = input("please enter a number: ")
a = int(a)
print("your number squared: ", a**2)

#2: create a function that accepts a string as a paremter and prints it

def getStr():
  string1 = input("please enter a word:  ")
  string1 = str(string1)
  print(string1)

getStr()

#3: write a program with two functions, first should take integer as parameter then return that number divided by two. the second function should take that integer as a parameter and return it multiplied by four

def ex3(x):
  return x/2

def ex3_1(x):
  return x * 4

y = ex3(4) #plug in 4 for the problem
ans = ex3_1(y)

print(ans)

#4: write a function that converts a string to a float and returns result. Build in exceptions

def convert(string):
  try:
    return float(string)
  except ValueError:
    print("Error, input could not be converted....")

c = convert("654.2") #entered in a valid format
print(c)


