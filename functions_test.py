import pytest
from notebook import *

import pandas as pd
import numpy as np
from PIL import Image, ImageFilter
import os

open_image = Image.open("images/pexels-carlosdetrip-16131605.jpg")
all_images = [open_image]

"""
Testes para as funções do notebook.py
"""

# Teste para a função de redimensionamento de imagens
def test_resize_image():
    expected_size = (1000, 1000)
    resized_images = resize_image(all_images)
    for image in resized_images:
        assert image.size == expected_size

# Teste para a função de aplicação do filtro de desfoque
def test_filter_blur():
    blurred_images = filter_blur(all_images)
    for image in blurred_images:
        assert isinstance(image, Image.Image)  # Verifica se cada elemento da lista é uma instância de Image.Image

# Teste para a função de conversão de imagens para tons de cinza
def test_gray_scale():
    grayscale_images = gray_scale(all_images)
    for image in grayscale_images:
        assert image.mode == 'L'  # Verifica se o modo de cada imagem é 'L' (tons de cinza)

# Teste para a função de transformação das imagens em arrays numpy
def test_transform_in_numpy():
    numpy_arrays = transform_in_numpy(all_images)
    for array in numpy_arrays:
        assert isinstance(array, np.ndarray)  # Verifica se cada elemento da lista é um array numpy

# Teste para a função de normalização dos valores dos pixels das imagens
def test_normalize():
    normalized_images = normalize(all_images)
    for image in normalized_images:
        assert np.max(image) <= 1.0  # Verifica se o valor máximo de cada imagem é menor ou igual a 1.0

if __name__ == '__main__':
    pytest.main()

