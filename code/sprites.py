import pygame
from pygame.math import Vector2 as vector

from settings import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, group) -> None:
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

class Animated(Generic):
    def __init__(self, assets, pos, group) -> None:
        
        self.aniamtion_frames = assets
        self.frame_index = 0
        super().__init__(pos, self.aniamtion_frames[self.frame_index], group)

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        if int(self.frame_index) >= len(self.aniamtion_frames):
           self.frame_index = 0
        self.image = self.aniamtion_frames[int(self.frame_index)]


    def update(self, dt):
        self.animate(dt)


class Particle(Animated):
    def __init__(self, assets, pos, group) -> None:
        super().__init__(assets, pos, group)
        self.rect = self.image.get_rect(center = pos)

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        if int(self.frame_index) >= len(self.aniamtion_frames):
           self.kill()
        else:
            self.image = self.aniamtion_frames[int(self.frame_index)]


class Coin(Animated):
    def __init__(self, coin_type, assets, pos, group) -> None:
        super().__init__(assets, pos, group)
        self.rect = self.image.get_rect(center = pos)
        self.coin_tupe = coin_type

class Player(Generic):
    def __init__(self, pos, group) -> None:
        super().__init__(pos, pygame.Surface((32,64)), group)
        self.image.fill('red')

        # movement
        self.direction = vector()
        self.pos = vector(self.rect.topleft)
        self.speed = 300

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

    def update(self, dt):
        self.input()
        self.move(dt)

