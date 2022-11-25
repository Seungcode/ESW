import numpy as np
from PIL import Image

class BackGround:
    def __init__(self):
        self.shape = Image.open("background.png").convert('RGBA')
        self.position = (119, 259)
    def move(self, command = None):
        self.list = list(self.position)
        if command['move'] == False:
            self.state = None
        else:
            self.state = 'move'

            if command['up_pressed']:
                if(self.list[1]>-50):
                    self.list[1] -= 5
                else:
                    self.list[1] = self.list[1]

            if command['down_pressed']:
                if(self.list[1]<259):
                    self.list[1] += 5
                else:
                    self.list[1] = self.list[1]

            if command['left_pressed']:
                if(self.list[0]>0):
                    self.list[0] -= 5
                else:
                    self.list[0] = self.list[0]
                
            if command['right_pressed']:
                if(self.list[0]<259):
                    self.list[0] += 5
                else:
                    self.list[0] = self.list[0]
        self.position = tuple(self.list)