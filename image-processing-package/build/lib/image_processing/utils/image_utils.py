import cv2
import numpy as np
from matplotlib import pyplot as plt

def load_image(image_path):
    """Carga una imagen desde la ruta dada."""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("No se pudo cargar la imagen. Verifica la ruta.")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def show_image(image, title="Imagen"):
    """Muestra una imagen utilizando Matplotlib."""
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()