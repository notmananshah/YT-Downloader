from pytube import YouTube
from sys import argv
import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
import os

# conversion logic
def convert():
    input_data = entry_link.get()
    yt = YouTube(input_data)
    yd = yt.streams.get_highest_resolution()
    
    # Get the user's Desktop folder path
    desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
    
    #set the output file path to the Desktop folder with the filename the same as the video title
    output_file_path = os.path.join(desktop_folder, yt.title)
    yd.download(output_file_path)
    
    #set the output string
    output_string.set(f"Video downloaded to {output_file_path}")
    
# window
window = ttk.Window(themename= "darkly")
window.title("YouTube Downloader")
window.geometry("600x200")

# title
title_label = ttk.Label(master = window, text = "Enter link to download video", font = "Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_link = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_link)
button = ttk.Button(master = input_frame, text = "Download", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# output the video details
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font = "Calibri 16", textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()


