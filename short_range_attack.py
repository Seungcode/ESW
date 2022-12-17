import numpy as np
from PIL import Image

class short_range_attack:
    def __init__(self,background, character):
        background = background.crop((80, 110, 170, 200))
        self.shape = Image.open("short.PNG").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([character.center[0]-50, character.center[1] - 70 , character.center[0] + 50, character.center[1] - 40])
        self.touch = 10
        self.position = character.position

    def collision_check(self, character, enemys):
        for enemy in enemys:
            collision = self.overlap(self.attack, enemy.attack)

            if collision:
                if enemy.state =='live':
                    enemy.life -= self.touch + character.level
                    break

    def overlap(self, ego_position, other_position):
        return (ego_position[2] >= other_position[0] >= ego_position[0] or ego_position[2]>=other_position[2] >= ego_position[0]) and (ego_position[1] <= other_position[1] <= ego_position[3] or ego_position[1] <= other_position[3] <= ego_position[3])