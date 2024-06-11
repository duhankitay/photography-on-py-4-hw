
import numpy as np

intensity_values = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
pixel_counts = [12, 18, 32, 48, 52, 65, 55, 42, 32, 16, 10, 5, 18, 25, 32, 40, 65, 43, 32, 20, 10, 4]

min_intensity = min(intensity_values)
max_intensity = max(intensity_values)

histogram = np.zeros(max_intensity - min_intensity + 1)
for intensity, count in zip(intensity_values, pixel_counts):
    histogram[intensity - min_intensity] = count

total_pixels = sum(pixel_counts)

current_max, threshold = 0, 0
sum_total, sum_foreground, weight_background, weight_foreground = 0, 0, 0, 0

for t in range(0, len(histogram)):
    sum_total += t * histogram[t]

for t in range(0, len(histogram)):
    weight_background += histogram[t]
    if weight_background == 0:
        continue
    weight_foreground = total_pixels - weight_background
    if weight_foreground == 0:
        break

    sum_foreground += t * histogram[t]
    mean_background = sum_foreground / weight_background
    mean_foreground = (sum_total - sum_foreground) / weight_foreground

    between_class_variance = weight_background * weight_foreground * (mean_background - mean_foreground) ** 2

    if between_class_variance > current_max:
        current_max = between_class_variance
        threshold = t

print(f"En uygun eşik değeri: {threshold + min_intensity}")

