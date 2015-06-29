import unittest
from PyKo import process_song_link, process_playlist_link

class TestPyKo(unittest.TestCase):

	def setUp(self):
		self.song_name = "benny+lava"
		self.song_url = "https://www.youtube.com/results?search_query={}"\
		.format(self.song_name)
		
		self.playlist_url = "https://www.youtube.com/results?filters=playlist&"\
		"lclk=playlist&search_query={}".format(self.song_name)

	def test_process_song_link_url(self):
		self.ln = process_song_link(self.song_url)
		print self.ln
		self.assertIn('watch?v', self.ln)

	def test_process_playlist_link(self):
		self.pl = process_playlist_link(self.playlist_url)
		print self.pl
		self.assertIn('watch?v', self.pl)

if __name__ == '__main__':
	unittest.main()