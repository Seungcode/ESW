from PIL import Image
import cv2 as cv
import numpy as np

class Enemy_1:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+24, position[1]+24))
        self.shape = Image.open("Enemy1.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0] + 5, position[1] + 5 , position[0] + 10, position[1] + 10])
        self.position = position