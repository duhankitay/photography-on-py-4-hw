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
    hist = np.zeros(256, dtype=int)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            hist[data[i, j]] += 1
    cdf = np.zeros(256, dtype=int)
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    cdf_min = cdf.min()
    M, N = data.shape
    L = 256 
    equalized_image = np.zeros_like(data)
    for i in range(M):
        for j in range(N):
            v = data[i, j]
            equalized_image[i, j] = round(((cdf[v] - cdf_min) / ((M * N) - cdf_min)) * (L - 1))
    for row in equalized_image:
        print(' '.join(map(str, row)))
else:
    print("Hiçbir dosya seçilmedi.")
