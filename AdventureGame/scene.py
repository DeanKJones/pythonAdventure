import pygame, math
from sprite import Sprite
from sprite_controlled import SpriteControlled

class Scene:

    def __init__(self, name, background_file, ground_file):
        self.name = name
        self.background = Sprite(0, 0, background_file, False)
        self.ground = Sprite(0, 0, ground_file, False)
        screen_w, screen_h = pygame.display.get_surface().get_size()
        ground_height = screen_h - self.ground.surface.get_height()
        self.ground.y = ground_height

        self.hero = SpriteControlled(10, ground_height, 'Hero.png', True, 2)
        self.friend = Sprite(200, ground_height, 'Friend.png', True)
        self.cursor = Sprite(0, 0, 'Cursor.png', False)

        self.font = pygame.font.Font(None, 24)
        self.collision_text = self.font.render("Oops, sorry!", False,(0, 0, 0))

        self.warp = Warp(500, 0, 'warp.png', False, "level01")
        self.warp.y = ground_height - self.warp.surface.get_height()/2
    
    def load(self):
        pass

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                self.hero.move_to(mouse_click[0])

    def update(self, change_scene):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.hero.update()
        if(self.hero.intersects(self.warp)):
            change_scene(self.warp.to_scene)
        if(self.hero.intersects(self.warp)):
            change_scene(self.warp.to_scene)

    def draw(self, screen):
        self.background.draw(screen)
        self.ground.draw(screen)
        self.hero.draw(screen)
        self.friend.draw(screen)
        if(self.hero.intersects(self.friend)):
            screen.blit(self.collision_text, (self.hero.x, self.hero.y - 100))
            #print(hero.x, hero.y)
        self.cursor.draw(screen)
