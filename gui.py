import tkinter as tk
from tkinter.filedialog import askdirectory
import pathlib

def button_clicked():
   askdirectory()
   
def browseFiles():
    window = tk.Tk()
    # window size, color, and title
    window.title("File Sorter")
    window.geometry("700x500")
    window.configure(bg = "#2C2C2C")

    # Textbox with file path
    # path_name = askdirectory()

    #Button Functionality
    browse_text = "Browse"
    browse_button = tk.Button(window, 
                   text=browse_text, 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)


    # Text for Title, subheading, and buttons
    title = "File Sorter"
    subheading = "Click Browse to select a folder to sort"
    sort_text = "Sort"
    open_folder_text = "Open Folder"

    # Tooltip text
    tooltip_text = "Please select a folder to sort in Browse"
    
    # Text Functionality

    title_display = tk.Label(window, text = title)
    title_display.config(bg = "#2C2C2C", fg = "#D4D4D4",font=("Roboto", 40))

    subheading_display = tk.Label(window, text = subheading)
    subheading_display.config(bg = "#2C2C2C", fg = "#D4D4D4",font = ("Roboto", 11))
    
    title_display.place(relx = 0.33, rely = 0.1)
    subheading_display.place(relx= 0.33, rely=0.24)
    browse_button.place(relx= 0.30,rely=0.30)

    window.mainloop()
browseFiles()