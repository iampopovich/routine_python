import re
import threading
import unittest


class regexTestcase(unittest.TestCase):

	# def __init__(self, *args,**kw):
	# 	# super().__init__(*args)
	# 	self.text = None
	# 	self.regex = None
	# 	self.count = None
	def setUp(self):
		self.text = 'hehehehhhehhehhe'
		self.part = 'he'
		self.count = 7

	def test_starts_with(self):
		result = re.search(r'^{}'.format(self.part), self.text)
		self.assertTrue(result)

	def test_ends_with(self):
		result = re.search(r'{}$'.format(self.part), self.text)
		self.assertTrue(result)

	def test_match_count_less(self):
		result = re.findall(r'{}'.format(self.part), self.text)
		self.assertLess(len(result), self.count)

	def test_match_count_equal(self):
		result = re.findall(r'{}'.format(self.part), self.text)
		self.assertEqual(len(result), self.count)

	def test_match_count_greater(self):
		result = re.findall(r'{}'.format(self.part), self.text)
		self.assertGreater(len(result), self.count)

if __name__ == '__main__':
	# test = regexTestcase()
	# test.text = 'hehehehhhehhehhe'
	# test.part = 'he'
	# test.count = 2
	unittest.main()