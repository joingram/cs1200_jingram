class Car():
	"""class is car"""
	def _init_(self, make, model):
		self.make = make
		self.model = model
		self.mileage_reading = 0
		
		
	def fill_tank(self):
		"""Fills gas tank"""
		print("fill	up tank")
		
	def drive(self, miles):
		"""Drive some miles"""
		self.mileage_reading += miles
		
		
	def print mileage(self):
		"""Tells mileage"""
		print(self.mileage)
		
	
		
	
		
		
		
		
		
	# ~ def get_descriptive_name(self):
		# ~ long_name = str(self.year) + ' ' + self.make + ' ' + slef.model
		# ~ return long_name.title()
		
	# ~ def read_mileage(self):
		# ~ print("This car has" + str(self.mileage_reading) + " miles on it.")
		
	# ~ def update_odomoter(self, mileage):
		# ~ if mileage >= self.mileage_reading:
			# ~ self.mileage_reading = mileage
		# ~ else:
			# ~ print("You can't roll back on mileage.")
			
		# ~ def increment_mileage(self, miles):
			# ~ self.mileage_reader += miles 
