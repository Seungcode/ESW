import numpy as np
import cv2 as cv

class BackGround:
    def __init__(self):
        self.appearance = 'regtangle'
        self.canvas = np.zeros((1000, 1000, 3), dtype = np.uint8)
        self.position = np.array(375, 1000, 625, 750)

        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        cv.rectangle(self.canvas, (0,0), (1000, 1000), (0,255,0), -1)
    
    def move(self, command = None):
        if command['move'] == False:
            self.state = None
        
        else:
            self.state = 'move'

            if command['up_pressed']:
                self.position[1] -= 5
                self.position[3] -= 5

            if command['down_pressed']:
                self.position[1] += 5
                self.position[3] += 5

            if command['left_pressed']:
                self.position[0] -= 5
                self.position[2] -= 5
                
            if command['right_pressed']:
                self.position[0] += 5
                self.position[2] += 5