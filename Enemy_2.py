from PIL import Image
import cv2 as cv
import numpy as np

class Enemy_2:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+50, position[1]+50))
        self.shape = Image.open("Enemy2.PNG").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0] + 10, position[1] + 10 , position[0] + 45, position[1] + 45])
        self.touch = 1
        self.state = 'live'
        self.deathtime = 0
        self.life = 30
        self.life_ = 30
        self.position = position

    def death(self, background):
        self.state = 'death'
        self.shape_ = background.crop((self.position[0], self.position[1], self.position[0]+50, self.position[1]+50))
