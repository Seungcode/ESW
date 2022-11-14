import numpy as np
import cv2 as cv

class Enemy_2:
    def __init__(self):
        self.canvas = np.zeros((35, 35, 3), dtype = np.uint8)
        white = (255, 255, 255)
        brown = (132, 184, 224)
        cv.line(self.canvas, (1, 27), (1, 10), white)
        cv.line(self.canvas, (16, 27), (16, 10), white)
        cv.line(self.canvas, (18, 27), (18, 10), white)
        cv.line(self.canvas, (33, 27), (33, 10), white)
        cv.line(self.canvas, (2, 10), (1, 10), white)
        cv.line(self.canvas, (3, 9), (2, 9), white)
        cv.line(self.canvas, (4, 8), (3, 8), white)
        cv.line(self.canvas, (4, 7), (5, 7), white)
        cv.line(self.canvas, (6, 6), (11, 6), white)
        cv.line(self.canvas, (16, 10), (15, 10), white)
        cv.line(self.canvas, (15, 9), (14, 9), white)
        cv.line(self.canvas, (13, 8), (14, 8), white)
        cv.line(self.canvas, (12, 7), (13, 7), white)
        cv.line(self.canvas, (19, 10), (18, 10), white)
        cv.line(self.canvas, (20, 9), (19, 9), white)
        cv.line(self.canvas, (21, 8), (20, 8), white)
        cv.line(self.canvas, (21, 7), (22, 7), white)
        cv.line(self.canvas, (22, 6), (28, 6), white)
        cv.line(self.canvas, (33, 10), (32, 10), white)
        cv.line(self.canvas, (31, 9), (32, 9), white)
        cv.line(self.canvas, (30, 8), (31, 8), white)
        cv.line(self.canvas, (30, 7), (29, 7), white)

        cv.line(self.canvas, (3, 10), (14, 10), brown)
        cv.line(self.canvas, (4, 9), (13, 9), brown)
        cv.line(self.canvas, (5, 8), (12, 8), brown)
        cv.line(self.canvas, (6, 7), (11, 7), brown)
        cv.line(self.canvas, (20, 10), (31, 10), brown)
        cv.line(self.canvas, (21, 9), (30, 9), brown)
        cv.line(self.canvas, (22, 8), (29, 8), brown)
        cv.line(self.canvas, (23, 7), (28, 7), brown)
        cv.rectangle(self.canvas, (2, 28), (15, 11), brown, -1)
        cv.rectangle(self.canvas, (18, 28), (32, 11), brown, -1)
        cv.rectangle(self.canvas, (7, 18), (10, 23), white, -1)
        cv.rectangle(self.canvas, (11, 12), (13, 14), white, -1)
        cv.rectangle(self.canvas, (4, 12), (6, 14), white, -1)
        cv.rectangle(self.canvas, (24, 18), (27, 23), white, -1)
        cv.rectangle(self.canvas, (30, 12), (28, 14), white, -1)
        cv.rectangle(self.canvas, (21, 12), (23, 14), white, -1)

        cv.line(self.canvas, (34, 29), (0, 29), white)
        cv.line(self.canvas, (34, 30), (0, 30), white)
        cv.line(self.canvas, (34, 31), (0, 31), white)
        cv.line(self.canvas, (2, 28), (0, 28), white)
        cv.line(self.canvas, (4, 28), (6, 28), white)
        cv.line(self.canvas, (8, 28), (10, 28), white)
        cv.line(self.canvas, (12, 28), (14, 28), white)
        cv.line(self.canvas, (16, 28), (18, 28), white)
        cv.line(self.canvas, (20, 28), (22, 28), white)
        cv.line(self.canvas, (24, 28), (26, 28), white)
        cv.line(self.canvas, (28, 28), (30, 28), white)
        cv.line(self.canvas, (32, 28), (34, 28), white)