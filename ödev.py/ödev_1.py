import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np

def load_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

file_path = load_file()
if file_path:
    data = pd.read_csv(file_path, header=None).values
    min_val = np.min(data)
    max_val = np.max(data)
    L = 256
    stretched_image = (data - min_val) / (max_val - min_val) * (L - 1)
    stretched_image = stretched_image.astype(int)
    
    for row in stretched_image:
        print(' '.join(map(str, row)))

else:
    print("Hiçbir dosya seçilmedi.")
