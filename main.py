import os
from list_files import list_files
from cleanup_file import cleanup_file
from create_page import create_page

def main():
    # Ask the user to choose a file
    filename = list_files()
    
    # Extract the title from the filename
    title = os.path.splitext(filename)[0]
    
    # Clean up the file content based on its format
    content = cleanup_file(filename)

    # Create a Confluence page with the title and content
    create_page(title, content)

if __name__ == "__main__":
    # The main function is executed when the script is run directly
    main()
