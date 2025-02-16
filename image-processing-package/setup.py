"""
Paquete de Procesamiento de Imágenes
=====================================
Este paquete proporciona funcionalidades básicas para el procesamiento de imágenes, incluyendo:
- Carga y visualización de imágenes.
- Conversión a escala de grises.
- Redimensionamiento.
- Aplicación de desenfoque (blur).

Estructura del paquete:
- **processing/image_processing.py**: Funciones para manipulación de imágenes.
- **utils/image_utils.py**: Funciones utilitarias para carga y visualización de imágenes.
- **main.py**: Script de prueba para ejecutar las funcionalidades del paquete.
"""

from setuptools import setup, find_packages

with open ("readme.md", "r") as f:
    page_description = f.read()



setup(
    name="image_processing_package_by_alexnocua",  
    version="0.1.1",
    author="Alex Eduarod Nocua Sema",
    author_email="nocua68@gmail.com",
    description="Un paquete para procesamiento básico de imágenes",
    long_description=open("readme.md", encoding="utf-8").read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/AlexNocua/Suzano-DIO/tree/master/image-processing-package",  
    packages=find_packages(),  
    install_requires=[
        "numpy",
        "opencv-python",
        "matplotlib"
    ],     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
