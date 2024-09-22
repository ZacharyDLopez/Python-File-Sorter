import os

def file_sorter_menu():
    print("+-----------------------------------+")
    print("|          File Sorter Menu         |")        
    print("+-----------------------------------+\n")
    print("1. Search for a Directory")
    print("2. Create a Directory")
    print("3. Search for a File")
    print("4. Sort Files")    
    print("5. Exit")

def search_directory(user_directory):
    print()

    if os.path.exists(user_directory):
        print("Directory found.\n")
    else:
        print("Directory not found.\n")

def create_directory(user_directory, new_directory):
    for items in os.listdir(user_directory):
        if items == new_directory:
            print("Directory already exists.\n")
            break
        else:
            os.mkdir(user_directory + "/" + new_directory)
            print("Directory created.\n")
            break

def search_files(user_directory, search_type):
    if search_type == "file":
        search_file = input("Enter the name of the file you are looking for: ")
        print()

        if not os.path.exists(user_directory + "/" + search_file):
            print("File not found.\n")

        else:
            file_list = []
            for files in os.listdir(user_directory):
                if search_file in files:
                    file_list.append(files)
                    print("File found.\n")
    else:
        search_directory = input("Enter the name of the directory you are looking for: ")
        print()

        if not os.path.exists(user_directory + "/" + search_directory):
            print("Directory not found.\n")

        else:
            directory_list = []
            for directories in os.listdir(user_directory):
                if search_directory in directories:
                    directory_list.append(directories)
                    print("Directory found.\n")
    

def sort_files(user_directory, sort_type):
    if sort_type == "files":
        folder_names = {
            "Text Files" : "txt",
            "PDF Files" : "pdf",
            "Word Files" : "docx",
            "Excel Files" : "xlsx",
            "Powerpoint Files" : "pptx", 
            "Image Files" : "png",
            "Audio Files" : "mp3",
            "Video Files" : "mp4",
            "Compressed Files" : "zip",
            "Executable Files" : "exe",
            "Python Files" : "py",
            "Java Files" : "java",
            "Application Extension Files" : "dll",
            "Configuration Files" : "ini",
            "Cabinet Files" : "cab",
            "BMP Files" : "bmp",
            "Windows Installer Files" : "MSI",
            "Git configuration Files" : "gitconfig",
            "Bash History Files" : "bash_history",
            "QREG Files" : "qreg",
            "JSON Files" : "json",
            "Node repl history Files" : "node_repl_history",
            "Less Hst Files" : "lesshst"
        }
        
        files_to_sort = os.listdir(user_directory)

        for files in files_to_sort:
            for folder_name, extension in folder_names.items():
                if extension in files:
                    if not os.path.exists(user_directory + "/" + folder_name):
                        os.mkdir(user_directory + "/" + folder_name)
                    os.rename(user_directory + "/" + files, user_directory + "/" + folder_name + "/" + files)

        print("Files sorted!\n") 

def main():
    file_sorter_menu()

    while True:
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            user_directory = input("\nEnter the file path you want to search for: ")
            search_directory(user_directory)

            user_continue = input("Do you want to continue? (y/n): ")
            print()

            if user_continue == "n":
                break
            else:
                file_sorter_menu()

        elif choice == "2":
            user_directory = input ("\nEnter a file path to create a new directory: ")
            print()

            new_directory = input("Enter the name of the new directory: ")
            print()

            create_directory(user_directory,new_directory)

            user_continue = input("Do you want to continue? (y/n): ")
            print()

            if user_continue == "n":
                break
            else:
                file_sorter_menu()

        elif choice == "3":
            user_directory = input("\nEnter the path of the directory you want to search for files in: ")
            print()

            search_type = input("Are you looking for a File or a Directory? (file/directory): ")
            print()

            search_files(user_directory, search_type)

            user_continue = input("Do you want to continue? (y/n): ")
            print()

            if user_continue == "n":
                break
            else:
                file_sorter_menu()

        elif choice == "4":
            user_directory = input("\nEnter the path of the directory you want to sort files in: ")
            print()

            sort_type = input("Are you sorting Files or Directories? (files/directories): ")
            print() 

            sort_files(user_directory, sort_type)

            user_continue = input("Do you want to continue? (y/n): ")
            print()

            if user_continue == "n":
                break
            else:
                file_sorter_menu()

        elif choice == "5":
            print("Thank you for using the File Sorter. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")
main()  