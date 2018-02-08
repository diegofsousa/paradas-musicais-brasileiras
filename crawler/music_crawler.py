from crawler.search import SearchLyricsData, SearchCipherData

import csv

class CrowlerList(object):
	"""docstring for CrowlerList"""
	def __init__(self, matrix):
		super(CrowlerList, self).__init__()
		self._matrix = matrix

	def matrix_to_csv(self, filename="music_crawler_file"):
		with open(filename+".csv", 'w') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=';',
							quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow(['position', 'artist', 'music', 'gender', 'number_of_unique_words', 'number_of_chords', 'views', 'lyrics_link', 'cipher_link'])
			pos = 0

			for music, artist in self._matrix:
				pos += 1
				row = []

				print("{} - {}".format(music, artist))
				sample = SearchLyricsData(artist, music)


				sample_cipher = None
				if sample.total_return_for_lyrics()[6]:
					sample_cipher = SearchCipherData(sample.total_return_for_lyrics()[6])

				row.append(pos)
				row.append(sample.total_return_for_lyrics()[0])
				row.append(sample.total_return_for_lyrics()[1])
				row.append(sample.total_return_for_lyrics()[5])
				row.append(sample.total_return_for_lyrics()[3])
				row.append(sample_cipher.number_of_chords())
				row.append(sample.total_return_for_lyrics()[4])
				row.append(sample.total_return_for_lyrics()[2])
				row.append(sample.total_return_for_lyrics()[6])

				filewriter.writerow(row)
				print("\n")

	def csv_to_csv(self, filename):
		with open(filename, newline='') as csvfile:
			music = csv.reader(csvfile, delimiter=';', quotechar='|')
			for row in music:
				print(row)

li = [
	['raça negra', 'cheia de manias'],
	['anitta', 'vai malandra'],
		
]

meu_crow = CrowlerList(li)
meu_crow.csv_to_csv("musica_tophits_00.htm.csv")