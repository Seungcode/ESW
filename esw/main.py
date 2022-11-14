from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageOps, ImageFilter
import time
import cv2 as cv
import random
import numpy as np
from colorsys import hsv_to_rgb
from Character import Character
from Joystick import Joystick
from Enemy_boss import Enemy_boss
def main():
    white = (255, 255, 255)
    joystick = Joystick()
    canvas = np.zeros((240, 240, 3), dtype = np.uint8)
    my_image = cv.rectangle(canvas, (0,0), (240,240), (255,255,255), -1)
    enemy_1 = Character(my_image)
    canvas = cv.resize(canvas, dsize=(640, 640), interpolation=cv.INTER_AREA)
    canvas = canvas[200:440, 200:440].copy()
    canvas = Image.fromarray(canvas)
    joystick.disp.image(canvas)
        

        

if __name__ == '__main__':
    main()