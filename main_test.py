import unittest
import main

class TestStringMethods(unittest.TestCase):

  def test_get_at_bat_sum(self):
      self.assertEqual(main.get_at_bats_sum('batting.csv'), 4858210)

  # def test_isupper(self):
  #     self.assertTrue('FOO'.isupper())
  #     self.assertFalse('Foo'.isupper())
  #
  # def test_split(self):
  #     s = 'hello world'
  #     self.assertEqual(s.split(), ['hello', 'world'])
  #     # check that s.split fails when the separator is not a string
  #     with self.assertRaises(TypeError):
  #         s.split(2)

if __name__ == '__main__':
    unittest.main()
