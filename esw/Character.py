import numpy as np
import cv2 as cv
from BackGround import BackGround
class Character:
    def __init__(self):
        self.canvas = np.zeros((40, 40, 3), dtype = np.uint8)
        self.position = np.array([BackGround.center[0]/2 - 20, BackGround.center[1]/2 - 20, BackGround.center[0]/2 + 20, BackGround.center[1]/2 + 20])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.state = None
        white = (255, 255, 255)
        pink = (203, 192, 255)
        red = (0, 0, 255)
        #발
        cv.line(self.canvas, (12, 40), (20, 40), white)
        cv.line(self.canvas, (25, 40), (33, 40), white)

        cv.line(self.canvas, (12, 40), (12, 38), white)
        cv.line(self.canvas, (33, 40), (33, 38), white)

        cv.line(self.canvas, (12, 38), (18, 38), white)
        cv.line(self.canvas, (33, 38), (27, 38), white)

        cv.line(self.canvas, (17, 38), (17, 37), white)
        cv.line(self.canvas, (28, 37), (28, 38), white)

        cv.line(self.canvas, (20, 37), (20, 40), white)
        cv.line(self.canvas, (25, 37), (25, 40), white)
        #발 색칠
        cv.line(self.canvas, (13, 39), (19, 39), pink)
        cv.line(self.canvas, (26, 39), (32, 39), pink)
        cv.rectangle(self.canvas, (19, 38), (20, 37), pink, -1)
        cv.rectangle(self.canvas, (27, 38), (26, 37), pink, -1)
        #몸통
        cv.line(self.canvas, (15, 36), (34, 36), white)

        cv.line(self.canvas, (15, 36), (15, 35), white)
        cv.line(self.canvas, (30, 36), (30, 35), white)

        cv.line(self.canvas, (14, 35), (15, 35), white)
        cv.line(self.canvas, (30, 35), (31, 35), white)

        cv.line(self.canvas, (14, 35), (14, 34), white)
        cv.line(self.canvas, (31, 35), (31, 34), white)

        cv.line(self.canvas, (13, 34), (14, 34), white)
        cv.line(self.canvas, (32, 34), (31, 34), white)

        cv.line(self.canvas, (13, 34), (13, 31), white)
        cv.line(self.canvas, (32, 34), (32, 31), white)

        cv.line(self.canvas, (14, 31), (13, 31), white)
        cv.line(self.canvas, (31, 31), (32, 31), white)

        cv.line(self.canvas, (14, 30), (14, 31), white)
        cv.line(self.canvas, (31, 30), (31, 31), white)

        cv.line(self.canvas, (14, 30), (15, 30), white)
        cv.line(self.canvas, (31, 30), (30, 30), white)

        cv.line(self.canvas, (15, 29), (15, 30), white)
        cv.line(self.canvas, (30, 29), (30, 30), white)

        cv.line(self.canvas, (15, 29), (17, 29), white)
        cv.line(self.canvas, (30, 29), (28, 29), white)

        cv.line(self.canvas, (17, 24), (17, 29), white)
        cv.line(self.canvas, (30, 24), (30, 29), white)
        #몸통 색칠 
        cv.rectangle(self.canvas, (16, 35), (29, 30), pink, -1)
        cv.rectangle(self.canvas, (18, 29), (27, 24), pink, -1)
        cv.line(self.canvas, (15, 34), (15, 31), pink)
        cv.line(self.canvas, (30, 34), (30, 31), pink)
        cv.line(self.canvas, (14, 33), (14, 32), pink)
        cv.line(self.canvas, (31, 33), (31, 32), pink)
        #꼬리
        cv.rectangle(self.canvas, (22, 34), (23, 33), white)
        #얼굴
        cv.line(self.canvas, (15, 23), (30, 23), white)

        cv.line(self.canvas, (15, 23), (15, 22), white)
        cv.line(self.canvas, (30, 23), (30, 22), white)

        cv.line(self.canvas, (15, 22), (14, 22), white)
        cv.line(self.canvas, (30, 22), (31, 22), white)

        cv.line(self.canvas, (14, 21), (14, 22), white)
        cv.line(self.canvas, (31, 21), (31, 22), white)

        cv.line(self.canvas, (14, 21), (13, 21), white)
        cv.line(self.canvas, (31, 21), (32, 21), white)

        cv.line(self.canvas, (13, 15), (13, 21), white)
        cv.line(self.canvas, (32, 15), (32, 21), white)

        cv.line(self.canvas, (13, 15), (14, 15), white)
        cv.line(self.canvas, (31, 15), (32, 15), white)

        cv.line(self.canvas, (14, 14), (14, 15), white)
        cv.line(self.canvas, (31, 14), (31, 15), white)

        cv.line(self.canvas, (14, 14), (16, 14), white)
        cv.line(self.canvas, (31, 14), (29, 14), white)

        cv.line(self.canvas, (16, 7), (16, 14), white)
        cv.line(self.canvas, (14, 7), (16, 7), white)

        cv.line(self.canvas, (13, 5), (13, 6), white)

        cv.line(self.canvas, (14, 4), (19, 4), white)

        cv.line(self.canvas, (19, 11), (19, 4), white)

        cv.line(self.canvas, (19, 11), (26, 11), white)

        cv.line(self.canvas, (26, 1), (26, 11), white)

        cv.line(self.canvas, (27, 0), (28, 0), white)

        cv.line(self.canvas, (29, 1), (29, 14), white)
        #몸통 색칠
        cv.rectangle(self.canvas, (16, 22), (29, 15), pink, -1)
        cv.rectangle(self.canvas, (17, 14), (28, 12), pink, -1)
        cv.rectangle(self.canvas, (27, 1), (28, 11), pink, -1)
        cv.rectangle(self.canvas, (17, 13), (18, 5), pink, -1)
        cv.rectangle(self.canvas, (16, 6), (14, 5), pink, -1)
        cv.line(self.canvas, (15, 23), (15, 15), pink)
        cv.line(self.canvas, (30, 23), (30, 15), pink)
        cv.line(self.canvas, (14, 22), (14, 16), pink)
        cv.line(self.canvas, (31, 22), (31, 16), pink)
        #꼬리
        cv.line(self.canvas, (26, 10), (26, 11), red)
        cv.line(self.canvas, (25, 11), (26, 11), red)
        cv.line(self.canvas, (28, 10), (28, 11), red)
        cv.line(self.canvas, (29, 11), (28, 11), red)
        cv.line(self.canvas, (26, 14), (26, 13), red)
        cv.line(self.canvas, (25, 13), (26, 13), red)
        cv.line(self.canvas, (29, 14), (29, 13), red)
        cv.line(self.canvas, (28, 13), (29, 13), red)