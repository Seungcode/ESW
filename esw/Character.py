import numpy as np
import cv2 as cv
from BackGround import BackGround
from PIL import Image
class Character:
    def __init__(self, background):
        #토끼 (최종)
        self.canvas = background
        #self.position = np.array([BackGround.center[0]/2 - 20, BackGround.center[1]/2 - 20, BackGround.center[0]/2 + 20, BackGround.center[1]/2 + 20])
        #self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.state = None
        x=120
        y=120
        black = (0, 0, 0)
        white = (255, 255, 255)
        pink = (255, 192, 203)
        red = (255, 0, 0)
        #발
        cv.line(self.canvas, (x+12, y+40), (x+20, y+40), black)
        cv.line(self.canvas, (x+25, y+40), (x+33, y+40), black)

        cv.line(self.canvas, (x+12, y+40), (x+12, y+38), black)
        cv.line(self.canvas, (x+33, y+40), (x+33, y+38), black)

        cv.line(self.canvas, (x+12, y+38), (x+18, y+38), black)
        cv.line(self.canvas, (x+33, y+38), (x+27, y+38), black)

        cv.line(self.canvas, (x+17, y+38), (x+17, y+37), black)
        cv.line(self.canvas, (x+28, y+37), (x+28, y+38), black)

        cv.line(self.canvas, (x+20, y+37), (x+20, y+40), black)
        cv.line(self.canvas, (x+25, y+37), (x+25, y+40), black)
        #발 색칠
        cv.line(self.canvas, (x+13, y+39), (x+19, y+39), pink)
        cv.line(self.canvas, (x+26, y+39), (x+32, y+39), pink)
        cv.rectangle(self.canvas, (x+18, y+38), (x+29, y+37), pink, -1)
        cv.rectangle(self.canvas, (x+27, y+38), (x+26, y+37), pink, -1)
        #몸통
        cv.line(self.canvas, (x+15, y+36), (x+30, y+36), black)

        cv.line(self.canvas, (x+15, y+36), (x+15, y+35), black)
        cv.line(self.canvas, (x+30, y+36), (x+30, y+35), black)

        cv.line(self.canvas, (x+14, y+35), (x+15,y+35), black)
        cv.line(self.canvas, (x+30, y+35), (x+31, y+35), black)

        cv.line(self.canvas, (x+14, y+35), (x+14, y+34), black)
        cv.line(self.canvas, (x+31, y+35), (x+31, y+34), black)

        cv.line(self.canvas, (x+13, y+34), (x+14, y+34), black)
        cv.line(self.canvas, (x+32, y+34), (x+31, y+34), black)

        cv.line(self.canvas, (x+13, y+34), (x+13, y+31), black)
        cv.line(self.canvas, (x+32, y+34), (x+32, y+31), black)

        cv.line(self.canvas, (x+14, y+31), (x+13, y+31), black)
        cv.line(self.canvas, (x+31, y+31), (x+32, y+31), black)

        cv.line(self.canvas, (x+14, y+30), (x+14, y+31), black)
        cv.line(self.canvas, (x+31, y+30), (x+31, y+31), black)

        cv.line(self.canvas, (x+14, y+30), (x+15, y+30), black)
        cv.line(self.canvas, (x+31, y+30), (x+30, y+30), black)

        cv.line(self.canvas, (x+15, y+29), (x+15, y+30), black)
        cv.line(self.canvas, (x+30, y+29), (x+30, y+30), black)

        cv.line(self.canvas, (x+15, y+29), (x+17, y+29), black)
        cv.line(self.canvas, (x+30, y+29), (x+28, y+29), black)

        cv.line(self.canvas, (x+17, y+24), (x+17, y+29), black)
        cv.line(self.canvas, (x+28, y+24), (x+28, y+29), black)
        #몸통 색칠 
        cv.rectangle(self.canvas, (x+16, y+35), (x+29, y+30), pink, -1)
        cv.rectangle(self.canvas, (x+18, y+29), (x+27, y+24), pink, -1)
        cv.line(self.canvas, (x+15, y+34), (x+15, y+31), pink)
        cv.line(self.canvas, (x+30, y+34), (x+30, y+31), pink)
        cv.line(self.canvas, (x+14, y+33), (x+14, y+32), pink)
        cv.line(self.canvas, (x+31, y+33), (x+31, y+32), pink)
        #꼬리
        cv.rectangle(self.canvas, (x+22, y+34), (x+23, y+33), black)
        #얼굴
        cv.line(self.canvas, (x+15, y+23), (x+30, y+23), black)

        cv.line(self.canvas, (x+15, y+23), (x+15, y+22), black)
        cv.line(self.canvas, (x+30, y+23), (x+30, y+22), black)

        cv.line(self.canvas, (x+15, y+22), (x+14, y+22), black)
        cv.line(self.canvas, (x+30, y+22), (x+31, y+22), black)

        cv.line(self.canvas, (x+14, y+21), (x+14, y+22), black)
        cv.line(self.canvas, (x+31, y+21), (x+31, y+22), black)

        cv.line(self.canvas, (x+14, y+21), (x+13, y+21), black)
        cv.line(self.canvas, (x+31, y+21), (x+32, y+21), black)

        cv.line(self.canvas, (x+13, y+15), (x+13, y+21), black)
        cv.line(self.canvas, (x+32, y+15), (x+32, y+21), black)

        cv.line(self.canvas, (x+13, y+15), (x+14, y+15), black)
        cv.line(self.canvas, (x+31, y+15), (x+32, y+15), black)

        cv.line(self.canvas, (x+14, y+14), (x+14, y+15), black)
        cv.line(self.canvas, (x+31, y+14), (x+31, y+15), black)

        cv.line(self.canvas, (x+14, y+14), (x+16, y+14), black)
        cv.line(self.canvas, (x+31, y+14), (x+29, y+14), black)

        cv.line(self.canvas, (x+16, y+7), (x+16, y+14), black)
        cv.line(self.canvas, (x+14, y+7), (x+16, y+7), black)

        cv.line(self.canvas, (x+13, y+5), (x+13, y+6), black)

        cv.line(self.canvas, (x+14, y+4), (x+19,y+4), black)

        cv.line(self.canvas, (x+19, y+11), (x+19, y+4), black)

        cv.line(self.canvas, (x+19, y+11), (x+26, y+11), black)

        cv.line(self.canvas, (x+26, y+1), (x+26, y+11), black)

        cv.line(self.canvas, (x+27, y+0), (x+28, y+0), black)

        cv.line(self.canvas, (x+29, y+1), (x+29, y+14), black)
        #얼굴 색칠
        cv.rectangle(self.canvas, (x+16, y+22), (x+29, y+15), pink, -1)
        cv.rectangle(self.canvas, (x+17, y+14), (x+28, y+12), pink, -1)
        cv.rectangle(self.canvas, (x+27, y+1), (x+28, y+11), pink, -1)
        cv.rectangle(self.canvas, (x+17, y+13), (x+18, y+5), pink, -1)
        cv.rectangle(self.canvas, (x+16, y+6), (x+14, y+5), pink, -1)
        cv.line(self.canvas, (x+15, y+22), (x+15, y+15), pink)
        cv.line(self.canvas, (x+30, y+22), (x+30, y+15), pink)
        cv.line(self.canvas, (x+14, y+21), (x+14, y+16), pink)
        cv.line(self.canvas, (x+31, y+21), (x+31, y+16), pink)
        #꼬리
        cv.line(self.canvas, (x+26, y+10), (x+26, y+11), red)
        cv.line(self.canvas, (x+25, y+11), (x+26, y+11), red)
        cv.line(self.canvas, (x+28, y+10), (x+28, y+11), red)
        cv.line(self.canvas, (x+29, y+11), (x+28, y+11), red)
        cv.line(self.canvas, (x+26, y+14), (x+26, y+13), red)
        cv.line(self.canvas, (x+25, y+13), (x+26, y+13), red)
        cv.line(self.canvas, (x+29, y+14), (x+29, y+13), red)
        cv.line(self.canvas, (x+28, y+13), (x+29, y+13), red)
    
