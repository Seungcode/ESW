from PIL import Image
import cv2 as cv
import numpy as np

class life:
    def __init__(self, character, background):
        shape_ = Image.open("life.png").convert('RGBA')
        self.shape = Image.open("life.png").convert('RGBA')
        shape = self.shape
        self.heart = Image.open("heart.png").convert('RGBA')
        self.position = (14, 10)
        for i in range (character.life):
            self.shape.paste(self.heart, (i*15+5, 2))