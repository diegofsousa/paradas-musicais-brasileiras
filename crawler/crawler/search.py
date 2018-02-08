from selenium import webdriver

from utils import (to_compose_search_string,
				   duck_search_string,
				   select_lyrics_link,
				   work_in_request_lyrics_url,
				   select_lyric_in_html,
				   select_number_views,
				   select_gender,
				   select_music_cipher_url)

class SearchLyricsData(object):
	"""docstring for Search"""
	def __init__(self, artist, music):
		super(SearchLyricsData, self).__init__()
		self.__artist = artist
		self.__music = music
		self.__search_string = to_compose_search_string(artist, music)
		self.__driver = webdriver.PhantomJS()
		self.__lyrics_url = self.__ask_duck_for_lyrics_url__()
		self.__lyrics_html = self.__request_lyrics_url__()

	def __repr__(self):
		return "<(SearchLyricsDataObject) artist: {}, music: {}, lyrics url: {}>".format(
						self.__artist, self.__music, self.__lyrics_url)

	def __ask_duck_for_lyrics_url__(self):
		try:
			self.__driver.get(duck_search_string(self.__search_string))
			return select_lyrics_link(self.__driver.page_source)
		except Exception as e:
			print(e)
			return None

	def __request_lyrics_url__(self):
		return work_in_request_lyrics_url(self.__lyrics_url)

	def total_return_for_lyrics(self):
		return (self.__artist,
				self.__music,
				self.__lyrics_url,
				self.__words_not_repeated_in_lyrics__(),
				self.__number_of_views__(),
				self.__gender__(),
				self.__music_cipher_url__())

	def __words_not_repeated_in_lyrics__(self):
		if self.__lyrics_html:
			return len(select_lyric_in_html(self.__lyrics_html))
		return None

	def __number_of_views__(self):
		if self.__lyrics_html:
			return select_number_views(self.__lyrics_html)
		return None

	def __gender__(self):
		if self.__lyrics_html:
			return select_gender(self.__lyrics_html)
		return None

	def __music_cipher_url__(self):
		if self.__lyrics_html:
			return select_music_cipher_url(self.__lyrics_html)
		return None
		

anita = SearchLyricsData("anitta", "vai malandra")
print(anita)
print(anita.total_return_for_lyrics())





		