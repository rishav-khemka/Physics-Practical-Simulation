from tkinter import Tk
from tkinter import filedialog
import os

#root = Tk(); root.withdraw()
current_directory = filedialog.askdirectory()
file_name = "test.txt"

file_path = os.path.join(current_directory,file_name)
print(file_path)