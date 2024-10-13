#Task-7.2
#Write another Python function to read from a text file.
#The function will take the name of the text file and display the content of the file into the console.
def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

# Example usage
read_file('my trail text file.txt')
