import csv

end = False

while(end == False):
    user_input = input("What type of animal would you like to inquire about today? ")
    file_to_open = 'data/' + user_input.lower() + '.csv'

    try:
        with open(file_to_open, newline='') as file:
            csv_reader = csv.DictReader(file, skipinitialspace=True)
            for row in csv_reader:
                print(f"{row['name'].capitalize()} is a {row['age']} year old {row['breed']}.")
            file.close()
        end = True
    except:
        print(f"Sorry, we don't have any {user_input} here.\n")