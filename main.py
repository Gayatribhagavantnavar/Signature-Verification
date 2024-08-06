import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
import cv2
from signature import match  # Assuming match is a function in signature.py that compares two images

THRESHOLD = 85  # Threshold for matching similarity percentage

# Function to open a file dialog and get the file path
def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)

# Function to check the similarity between two signatures
def checkSimilarity(window, path1, path2):
    result = match(path1=path1, path2=path2)  # Call the match function from signature.py
    if result <= THRESHOLD:
        messagebox.showerror("Failure: Signatures Do Not Match", "Signatures do not match!")
    else:
        messagebox.showinfo("Success: Signatures Match", "Signatures match!")
    return True

# Setting up the main window
root = tk.Tk()
root.title("Signature Matching")
root.geometry("500x700")
root.configure(bg='cyan')

# Adding labels, entry fields, and buttons to the window
uname_label = tk.Label(root, text="Compare Two Signatures:", font=10)
uname_label.place(x=90, y=50)

img1_message = tk.Label(root, text="Signature 1", font=10)
img1_message.place(x=10, y=120)

image1_path_entry = tk.Entry(root, font=10)
image1_path_entry.place(x=150, y=120)

img1_browse_button = tk.Button(
    root, text="Browse", font=10, command=lambda: browsefunc(ent=image1_path_entry))
img1_browse_button.place(x=400, y=120)

img2_message = tk.Label(root, text="Signature 2", font=10)
img2_message.place(x=10, y=250)

image2_path_entry = tk.Entry(root, font=10)
image2_path_entry.place(x=150, y=250)

img2_browse_button = tk.Button(
    root, text="Browse", font=10, command=lambda: browsefunc(ent=image2_path_entry))
img2_browse_button.place(x=400, y=250)

compare_button = tk.Button(
    root, text="Compare", font=10, command=lambda: checkSimilarity(window=root,
                                                                   path1=image1_path_entry.get(),
                                                                   path2=image2_path_entry.get(),))

compare_button.place(x=200, y=320)

root.mainloop()  # Start the Tkinter main loop
