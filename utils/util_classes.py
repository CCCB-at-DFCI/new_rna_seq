from printers import pretty_print
import sys
import logging
from custom_exceptions import ParameterNotFoundException

class Params(object):
	def __init__(self):
		self.__param_dict__ = {}

	def __str__(self):
		return pretty_print(self.__param_dict__)


	def get_param_dict(self):
		return self.__param_dict__

	def get(self, name):
		"""
		Returns the value, given the key.
		Will raise a KeyError if the key 'name' is not found in the dictionary
		"""
		try:
			return self.__param_dict__[name]
		except KeyError:
			logging.error("Could not locate parameter: '%s' in parameter dictionary.  ", name)
			raise ParameterNotFoundException("Tried to retrieve a parameter that was not set.  See log.")


	def add(self, *args, **kwargs):
		"""
		Adds key-value pairs to the dictionary of parameters
		"""
		for arg in args:
			self.__add_dict__(arg)
		
		self.__add_dict__(kwargs)



	def __add_dict__(self, d):
		"""
		private method that unpacks a dictionary and adds it to the param_dict dictionary
		Silently errors if the passed argument d is not a dictionary
		"""
		try:
			for k,v in d.iteritems():
				self.__param_dict__[k]=v
		except AttributeError:
			pass
