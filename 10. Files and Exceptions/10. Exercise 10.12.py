#Writing a program that retrieves the number and if the number is not there it stores it
import json
running = True
while running:
    filename = 'favorite_numbers.json'
    try:
        favorite_number = int(input('What is your favorite number: '))

    except ValueError:
        print('Please enter a valid number')
    else:
        with open(filename) as f:
            number = json.load(f)

        if favorite_number == number:
            print(f'Your favorite number {favorite_number} is already saved!')

        else:
            running = False
            with open(filename, 'w') as new_file:
                json.dump(favorite_number, new_file)
            print(f'Your favorite number has been saved!')
