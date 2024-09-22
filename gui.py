from tkinter import *
from tkinter import filedialog as fd
import pathlib

def select_file_path():
    path_name = fd.askopenfilename
    print(path_name)
    
def browseFiles():
    window = Tk()
    # window size, color, and title
    window.title("File Sorter")
    window.geometry("700x500")
    window.configure(bg = "#2C2C2C")

    # Textbox with file path

    
    # Text for Title, subheading, and buttons
    title = "File Sorter"
    subheading = "Click Browse to select a folder to sort"
    browse_button = "Browse"
    sort = "Sort"
    open_folder = "Open Folder"

    # Tooltip text
    tooltip_text = "Please select a folder to sort in Browse"
    
    # Text Functionality

    title_display = Label(window, text = title)
    title_display.config(bg = "#2C2C2C", fg = "#D4D4D4",font=("Roboto", 40))

    subheading_display = Label(window, text = subheading)
    subheading_display.config(bg = "#2C2C2C", fg = "#D4D4D4",font = ("Roboto", 11))
    
    title_display.place(relx = 0.33, rely = 0.1)
    subheading_display.place(relx= 0.33, rely=0.24)

    window.mainloop()
browseFiles()