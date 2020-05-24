#return dictionary of infromation about artist/album
#takes textual info and puts it into a meaningful data structure
def make_album(artist, album_title, song = ''):
    music_album = {'artist': artist, 'album': album_title}
    if song:
        music_album['song'] = song
    return music_album 




musician = make_album('System of a down', 'Toxicity')
print(musician)
musician = make_album('led zep', 'Physical Graffiti')
print(musician)
musician = make_album('beatles', 'red album')
print(musician)



