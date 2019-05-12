import lyricsgenius
import vaderSentiment

genius = lyricsgenius.Genius("PcLPErAXnHEREVUwt1joZmXNyW-pChC-K7OAZdWm7WPxMWaC0ui9fEFgKV6W9SBF")
# artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")

song = genius.search_song("Backseat Freestyle", "Kendrick Lamar")
print(song.lyrics)



# print(artist.songs)