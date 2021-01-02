import lyricsgenius
import os
token_file = open('genius_token.txt', 'r')
token = token_file.read().rstrip('\n')
genius = lyricsgenius.Genius(token)
token_file.close()
artists_list = open('artists.txt', 'r')
for artist in artists_list:
    artist = artist.rstrip('\n')
    id = -1
    if artist[0] == '(':
        id = artist.split()[0]
        id = id.lstrip('(')
        id = id.rstrip(')')
        id = int(id)
    path = './data/' + artist
    os.mkdir(path)
    if id == -1:
        artist = genius.search_artist(artist, sort="popularity", get_full_info=False)
    else:
        artist = genius.search_artist(artist, sort="popularity", get_full_info=False, artist_id=id)
    print(artist.songs)
    for song in artist.songs:
        try:
            lyrics_file = open(path + '/' + song.title + '.txt', 'w')
        except Exception:
            print('Failed to create file for' + song.title)
            continue
        if song.lyrics is not None:
            lyrics_file.write(song.lyrics)
        lyrics_file.close()

