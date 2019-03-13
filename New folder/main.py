#from my_functions import replicate,unique
import my_functions
import math
x= .67
z = math.cos(x)
x = math.sin(x)
c = math.tan(x)
print("The cos of .67 is" + str(z))
print("The sin of .67 is" + str(x))
print("The cos of .67 is" + str(c))

print(my_functions.replicate('hi',3))
print("The colors are" + str(my_functions.unique("red","blue","green","green")))
