import pandas as pd
import numpy as np
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import os

# Lista para armazenar todas as imagens carregadas
all_images = []

# Função para carregar arquivos de imagem da pasta 'images'
def load_files():
    folder = os.listdir("images")  # Lista todos os arquivos na pasta 'images'

    for archive in folder:
        full_path = os.path.join("images", archive)  # Caminho completo para o arquivo de imagem
        load = Image.open(full_path)  # Abre o arquivo de imagem
        all_images.append(load)  # Adiciona a imagem à lista 'all_images'

load_files()  # Chama a função para carregar os arquivos de imagem

# Função para redimensionar todas as imagens para o tamanho oficial
def resize_image(all_images):
    official_size = (1000, 1000)  # Tamanho oficial desejado
    for image in range(len(all_images)):
        all_images[image] = all_images[image].resize(official_size)  # Redimensiona a imagem
    return all_images

result_resize = resize_image(all_images)  # Chama a função de redimensionamento

# Função para aplicar o filtro de desfoque em todas as imagens
def filter_blur(all_images):
    for i in range(len(all_images)):
        all_images[i] = all_images[i].filter(ImageFilter.BLUR) # aplica o filtro de desfoque
    return all_images

result_blur = filter_blur(result_resize)  # Chama a função para aplicar o filtro de desfoque

# Função para converter imagens para tons de cinza
def gray_scale(all_images):
    for i in range(len(all_images)):
        all_images[i] = all_images[i].convert("L")  # Converte a imagem para tons de cinza
    
    return all_images

result_gray = gray_scale(result_blur)

# Função para transformar todas as imagens em arrays numpy
def transform_in_numpy(all_images):
    for image in range(len(all_images)):
        all_images[image] = np.array(all_images[image])  # Transforma a imagem em um array numpy
    return all_images

result_transform_numpy = transform_in_numpy(result_gray)  # Chama a função para transformar as imagens em arrays numpy

# Função para normalizar os valores dos pixels de todas as imagens
def normalize(all_images):
    for image in range(len(all_images)):
        all_images[image] = all_images[image] / 255  # Normaliza os valores dos pixels
    return all_images

result_normalize = normalize(result_transform_numpy)  # Chama a função para normalizar os valores dos pixels

# Achatar (flatten) os arrays numpy para uma dimensão
flattened_arrays = [array.flatten() for array in result_normalize]

# Criação do DataFrame do Pandas
df = pd.DataFrame(flattened_arrays)