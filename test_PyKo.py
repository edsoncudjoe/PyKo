from bs4 import BeautifulSoup
import unittest
from PyKo import songName, artistName, front

class Test_PyKo(unittest.TestCase):

	def setUp(self):
		self.PyKo.songName = "Minnie moocher"
		self.PyKo.artistName = "Cab Calloway"

	def test_songName(self):
		assertEqual(self.PyKo.songName, "Minnie moocher")

	def test_front(self):
		pass

if __name__ == '__main__':
	unittest.main()