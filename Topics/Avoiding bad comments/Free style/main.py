#   Module OS will provide access to the operating system
import os

#   file_name will register the user input to find the file
file_name = input("Please write the name of the file to work with:\n")

if os.path.exists(file_name):
    #   with function allow us to read the file
    with open(file_name) as file:
        content = file.read()

    #   process() function to be applied to the file
    new_content = process(content)

    #   with function now help us to create a new writing file
    with open(f'{file_name}_processed.txt', 'w') as new_file:
        new_file.write(new_content)

    #   Return results
    print("All done!")

#   If the file does not exist return warning
else:
    print("The file you entered does not exist!")
