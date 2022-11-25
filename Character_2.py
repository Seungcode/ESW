import numpy as np
from PIL import Image, ImageDraw
import cv2 as cv
from BackGround import BackGround
from PIL import Image
class Character_2:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+70, position[1]+70))
        self.shape = Image.open("Rabbit_2.PNG").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.life = 5
        self.safe = np.array([position[0] + 10, position[1] + 5 , position[0] + 50, position[1] + 65])
        self.level = 1
        self.position = position