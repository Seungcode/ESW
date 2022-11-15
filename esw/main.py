from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageOps, ImageFilter
import time
import cv2 as cv
import random
import numpy as np
from colorsys import hsv_to_rgb
from Character import Character
from Joystick import Joystick
from Enemy_1 import Enemy_1
def main():
    white = (255, 255, 255)
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 255, 255, 255))

    enemy_1 = Character()
    joystick.disp.image(my_image)
    joystick.disp.image(enemy_1.shape)
        

        

if __name__ == '__main__':
    main()