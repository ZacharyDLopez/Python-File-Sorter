from tkinter import *
from tkinter import filedialog

def browseFiles():
    #filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    
    #label_file_explorer.configure(text="File Opened: "+filename)
    window = Tk()
    window.title("File Sorter")
    window.geometry("500x500")
    window.config(bg="black")
    
    label_file_explorer = Label(window, text="File Explorer using Tkinter", width=100, height=4, fg="blue")
    button_explore = Button(window, text="Browse Files", command=browseFiles)
    
    button_explore.pack(pady=20)
    label_file_explorer.pack(pady=20)
    
    window.mainloop()
browseFiles()