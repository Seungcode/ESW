from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageOps, ImageFilter
import time
import cv2 as cv
import random
import numpy as np
from colorsys import hsv_to_rgb
from Character_1_1 import Character_1_1
from Character_1_2 import Character_1_2
from Character_1 import Character_1
from Character_2 import Character_2
from Character_2_1 import Character_2_1
from Character_2_2 import Character_2_2
from Joystick import Joystick
from Enemy_1 import Enemy_1
from Enemy_2 import Enemy_2
from Enemy_3 import Enemy_3
from Enemy_boss import Enemy_boss
from BackGround import BackGround
from short_range_attack import short_range_attack
from long_range_attack import long_range_attack
from carrot import carrot

def main():
    white = (255, 255, 255)
    joystick = Joystick()
    my_image = BackGround()
    makenew = BackGround()
    gameclearflag = 0
    start_ = Image.open('start.png')
    enemy_1_1 = Enemy_1((240, 360), my_image.shape)
    my_image.shape.paste(enemy_1_1.shape, (enemy_1_1.position[0], enemy_1_1.position[1]))
    enemy_1_2 = Enemy_1((200, 330), my_image.shape)
    my_image.shape.paste(enemy_1_2.shape, (enemy_1_2.position[0], enemy_1_2.position[1]))
    enemy_1_3 = Enemy_1((160, 360), my_image.shape)
    my_image.shape.paste(enemy_1_3.shape, (enemy_1_3.position[0], enemy_1_3.position[1]))
    enemy_1_4 = Enemy_1((120, 330), my_image.shape)
    my_image.shape.paste(enemy_1_4.shape, (enemy_1_4.position[0], enemy_1_4.position[1]))
    enemy_1_5 = Enemy_1((280, 330), my_image.shape)
    my_image.shape.paste(enemy_1_5.shape, (enemy_1_5.position[0], enemy_1_5.position[1]))
    enemy_1_6 = Enemy_1((320, 360), my_image.shape)
    my_image.shape.paste(enemy_1_6.shape, (enemy_1_6.position[0], enemy_1_6.position[1]))
    enemy_1_7 = Enemy_1((360, 330), my_image.shape)
    my_image.shape.paste(enemy_1_7.shape, (enemy_1_7.position[0], enemy_1_7.position[1]))
    enemy_2_1 = Enemy_2((100, 270), my_image.shape)
    my_image.shape.paste(enemy_2_1.shape, (enemy_2_1.position[0], enemy_2_1.position[1]))
    enemy_2_2 = Enemy_2((180, 270), my_image.shape)
    my_image.shape.paste(enemy_2_2.shape, (enemy_2_2.position[0], enemy_2_2.position[1]))
    enemy_2_3 = Enemy_2((260, 270), my_image.shape)
    my_image.shape.paste(enemy_2_3.shape, (enemy_2_3.position[0], enemy_2_3.position[1]))
    enemy_2_4 = Enemy_2((340, 270), my_image.shape)
    my_image.shape.paste(enemy_2_4.shape, (enemy_2_4.position[0], enemy_2_4.position[1]))
    enemy_3_1 = Enemy_3((120, 170), my_image.shape)
    my_image.shape.paste(enemy_3_1.shape, (enemy_3_1.position[0], enemy_3_1.position[1]))
    enemy_3_2 = Enemy_3((210, 170), my_image.shape)
    my_image.shape.paste(enemy_3_2.shape, (enemy_3_2.position[0], enemy_3_2.position[1]))
    enemy_3_3 = Enemy_3((300, 170), my_image.shape)
    my_image.shape.paste(enemy_3_3.shape, (enemy_3_3.position[0], enemy_3_3.position[1]))
    enemy_boss = Enemy_boss((210, 70), my_image.shape)
    my_image.shape.paste(enemy_boss.shape, (enemy_boss.position[0], enemy_boss.position[1]))
    character_ = Character_1((my_image.position[0]+90, my_image.position[1]+130), my_image)
    my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
    my_image_.paste(character_.shape, (90, 130))
    joystick.disp.image(start_)
    start = time.time()

    enemy=[enemy_1_1, enemy_1_2, enemy_1_3, enemy_1_4, enemy_1_5, enemy_1_6, enemy_1_7, enemy_2_1, enemy_2_2, enemy_2_3, enemy_2_4,enemy_3_1, enemy_3_2, enemy_3_3, enemy_boss]

    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
    
        if not joystick.button_U.value:
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value: 
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value: 
            command['right_pressed'] = True
            command['move'] = True

        if not joystick.button_A.value:
            bullet = short_range_attack(my_image_, character)
            my_image_.paste(bullet.shape, (80, 110))
            joystick.disp.image(my_image_)
            bullet.collision_check(character_, enemy)
            time.sleep(1.5)
            my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
            my_image_.paste(character.shape, (90, 130))
            joystick.disp.image(my_image_)

        if not joystick.button_B.value:
            bullet = long_range_attack(my_image_, character)
            my_image_.paste(bullet.shape, (85, 75))
            joystick.disp.image(my_image_)
            bullet.collision_check_long(character_, enemy)
            time.sleep(2.2)
            my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
            my_image_.paste(character.shape, (90, 130))
            joystick.disp.image(my_image_)
        
        for enemys in enemy:
            if enemys.life<=0:
                character_.level += 1
                enemys.death(makenew.shape)
                my_image.shape.paste(enemys.shape, (enemys.position[0], enemys.position[1]))
                if enemys == enemy_boss:
                    gameclearflag = 1
                    fianlcarrot = carrot(enemy_boss.position, my_image)
                    my_image.shape.paste(fianlcarrot.shape, (fianlcarrot.position[0], fianlcarrot.position[1]))
                enemy.remove(enemys)
                my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
                if character_.level < 10:
                    character = Character_1((my_image.position[0]+90, my_image.position[1]+130), my_image)
                    my_image_.paste(character.shape, (90, 130))
                else:
                    character = Character_2((my_image.position[0]+90, my_image.position[1]+130), my_image)
                    my_image_.paste(character.shape, (90, 130))
                joystick.disp.image(my_image_)

            

        my_image.move(command)
        if character_.level < 10 and command['move']==True:
            my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
            character = Character_1_1((my_image.position[0]+90, my_image.position[1]+130), my_image)
            my_image_.paste(character.shape, (90, 130))
            joystick.disp.image(my_image_)
            my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
            character = Character_1_2((my_image.position[0]+90, my_image.position[1]+130), my_image)
            my_image_.paste(character.shape, (90, 130))
            joystick.disp.image(my_image_)
            my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
            character = Character_1((my_image.position[0]+90, my_image.position[1]+130), my_image)
            my_image_.paste(character.shape, (90, 130))
            end = time.time()
            if end-start>=5:
                character_.collision_check(character, enemy, character_)
                start = time.time()
            if character_.life <= 0:
                my_image_ = Image.open('gameover.png')
                joystick.disp.image(my_image_)
                exit(0)
        if character_.level >= 10 and command['move']==True:
            my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
            character = Character_2_1((my_image.position[0]+90, my_image.position[1]+130), my_image)
            my_image_.paste(character.shape, (90, 130))
            joystick.disp.image(my_image_)
            my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
            character = Character_2_2((my_image.position[0]+90, my_image.position[1]+130), my_image)
            my_image_.paste(character.shape, (90, 130))
            joystick.disp.image(my_image_)
            my_image_ = my_image.shape.crop((my_image.position[0],my_image.position[1], my_image.position[0]+240, my_image.position[1]+240))
            character = Character_2((my_image.position[0]+90, my_image.position[1]+130), my_image)
            my_image_.paste(character.shape, (90, 130))
            end = time.time()
            if end-start>=5:
                before = character_.life
                character_.collision_check(character, enemy, character_)
                after = character_.life
                if before != after:
                    start = time.time()
            if character_.life <= 0:
                my_image_ = Image.open('gameover.png')
                joystick.disp.image(my_image_)
                exit(0)
        if gameclearflag == 1:
            finish_ = fianlcarrot.collision_check(character)
            if finish_:
                my_image_ = Image.open('finish.png')
                joystick.disp.image(my_image_)
                exit(0)
    joystick.disp.image(my_image_)
        
        

if __name__ == '__main__':
    main()