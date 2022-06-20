# def dict():
#     x={i:i**2 for i in range(1,16)}
#     print(x)
# dict()
# from tkinter import Y
from collections import defaultdict

def numbers():
    x=["a","b","c","d","z"]
    y=[1, 2,3,7,4]
  
    z=defaultdict(list)
for key, value in zip(x, y):
    z[key].append(value)

    z[key].append(value)
    print (dict(z)) 
numbers()
  

