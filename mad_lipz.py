import functions
import os
import random

# program checks if we are in the right folder and if not changes it the correct one
current_directory = os.getcwd()
text_directory = current_directory + '/Texts'
os.chdir(text_directory)

# program creates the variable to store all the files in the texts folder
file_list = os.listdir(text_directory)

# program creates a path of one random file from the folder
file_name = random.choice(file_list)
path_to_file = os.path.join(text_directory, file_name)

# program opens the randomly chosen file
opened_file = open(path_to_file)

# program stores the file content as string in a variable
text = opened_file.read()

# program converts the string into a list of words
list_of_words = text.split()

# program replaces the words
functions.replace_words(list_of_words)

# program converts the list of words back to a string and prints it on the screen
functions.list_to_string(list_of_words)
