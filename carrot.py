import numpy as np
from PIL import Image, ImageDraw
import cv2 as cv
from BackGround import BackGround
from PIL import Image
class carrot:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+100, position[1]+100))
        self.shape = Image.open("carrot.PNG").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.safe = np.array([position[0]+30, position[1]+30 , position[0] + 70, position[1] + 70])
        self.position = position

    def collision_check(self, character):
        collision = self.overlap(character.safe, self.safe)
        return collision

    def overlap(self, ego_position, other_position):
        return (other_position[2] >ego_position[0] > other_position[0] or other_position[2] >= ego_position[2] >= other_position[0]) and (ego_position[1] <= ego_position[1] <= other_position[3] or other_position[1] <= ego_position[3] <= other_position[3])