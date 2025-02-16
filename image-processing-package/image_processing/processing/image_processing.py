import cv2
import numpy as np
from matplotlib import pyplot as plt

def convert_to_grayscale(image):
    """
    Convierte una imagen a escala de grises.
    
    Parámetros:
        image (numpy.ndarray): Imagen en formato RGB.
    
    Retorna:
        numpy.ndarray: Imagen en escala de grises.
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def resize_image(image, width, height):
    """
    Redimensiona una imagen a las dimensiones dadas.
    
    Parámetros:
        image (numpy.ndarray): Imagen en formato RGB.
        width (int): Ancho deseado.
        height (int): Alto deseado.
    
    Retorna:
        numpy.ndarray: Imagen redimensionada.
    """
    return cv2.resize(image, (width, height))

def apply_blur(image, ksize=5):
    """
    Aplica un filtro de desenfoque (blur) a la imagen.
    
    Parámetros:
        image (numpy.ndarray): Imagen en formato RGB.
        ksize (int): Tamaño del kernel del filtro.
    
    Retorna:
        numpy.ndarray: Imagen con efecto de desenfoque.
    """
    return cv2.GaussianBlur(image, (ksize, ksize), 0)