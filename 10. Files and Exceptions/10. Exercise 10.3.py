#First creating an empty file, add more data to it
filename = 'guest.txt'
with open(r'E:\Studio 1\Videos\Python\Crash Course\10. Files and Exceptions\guest.txt', 'w') as guests:
    guest_list = guests.write('Estina Haluse\n')

#Now we should add new guests to the list
file_name = 'guest.txt'
with open(file_name, 'a') as update_guests:
    update_guests.write("Givious Haluse\n")
    update_guests.write("Rose Zulu\n")
    update_guests.write("Sunwell Haluse\n")
    update_guests.write("Haggai Haluse\n")
