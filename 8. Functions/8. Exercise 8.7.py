# A function returning a dictionary
def make_album(artist_name, album_title, tracks=None):
    album = {"artist": artist_name.title(), "title": album_title.title()}
    if tracks:
        album["tracks"] = tracks
    return album
full_info = make_album("yo maps", "komando")
chile_one = make_album("chile one", "eagle one")
JK = make_album("JK", "balalolela", 27)
print(full_info)
print(chile_one)
print(JK)