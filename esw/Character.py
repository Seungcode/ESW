import numpy as np
import cv2 as cv

class Character:
    def __init__(self, width, height):
        self.canvas = np.zeros((255, 255, 3), dtype = np.uint8)
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.state = None
        white = (255, 255, 255)
        pink = (203, 192, 255)
        red = (0, 0, 255)
        #발
        cv.line(self.canvas, (112, 139), (120, 139), white)   
        cv.line(self.canvas, (123, 139), (131, 139), white)

        cv.line(self.canvas, (111, 138), (112, 138), white)
        cv.line(self.canvas, (120, 138), (123, 138), white)
        cv.line(self.canvas, (131, 138), (132, 138), white)

        cv.line(self.canvas, (111, 138), (111, 136), white)
        cv.line(self.canvas, (132, 138), (132, 136), white)

        cv.line(self.canvas, (111, 136), (113, 136), white)
        cv.line(self.canvas, (130, 136), (132, 136), white)
    
        cv.line(self.canvas, (121, 138), (121, 135), white)
        cv.line(self.canvas, (122, 138), (122, 135), white)

        cv.line(self.canvas, (113, 135), (116, 135), white)
        cv.line(self.canvas, (127, 135), (130, 135), white)
        # 발 색칠 코드
        cv.line(self.canvas, (112, 138), (119, 138), pink)
        cv.line(self.canvas, (124, 138), (131, 138), pink)
        cv.line(self.canvas, (112, 137), (120, 137), pink)
        cv.line(self.canvas, (123, 137), (131, 137), pink)
        cv.line(self.canvas, (114, 136), (120, 136), pink)
        cv.line(self.canvas, (123, 136), (129, 136), pink)
        cv.line(self.canvas, (117, 135), (120, 135), pink)
        cv.line(self.canvas, (123, 135), (126, 135), pink)

        #몸통
        cv.line(self.canvas, (113, 134), (130, 134), white)

        cv.line(self.canvas, (112, 133), (113, 133), white)
        cv.line(self.canvas, (130, 133), (131, 133), white)

        cv.line(self.canvas, (111, 132), (112, 132), white)
        cv.line(self.canvas, (131, 132), (132, 132), white)
    
        cv.line(self.canvas, (111, 132), (111, 127), white)
        cv.line(self.canvas, (132, 132), (132, 127), white)

        cv.line(self.canvas, (111, 127), (112, 127), white)
        cv.line(self.canvas, (132, 127), (131, 127), white)

        cv.line(self.canvas, (112, 126), (113, 126), white)
        cv.line(self.canvas, (130, 126), (131, 126), white)

        cv.line(self.canvas, (113, 126), (113, 123), white)
        cv.line(self.canvas, (130, 126), (130, 123), white)
        #몸통 색칠 코드
        cv.line(self.canvas, (114, 133), (129, 133), pink)
        cv.line(self.canvas, (112, 132), (131, 132), pink)
        cv.line(self.canvas, (112, 131), (131, 131), pink)
        cv.line(self.canvas, (112, 130), (131, 130), pink)
        cv.line(self.canvas, (112, 129), (131, 129), pink)
        cv.line(self.canvas, (112, 128), (131, 128), pink)
        cv.line(self.canvas, (113, 127), (130, 127), pink)
        cv.line(self.canvas, (114, 126), (129, 126), pink)
        cv.line(self.canvas, (114, 125), (129, 125), pink)
        cv.line(self.canvas, (114, 124), (129, 124), pink)
        cv.line(self.canvas, (114, 123), (129, 123), pink)   
        #꼬리
        cv.line(self.canvas, (121, 131), (122, 131), white)
        cv.line(self.canvas, (121, 130), (122, 130), white)  
        #얼굴
        cv.line(self.canvas, (114, 122), (129, 122), white)

        cv.line(self.canvas, (114, 121), (114, 117), white)

        cv.line(self.canvas, (114, 117), (116, 117), white)

        cv.line(self.canvas, (116, 117), (116, 110), white)

        cv.line(self.canvas, (115, 110), (116, 110), white)

        cv.line(self.canvas, (114, 109), (114, 108), white)

        cv.line(self.canvas, (115, 107), (119, 107), white)

        cv.line(self.canvas, (119, 107), (119, 114), white)

        cv.line(self.canvas, (119, 114), (126, 114), white)

        cv.line(self.canvas, (126, 114), (126, 102), white)

        cv.line(self.canvas, (127, 101), (128, 101), white)

        cv.line(self.canvas, (129, 101), (129, 122), white)

        #몸통 색칠 코드
        cv.rectangle(self.canvas, (115,121), (128, 118), pink, -1)
        cv.rectangle(self.canvas, (117,117), (128, 115), pink, -1)
        cv.rectangle(self.canvas, (127,102), (128, 114), pink, -1)
        cv.rectangle(self.canvas, (117,116), (118, 110), pink, -1)
        cv.rectangle(self.canvas, (115,108), (118, 109), pink, -1)

    cv.line(self.canvas, (124, 117), (124, 116), red)
    cv.line(self.canvas, (126, 117), (126, 116), red)
    cv.line(self.canvas, (123, 116), (124, 116), red)
    cv.line(self.canvas, (126, 116), (127, 116), red)
    cv.line(self.canvas, (123, 114), (124, 114), red)
    cv.line(self.canvas, (126, 114), (127, 114), red)
    cv.line(self.canvas, (124, 113), (124, 114), red)
    cv.line(self.canvas, (126, 114), (126, 113), red)    
