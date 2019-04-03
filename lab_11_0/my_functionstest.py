import unittest
import my_functions

class TestMyFunctions(unittest.TestCase):
	def test_addnumbers(self):
		self.assertEqual(my_functions.add_numbers(3,2),5)
	def test_addnumbers(self):
		self.assertEqual(my_functions.add_numbers(3,3),6)
	def test_addnumbers2(self):
		self.assertEqual(my_functions.add_numbers(3,3),6)
	def test_subtract_numbers(self):
		self.assertEqual(my_functions.subtract_numbers(2,3),1)
	def test_subtract_numbers2(self):
		self.assertEqual(my_functions.subtract_numbers(2,4),2)
	def test_multiply_numbers(self):
		self.assertEqual(my_functions.multiply_numbers(2,0),0)
	def test_multiply_numbers2(self):
		self.assertEqual(my_functions.multiply_numbers(3,0),0)
	def test_is_prime(self):
		self.assertTrue(my_functions.is_prime(2), True )
	def test_is_prime2(self):
		self.assertEqual(my_functions.is_prime(21), False)
	def test_letters(self):
		self.assertEqual(my_functions.letters('Hello World'), [' ', 'H', 'W', 'd', 'e', 'l', 'o', 'r'])
	def test_letters2(self):
		self.assertEqual(my_functions.letters('turkey'), [ 'e', 'k', 'r', 't', 'u','y' ])
	
		
unittest.main()

