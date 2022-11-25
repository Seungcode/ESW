import numpy as np
from PIL import Image, ImageDraw
import cv2 as cv
from BackGround import BackGround
class Character_1_1:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+70, position[1]+70))
        self.shape = Image.open("Rabbit_1_1.PNG").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position