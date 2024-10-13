#Task-7.1
# Write a Python program using Function to which will do the following:- 
# a.) The function will create a text file with the current timestamp. 
# b.) The file content should have the content of the current timestamp.

import datetime

def create_timestamp_file():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    
    # Create a filename using the current timestamp
    filename = f"{current_timestamp}.txt"
    
    #the current timestamp to the file
    with open(filename, 'w') as file:
        file.write(current_timestamp)
    
    print(f"File '{filename}' created with the current timestamp.")

# Callfunction
create_timestamp_file()
