import numpy as np
import cv2 as cv

class Enemy_1:
    def __init__(self):
        self.canvas = np.zeros((25, 25, 3), dtype = np.uint8)
        self.health = 3
        self.state = 'alive'
        white = (255, 255, 255)
        brown = (224, 184, 132)
        cv.line(self.canvas, (6,22), (6,11),white)
        cv.line(self.canvas, (20,22), (20,11),white)
        cv.line(self.canvas, (7,11), (6,11),white)
        cv.line(self.canvas, (20,11), (19,11),white)
        cv.line(self.canvas, (7,10), (7,11),white)
        cv.line(self.canvas, (19,10), (19,11),white)
        cv.line(self.canvas, (7,10), (8,10),white)
        cv.line(self.canvas, (19,10), (18,10),white)
        cv.line(self.canvas, (8,9), (8,10),white)
        cv.line(self.canvas, (18,9), (18,10),white)
        cv.line(self.canvas, (8,9), (9,9),white)
        cv.line(self.canvas, (18,9), (17,9),white)
        cv.line(self.canvas, (9,8), (9,9),white)
        cv.line(self.canvas, (17,8), (17,9),white)
        cv.line(self.canvas, (9,8), (17,8),white)

        cv.rectangle(self.canvas, (7, 22), (19, 12), brown, -1)
        cv.line(self.canvas, (8,11), (18,11),brown)
        cv.line(self.canvas, (9,10), (17,10),brown)
        cv.line(self.canvas, (10,9), (16,9),brown)

        cv.line(self.canvas, (10,18), (10,17),white)
        cv.line(self.canvas, (16,18), (16,17),white)
        cv.line(self.canvas, (11,19), (15,19),white)
        cv.rectangle(self.canvas, (10, 13), (11, 14), white, -1)
        cv.rectangle(self.canvas, (16, 13), (15, 14), white, -1)

        cv.line(self.canvas, (4,23), (22,23),white)
        cv.line(self.canvas, (5,22), (6,22),white)
        cv.line(self.canvas, (8,22), (9,22),white)
        cv.line(self.canvas, (11,22), (12,22),white)
        cv.line(self.canvas, (14,22), (15,22),white)
        cv.line(self.canvas, (17,22), (18,22),white)
        cv.line(self.canvas, (20,22), (21,22),white)