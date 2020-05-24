#return dictionary of infromation about artist/album
#takes textual info and puts it into a meaningful data structure
def make_album(artist, album_title, song = ''):
    music_album = {'artist': artist, 
                'album': album_title
                }
    if song:
        music_album['song'] = song
    return music_album 


active = True
while active:
    prompt = "Enter album artist and title"
    artist = input(prompt)
    if artist == 'quit':
        break

    prompt = "Enter artist"
    album_title = input(prompt)
    if album_title == 'quit':
        break

    album = make_album(artist, album_title)
print(album)
