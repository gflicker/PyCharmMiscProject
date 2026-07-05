# A function returning a dictionary
def make_album(artist_name, album_title, tracks=None):
    album = {"artist": artist_name.title(), "title": album_title.title()}
    if tracks:
        album["tracks"] = tracks
    return album
#Looping it to infinite
while True:
    print("enter 'q' any time to quit")
    name = input("Artist's name: ")
    #Kill switch
    if name == 'q':
        break
    artist_album = input("Title of the album: ")
    if artist_album == 'q':
        break
    #Calling the function
    full_info = make_album(name, artist_album)
    print(full_info)