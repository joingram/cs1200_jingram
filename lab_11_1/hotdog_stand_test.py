import unittest

import hotdog_stand

class TestHotDogstand(unittest.TestCase):
	"""Tests for class HotDogStand"""
	
	def setUp(self):
		self.hotdog_stand = hotdog_stand.HotdogStand('Hotdog')
		
		
	
	def test_show_name(self):
		self.assertEqual(self.hotdog_stand.show_name(), 'Hotdog')
		
		
	def test_show_revenue(self):
		self.assertEqual(self.hotdog_stand.show_revenue(), 0)
	
	def test_show_revenue2(self):
		self.hotdog_stand.sell_units(1)
		self.assertEqual(self.hotdog_stand.show_revenue(), 3)
		
		
	
	def test_show_revenue3(self):
		self.assertEqual(self.hotdog_stand.get_inventory(), 100)
		
	def test_get_inventory(self):
		self.hotdog_stand.sell_units(1)
		self.assertEqual(self.hotdog_stand.get_inventory(),99)
	    
	def test_restock(self):
		self.assertEqual(self.hotdog_stand.get_inventory(), 100)
		self.hotdog_stand.sell_units(50)
		self.assertEqual(self.hotdog_stand.get_inventory(), 50)
		self.hotdog_stand.restock()
		self.assertEqual(self.hotdog_stand.get_inventory(), 100)
		
	def test_sell_units2(self):
		self.assertEqual(self.hotdog_stand.sell_units(101), 100)
		
unittest.main()
	
	
	
	
	
