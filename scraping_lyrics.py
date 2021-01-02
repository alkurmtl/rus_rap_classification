import lyricsgenius
import os
token_file = open('genius_token.txt', 'r')
token = token_file.read().rstrip('\n')
genius = lyricsgenius.Genius(token)
token_file.close()
artists_list = open('artists.txt', 'r')
for artist in artists_list:
    artist = artist.rstrip('\n')
    path = './data/' + artist
    os.mkdir(path)
    artist = genius.search_artist(artist, sort="popularity", include_features=True)
    print(artist.songs)
    for song in artist.songs:
        lyrics_file = open(path + '/' + song.title + '.txt', 'w')
        lyrics_file.write(song.lyrics)
        lyrics_file.close()

