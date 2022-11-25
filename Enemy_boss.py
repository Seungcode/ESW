from PIL import Image
import cv2 as cv
import numpy as np

class Enemy_boss:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+80, position[1]+80))
        self.shape = Image.open("EnemyBoss.PNG").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0] + 5, position[1] + 5 , position[0] + 70, position[1] +70])
        self.position = position