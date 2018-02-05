from selenium import webdriver
import requests as req

from utils import to_compose_search_string, duck_search_string, select_lyrics_link

class Search(object):
	"""docstring for Search"""
	def __init__(self, artist, music):
		super(Search, self).__init__()
		self.artist = artist
		self.music = music
		self.search_string = to_compose_search_string(artist, music)
		self.driver = webdriver.PhantomJS()

	def ask_duck_for_lyrics(self):
		try:
			self.driver.get(duck_search_string(self.search_string))
			return select_lyrics_link(self.driver.page_source)
		except Exception as e:
			print(e)
			return None
		

anita = Search("anitta", "vai malandra")
print(anita.ask_duck_for_lyrics())





		