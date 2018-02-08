from selenium import webdriver

from utils import (to_compose_search_string,
				   duck_search_string,
				   select_lyrics_link,
				   work_in_request_url,
				   select_lyric_in_html,
				   select_number_views,
				   select_gender,
				   select_music_cipher_url,
				   select_music_chords)

class SearchLyricsData(object):
	"""docstring for Search"""
	def __init__(self, artist, music):
		super(SearchLyricsData, self).__init__()
		self.__artist = artist
		self.__music = music
		self.__search_string = to_compose_search_string(artist, music)
		self.__driver = webdriver.Firefox()
		self.__lyrics_url = self.__ask_duck_for_lyrics_url__()
		self.__lyrics_html = self.__request_lyrics_url__()
		self.__driver.quit()

	def __repr__(self):
		return "<(SearchLyricsDataObject) artist: {}, music: {}, lyrics url: {}>".format(
						self.__artist, self.__music, self.__lyrics_url)

	def __ask_duck_for_lyrics_url__(self):
		print("Request duck go search url...", end='', flush=True)
		try:
			self.__driver.get(duck_search_string(self.__search_string))
			print("  Ok!")
			#self.__driver.quit()
			return select_lyrics_link(self.__driver.page_source)
		except Exception as e:
			print(" "+ e)
			return None

	def __request_lyrics_url__(self):
		if self.__lyrics_url:
			print("Request lyrics url...", end='', flush=True)
			return work_in_request_url(self.__lyrics_url)
		return None

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
		

class SearchCipherData(object):
	"""docstring for SearchCipherData"""
	def __init__(self, cipher_url):
		super(SearchCipherData, self).__init__()
		self.__cipher_url = cipher_url
		self.__cipher_html = self.__request_cipher_url__()

	def __request_cipher_url__(self):
		print("Request cipher url...", end='', flush=True)
		return work_in_request_url(self.__cipher_url)

	def number_of_chords(self):
		if self.__cipher_html:
			return len(select_music_chords(self.__cipher_html))
		return None

anita_l = SearchLyricsData("tom jobim", "desafinado")
if anita_l.total_return_for_lyrics()[6]:
	anita_c = SearchCipherData(anita_l.total_return_for_lyrics()[6])

print(anita_l)
print(anita_c.number_of_chords())