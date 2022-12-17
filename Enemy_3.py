from PIL import Image
import cv2 as cv
import numpy as np

class Enemy_3:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+70, position[1]+70))
        self.shape = Image.open("Enemy3.PNG").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0] + 20, position[1] + 20 , position[0] + 65, position[1] + 65])
        self.touch = 1
        self.state = 'live'
        self.deathtime = 0
        self.life = 50
        self.life_ = 50
        self.position = position

    def death(self, background):
        self.state = 'death'
        self.shape = background.crop((self.position[0], self.position[1], self.position[0]+70, self.position[1]+70))
