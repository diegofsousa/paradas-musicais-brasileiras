from crawler.crawler.search import SearchLyricsData, SearchCipherData

import csv

class CrowlerList(object):
	"""docstring for CrowlerList"""
	def __init__(self):
		super(CrowlerList, self).__init__()

	def matrix_to_csv(self, matrix, filename="music_crawler_file"):
		with open(filename+".csv", 'w') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=';',
							quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow(['position', 'artist', 'music', 'gender', 'number_of_unique_words', 'number_of_chords', 'views', 'lyrics_link', 'cipher_link'])
			pos = 0

			for music, artist in matrix:
				pos += 1
				row = []

				print("[{}/{}] Searching for '{} - {}'' ...".format(pos, len(matrix), music, artist))
				sample = SearchLyricsData(artist, music)


				sample_cipher = None
				if sample.total_return_for_lyrics()[6]:
					sample_cipher = SearchCipherData(sample.total_return_for_lyrics()[6])

				sample = [b if b is not None else '' for b in sample.total_return_for_lyrics()]

				row.append(pos)
				row.append(sample[0])
				row.append(sample[1])
				row.append(sample[5])
				row.append(sample[3])
				try:
					row.append(sample_cipher.number_of_chords())
				except Exception as e:
					row.append('')
				row.append(sample[4])
				row.append(sample[2])
				row.append(sample[6])

				filewriter.writerow(row)
				print("\n")

	def csv_to_csv(self, filename):
		with open(filename, newline='') as csvfile:
			music = csv.reader(csvfile, delimiter=';', quotechar='|')
			self.matrix_to_csv(list(music), filename+"_output")