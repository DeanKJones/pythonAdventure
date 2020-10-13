import pygame
from sprite import Sprite
from sprite_controlled import SpriteControlled
from scene import Scene

class Level00(Sprite):

    def __init__(self, background_file, ground_file):
        Scene.__init__(self, 'Background.png', 'Ground.png')
        screen_h = pygame.display.get_surface().get_size()
        ground_height = screen_h - self.ground.surface.get_height()
        self.ground.y = ground_height
        self.hero = SpriteControlled(10, ground_height, 'Hero.png', True, 2)
        self.cursor = Sprite(0, 0, 'Cursor.png', False)
        self.warp = Warp(500, 0, 'Warp.png', False, "level01")
        self.warp.y = ground_height - self.warp.surface.get_height()/2

        self.warp = Warp(680, 0, 'Warp.png', False, "level01", 0)

    def update(self, change_scene):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.hero.update()

        if(self.hero.intersects(self.warp)):
            change_scene(self.warp.to_scene)

        if(self.hero.intersects(self.warp)):
            change_scene(self.warp.to_scene)

        if self.hero.intersects(self.warp):
            change_scene(self.warp.to_scene, self.warp.to_scene_x)

