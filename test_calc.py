import unittest
import calc


class TestCalc(unittest.TestCase):

	# Test method name should start with test_. otherwise it will not be tested

	def test_add(self):	
		self.assertEqual(calc.add(10, 5), 15)
		self.assertEqual(calc.add(-1, 1), 0)
		self.assertEqual(calc.add(-1, -1), -2)

	def test_subt(self):
		self.assertEqual(calc.subt(10, 5), 5)
		self.assertEqual(calc.subt(-1, 1), -2)
		self.assertEqual(calc.subt(-1, -1), 0)

	def test_mult(self):
		self.assertEqual(calc.mult(10, 5), 50)
		self.assertEqual(calc.mult(-1, 1), -1)
		self.assertEqual(calc.mult(-1, -1), 1)

	def test_divide(self):
		self.assertEqual(calc.divide(10, 5), 2)
		self.assertEqual(calc.divide(-1, 1), -1)
		self.assertEqual(calc.divide(-1, -1), 1)
		self.assertEqual(calc.divide(5, 2), 2.5)

		# Below two ways to assert exceptions

		#self.assertRaises(ValueError, calc.divide, 10, 0) or

		with self.assertRaises(ValueError):
			calc.divide(10, 0)


if __name__ == '__main__':
	unittest.main()
