import unittest
import mock
import sys

# for finding modules in the sibling directories
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from utils.util_methods import *
from utils.custom_exceptions import *

def dummy_join(a,b):
	return os.path.join(a,b)

class UtilMethodsTest(unittest.TestCase):

	@mock.patch('utils.util_methods.os')
	def test_missing_file_raises_exception(self, mock_os):

		mock_os.path.isfile.return_value = False
		with self.assertRaises(MissingFileException):
			check_for_file('/path/to/nothing')


	@mock.patch('utils.util_methods.os')
	def test_missing_config_file_raises_exception(self, mock_os):

		mock_os.listdir.return_value = []
		with self.assertRaises(ConfigFileNotFoundException):
			locate_config('/path/to/dir')


	@mock.patch('utils.util_methods.os.path.join', side_effect=dummy_join)
	@mock.patch('utils.util_methods.os')
	def test_multiple_config_files_raises_exception(self, mock_os, mock_join):

		mock_os.listdir.return_value = ['a.cfg','b.cfg']
		with self.assertRaises(MultipleConfigFileFoundException):
			locate_config('/path/to/dir')

	@mock.patch('utils.util_methods.os.path.join', side_effect=dummy_join)
	@mock.patch('utils.util_methods.os')
	def test_single_config_file(self, mock_os, mock_join):

		mock_os.listdir.return_value = ['a.cfg']
		self.assertEqual(locate_config('/path/to/dir'), '/path/to/dir/a.cfg')
		

if __name__ == "__main__":
	unittest.main()