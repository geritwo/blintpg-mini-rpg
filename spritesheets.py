import pygame


class SpriteSheet:
    def __init__(self, filename, w, h, color_key, scale=1):
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.color_key = color_key
        self.scale = scale

        # Dimensions of one tile
        self.w = w
        self.h = h

    def get_image(self, x_pos, y_pos):
        # Get single image from spritesheet
        image = pygame.Surface((self.w, self.h)).convert_alpha()  # Blank surface for image
        # Blit image from sheet to surface (source, (destination top left x,y), area Rect from source)
        image.blit(self.sprite_sheet, (0, 0), (x_pos, y_pos, self.w, self.h))
        if self.scale != 1:
            image = pygame.transform.scale(image, (self.w * self.scale, self.h * self.scale))
        # Color key from transparency
        image.set_colorkey(self.color_key)

        return image

    def get_phases(self, row, column, steps, vertical=False) -> []:
        phases = []
        x_pos, y_pos = column * self.w, row * self.h
        for step in range(0, steps+1):
            phases.append(self.get_image(x_pos, y_pos))
            if vertical:
                y_pos += self.h
            else:
                x_pos += self.w
        return phases







