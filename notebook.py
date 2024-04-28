import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

all_images = []

def load_files():
    folder = os.listdir("images")

    for archive in folder:
        full_path = os.path.join("images", archive)
        load = Image.open(full_path)
        all_images.append(load)

    print(all_images)

def crop_image(all_images):
    pass

def blur_image(all_images):
    pass

def transform_in_numpy(all_images):
    pass

def normalize(all_images):
    pass
