#Chapter 4 Functions
# October 13 2020
def f(x):
  return x*2
print(f(2))

def func():
  return 20*3
result1 = func()
print(result1)

def func1(a,b,c):
  return a+b+c
result2 = func1(4,5,6)
print(result2)


age = input("Enter your age:")
int_age = int(age)
if int_age < 30:
  print("wow, so young")
else:
  print("wow, so old")

#call above age three times
def ask_age():
  age = input("Enter your age:")
  int_age = int(age)
  if int_age < 30:
    print("wow, so young")
  else:
    print("wow, so old")

#ask_age()
#ask_age()
#ask_age()

#Parameters
def adding(x1, y1=10):
  return x1+y1

result = adding(4)
print(result)

