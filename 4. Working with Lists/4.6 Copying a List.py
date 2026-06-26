#Copying a list
my_favorite = ["Nshima", "Beans", "Pizza", "Kapenta", "Fish"]
Caramels_favorite = my_favorite
print(f'My favorite foods are:')
for favorite in my_favorite:
    print(favorite.upper())
print(f'My girlfriends favorite foods are:')
for favor in Caramels_favorite:
    print(favor.upper())
print("The outcome is the same because my girlfriends list has been\n"
      "copied from my list.\n")
#We add one food item to my girlfriend's list
print("Will add one item to Caramels_favorite "
      "and see if it will be my_favorite.")
Caramels_favorite.insert(0,"Sausage")
my_favorite.sort(reverse=False)
for mine in my_favorite:
    #my_favorite.sort(reverse=True)
    print(mine.upper())