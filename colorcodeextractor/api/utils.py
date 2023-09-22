import cv2
import numpy as np

def extract_colors(image_data):
    color_vals = {}
    img = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
    pixels = img.reshape((-1, 3))
    num_colors = 10
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels.astype(np.float32), num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    color_labels = {
    'URO': [206, 193, 187],
    'BIL': [202, 185, 164],
    'KET': [193, 171, 153],
    'BLD': [204, 159, 54],
    'PRO': [191, 172, 130],
    'NIT': [203, 189, 170],
    'LEU': [194, 175, 164],
    'GLU': [128, 173, 163],
    'SG': [191, 159, 76],
    'PH': [206, 152, 106]
    }
    extracted_colors = {}
    for center in centers:
        min_distance = float('inf')
        dominant_label = None

        for label, color in color_labels.items():
            distance = np.linalg.norm(np.array(center) - np.array(color))
            if distance < min_distance:
                min_distance = distance
                dominant_label = label

        extracted_colors[dominant_label] = center
    for label, color in extracted_colors.items():
        r, g, b = color
        color_vals[label] = [r, g, b]
    return color_vals
