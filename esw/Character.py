import numpy as np
from PIL import Image, ImageDraw
import cv2 as cv
from BackGround import BackGround
from PIL import Image
class Character:
    def __init__(self):
        my_image = Image.new("RGBA", (90,90))
        my_draw = ImageDraw.Draw(my_image)
        my_draw.rectangle((0, 0, 90, 90), fill=(255, 255, 255, 255))
        self.shape = Image.open("Rabbit.png").convert('RGBA')
        self.shape = Image.alpha_composite(my_image, self.shape)