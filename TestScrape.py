import lyricsgenius
genius = lyricsgenius.Genius("PcLPErAXnHEREVUwt1joZmXNyW-pChC-K7OAZdWm7WPxMWaC0ui9fEFgKV6W9SBF")
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
