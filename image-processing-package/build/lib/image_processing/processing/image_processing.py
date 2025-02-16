import cv2
import numpy as np
from matplotlib import pyplot as plt

def convert_to_grayscale(image):
    """Convierte una imagen a escala de grises."""
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def resize_image(image, width, height):
    """Redimensiona una imagen a las dimensiones dadas."""
    return cv2.resize(image, (width, height))

def apply_blur(image, ksize=5):
    """Aplica un filtro de desenfoque (blur) a la imagen."""
    return cv2.GaussianBlur(image, (ksize, ksize), 0)