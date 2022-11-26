from PIL import Image
import cv2 as cv
import numpy as np

class Enemy_1:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+24, position[1]+24))
        self.shape = Image.open("Enemy1.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0], position[1], position[0] + 20, position[1] + 20])
        self.touch = 1
        self.life = 15
        self.position = position

    def death(self, background):
        self.touch = 0
        self.shape = background.crop((self.position[0], self.position[1], self.position[0]+24, self.position[1]+24))
