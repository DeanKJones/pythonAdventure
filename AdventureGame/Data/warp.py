import pygame
from sprite import Sprite
from sprite_animated import SpriteAnimated

class Warp(Sprite):
    def __init__(self, x, y, filename, centered, to_scene):
        Sprite.__init__(self, x, y, filename, centered)
        self.to_scene = to_scene
        self.to_scene_x = to_scene