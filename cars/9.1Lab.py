"""
CSCI 1200
Lab Exercise 9.1

CLASSES

In this lab you will learn about class inheritance. Do all work in 
Geany IDE and follow instructions provided in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- Declare classes
- Declare and use attributes
- Declare and use methods
- Instantiate objects
- Use class inheritance

Evaluation
==========
20 pts. - submitted filename 9_1.py
20 pts. - 9_1.py executes without error
20 pts.	- Car class definition meets requirements
20 pts.	- ElectricCar class definition meets requirements
20 pts.	- Objects instantiated and used correctly

Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""

#=======================================================================
# ASSIGNMENT INSTRUCTIONS
#-----------------------------------------------------------------------
# In this assignment you will practice again how to declare and use
# classes in python. However, this time you will also create a child
# class that inherits from its parent class. This assignment will 
# demonstrate you some of the key features of inheritance. 
#
# STEPS:
# 
# 1. Declare a class called Car.
# 
# 2. Within Car class, create attributes for make and model. These
#    are required parameters when the class is instantiated. Also
#    create an attribute for mileage. Initialize this attribute with
#    a default value 0.
# 
# 3. Within Car class, make a method called drive(). The drive accepts
#    a numeric parameter `miles`. In the method body, add miles
#    to the current mileage of the car.
#
# 4. Within Car class, make another method called print_mileage(). This
#    method will print the make and model and the current mileage.
#
# 5. Within Car class, make another method called fill_gas(). When
#    called, this method prints an appropriate message, such as "gas
#    tank filled". This completes your Car class.
#-----------------------------------------------------------------------

class Car():
	"""class is car"""
	def __init__(self, make, model):
		self.make = make
		self.model = model
		self.mileage_reading = 0
		
		
	def fill_tank(self):
		"""Fills gas tank"""
		print("fill	up tank")
		
	def drive(self, miles):
		"""Drive some miles"""
		self.mileage_reading += miles
		
		
	def print_mileage(self):
		"""Tells mileage"""
		print(self.mileage_reading)
		
		
class ElectricCar(Car):
	
	"""Represent aspects of a car , specific to electric vehicles."""
	def __init__(self, make, model):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model)
		
	def fill_tank(self):
		"""Ready to go"""
		print("Ready to go")
	
	def charge_battery(self):
		"""Battery level"""
		print("All charged up")
		
my_car = Car("Ford", "Tundra")
fancy_car = ElectricCar('Tesla', 'model s')

my_car.drive(100) 
       
my_car.drive(200)

my_car.print_mileage()

my_car.fill_tank()

fancy_car.drive(100)

fancy_car.drive(200)

fancy_car.fill_tank()

fancy_car.charge_battery()

fancy_car.print_mileage()
	
	



#-----------------------------------------------------------------------
# 6. Declare another class called ElectricCar that inherits from Car.
#
# 7. Within ElectricCar class, create new method called charge_battery().
#    When called, this method should print an appropriate message. 
#
# 8. Within ElectricCar class, we are going to want to change the 
#    behavior of fill_gas() method, because it does not make sense to 
#    fill gas for an electric car. Override this method with a more
#    appropriate behavior.
#-----------------------------------------------------------------------







#-----------------------------------------------------------------------
# 8. Instantiate two objects where one must be a Car and one must be an 
#    ElectricCar.
#
# 9. Demonstrate that, for both objects, you can call the method drive.
#    After that display the mileage for both objects.
#
# 10. Demonstrate that for both objects, you can call the method 
#     fill_gas(). However these methods behave differently.
#
# 11. Lastly show that for ElectricCar, you can also call a method
#     charge_battery(). This method does not exist for regular Car.
#     Spend a few moments to review your code and understand why the
#     method exists for the child class but not for parent class.
#-----------------------------------------------------------------------








#=======================================================================
# That's it for today!
# End of Lab Exercise 9.1
#=======================================================================
