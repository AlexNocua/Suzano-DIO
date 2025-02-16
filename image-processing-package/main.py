from image_processing.utils.image_utils import load_image, show_image
from image_processing.processing.image_processing import convert_to_grayscale, resize_image, apply_blur

if __name__ == "__main__":
    """
    Script de prueba para el paquete de procesamiento de imágenes.
    """
    image_path = "foto.jpg"
    image = load_image(image_path)
    show_image(image, "Imagen Original")
    gray_image = convert_to_grayscale(image)
    show_image(gray_image, "Imagen en Escala de Grises")
    resized_image = resize_image(image, 100, 100)
    show_image(resized_image, "Imagen Redimensionada")
    blurred_image = apply_blur(image)
    show_image(blurred_image, "Imagen Desenfocada")