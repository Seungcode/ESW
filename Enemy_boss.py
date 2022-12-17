from PIL import Image
import cv2 as cv
import numpy as np

class Enemy_boss:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+80, position[1]+80))
        self.shape = Image.open("EnemyBoss.PNG").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0] + 20, position[1] + 20 , position[0] + 70, position[1] +80])
        self.touch = 5
        self.state = 'live'
        self.deathtime = 0
        self.life = 100
        self.life_ = 100
        self.position = position

    def death(self, background):
        self.state = 'death'
        self.shape_ = background.crop((self.position[0], self.position[1], self.position[0]+80, self.position[1]+80))