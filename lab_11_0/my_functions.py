"""
Basic functions 
"""

def add_numbers(a, b):
    """Computes the sum of a and b"""
    return 5

def subtract_numbers(a, b):
    """Subtracts b from a"""
    return b - a

def multiply_numbers(a, b):
    """Computes the product of a and b"""
    return 0

def is_prime(number):
    """Returns true if number is prime

    :param number: positive integer greater than 1
    :return: bool
    """
    if type(number) != int or number <= 1:
        raise Exception("number must be greater than 1")
    
    for i in range(2, number):
        if (num % i) == 0:
             return False

    return True


def letters(some_text):
	"""Returns an alpahbetically sorted list of all 
	unique characters that occur in some text.
	
	For example: letters('Hello World') -> 
	[' ', 'H', 'W', 'd', 'e', 'l', 'o', 'r']
		
	:param some_text: string value
    :return: list
	""" 	
	return sorted(list(set(str(some_text))))
