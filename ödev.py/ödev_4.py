import numpy as np

intensity_values = np.array([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150])
pixel_counts = np.array([12, 18, 32, 48, 52, 65, 55, 42, 32, 16, 10, 5, 18, 25, 32, 40, 65, 43, 32, 20, 10, 4])

T0 = 100
threshold = 1
T1 = T0

while True:
 
    G1 = intensity_values[intensity_values > T0]
    G2 = intensity_values[intensity_values <= T0]
  
    G1_pixel_counts = pixel_counts[intensity_values > T0]
    G2_pixel_counts = pixel_counts[intensity_values <= T0]
    
    m1 = np.sum(G1 * G1_pixel_counts) / np.sum(G1_pixel_counts)
    m2 = np.sum(G2 * G2_pixel_counts) / np.sum(G2_pixel_counts)

    T1 = (m1 + m2) / 2
    
    if abs(T1 - T0) < threshold:
        break
    else:
        T0 = T1

print(f"Optimum Eşik Değeri: {T1}")
