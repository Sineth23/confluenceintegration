import os

def list_files():
    # Specify the directory path
    directory = "created documentation"
    
    # Get the list of files in the directory
    files = os.listdir(directory)
    
    # Display the list of files with numbers
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    
    # Ask the user to choose a file by entering its number
    file_num = int(input("Enter the number of the file you want to choose: "))
    
    # Return the selected file
    return files[file_num - 1]
