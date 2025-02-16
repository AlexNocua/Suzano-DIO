def load_image(image_path):
    """
    Carga una imagen desde la ruta dada.
    
    Parámetros:
        image_path (str): Ruta de la imagen.
    
    Retorna:
        numpy.ndarray: Imagen en formato RGB.
    
    Lanza:
        ValueError: Si la imagen no se pudo cargar.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("No se pudo cargar la imagen. Verifica la ruta.")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def show_image(image, title="Imagen"):
    """
    Muestra una imagen utilizando Matplotlib.
    
    Parámetros:
        image (numpy.ndarray): Imagen en formato RGB o escala de grises.
        title (str): Título de la imagen mostrada.
    """
    plt.imshow(image, cmap='gray' if len(image.shape) == 2 else None)
    plt.title(title)
    plt.axis("off")
    plt.show()