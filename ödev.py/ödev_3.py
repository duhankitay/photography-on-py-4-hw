import tkinter as tk
from tkinter import filedialog
import numpy as np

def load_csv_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    data = np.genfromtxt(file_path, delimiter=',')
    return data

def apply_gaussian_filter(image):
    filter_kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]) / 16.0
    
    output_image = np.zeros((image.shape[0] - 2, image.shape[1] - 2))
    
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            sub_matrix = image[i-1:i+2, j-1:j+2]
            filtered_value = np.sum(sub_matrix * filter_kernel)
            output_image[i-1, j-1] = filtered_value
    
    return output_image

def main():
    image_data = load_csv_file()
    result_image = apply_gaussian_filter(image_data)
    print("Sonuç Matris:")
    print(result_image)

if __name__ == "__main__":
    main()
