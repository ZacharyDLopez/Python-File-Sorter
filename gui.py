import tkinter as tk
from tkinter import filedialog
import os as os
import file_sorter

def select_folder():
   path = filedialog.askopenfilename(title='Please Select a Directory', filetypes=file_sorter.folder_names)

   return path

def browseFiles():
    window = tk.Tk()
    # Define window size, color, and title
    window.title("File Sorter")
    window.geometry("700x500")
    window.configure(bg = "#2C2C2C")

    #Define button functionality
    current_directory = select_folder
   

    browse_text = "Browse"
    browse_button = tk.Button(window, 
                   text=browse_text, 
                   command=current_directory,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="#696969",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="#D4D4D4",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="#444444",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=10,
                   wraplength=100)
    '''
    sort_text = "Sort"
    sort_button = tk.Button(window, 
                   text=sort_text, 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="#696969",
                   cursor="hand2",
                   disabledforeground="#323232",
                   fg="#D4D4D4",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="#444444",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=10,
                   wraplength=100)
    
    open_folder_text = "Open Folder"
    open_folder_button = tk.Button(window, 
                   text=open_folder_text, 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="#696969",
                   cursor="hand2",
                   disabledforeground="#323232",
                   fg="#D4D4D4",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="#444444",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=10,
                   wraplength=100)
    '''
    # Define textbox with file path
    
    #path_entry = tk.Text(window,font='Roboto')
    #path_entry.insert(path_name)

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
    path_entry.place(relx = 0.22,rely = 0.40)
    browse_button.place(relx= 0.22,rely=0.65)
    
    sort_button.place(relx=0.42,rely= 0.65)
    sort_button.config(state="disabled")
    open_folder_button.place(relx=0.62,rely=0.65)
    open_folder_button.config(state="disabled")
    
    window.mainloop()
browseFiles()