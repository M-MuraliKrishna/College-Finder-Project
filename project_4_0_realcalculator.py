# -*- coding: utf-8 -*-
"""Project 4.0 RealCalculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oLQFMInFf0oKe6A4d7IaWXMMMuMEyi7B
"""

def add(a,b):
  addition = a+b
  print(f"The Addition of {a} and {b} is {addition}")   #formatted strings
  
def sub(a,b):
  subtract = a-b
  print(f"The Subtraction of {a} and {b} is {subtract}")

def multi(a,b):
  multiplication = a*b
  print(f"The Multiplication of {a} and {b} is {multiplication}")

def div(a,b):
  division = a/b
  print(f"The Division of {a} and {b} is {division}")

def modules(a,b):
  module = a/b
  print(f"The Modules of {a} and {b} is {module}")

#taking multiple inputs in a single line
num1,operator,num2 = map(str, input("Enter Your Equation: ").split())
num1=int(num1)
num2=int(num2)

if operator == "+":
  print(add(num1,num2))
elif operator == "-":
  print(sub(num1,num2))
elif operator == "*":
  print(multi(num1,num2))
elif operator == "/":
  print(div(num1,num2))
elif operator == "%":
  print(modules(num1,num2))
else:
  print("Invalid typo Error! type something like- 4 / 2")