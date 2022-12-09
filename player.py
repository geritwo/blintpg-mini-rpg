import pygame
from settings import *
from spritesheets import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.sprite_sheet = SpriteSheet("assets/SproutLandsAssets/Characters/BasicCharacterSpritesheet.png",
                                        48, 48, 'black', 2)
        self.animations = {}
        self.import_assets()

        # General setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

        # Movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.animations = {
            'down': [], 'up': [], 'left': [], 'right': []
        }

        pos_v, pos_h = 0, 0
        for animation in self.animations.keys():
            phases = self.sprite_sheet.get_phases(pos_v, pos_h, 4)
            self.animations[animation] = phases
            pos_v += 1

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # Horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # Vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)



