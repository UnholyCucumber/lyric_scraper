import lyricsgenius
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

genius = lyricsgenius.Genius("PcLPErAXnHEREVUwt1joZmXNyW-pChC-K7OAZdWm7WPxMWaC0ui9fEFgKV6W9SBF")
# artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")

song = genius.search_song("Happy", "Pharrell Williams")
lyrics = song.lyrics
def isWrittenLine(line) :
    return line and not line.startswith('[')
to_anlayze = list(filter(isWrittenLine, lyrics.splitlines()))
print(to_anlayze)

analyzer = SentimentIntensityAnalyzer()
for line in to_anlayze:
    scores = analyzer.polarity_scores(line)
    print("{:-<65} {}".format(line, str(scores)))

full_lyrics = ' '.join(to_anlayze)
vs = analyzer.polarity_scores(full_lyrics)
print("{:-<65} {}".format(full_lyrics, str(vs)))
