import pygame, sys
from sprite_controlled import SpriteControlled
from sprite import Sprite
from warp import Warp
from ui_panel import UiPanel
from ui_group import UiGroup
#from ui_element import UiElement
from ui_button import UiButton
from sprite_animated import SpriteAnimated

class Scene:
    
    path = 'D:\\JONES_Dean\\pythonAdventure\\AdventureGame\\Images\\'
    path = 'D:\\JONES_Dean\\pythonAdventure\\AdventureGame\\Data\\'

    def __init__(self, filename):
        self.filename = filename
        self.load(filename)

    def load(self, filename):
        file = open(Scene.path + filename)
        data = file.read().splitlines()

        #self.panel = UiPanel(0, 0, 800, 100)
        #self.button = UiButton(10, 10, 80, 80)

        ground_height = 0
        self.cursor = Sprite(0, 0, 'cursor.png', False)
        self.sprites = []
        self.warps = []

        self.ui_top = UiGroup()
        panel = UiPanel(0, 0, 800, 100)
        button = UiButton(10, 10, 80, 80, filename)
        self.ui_top.add_element(panel)
        self.ui_top.add_element(button)

        collision_text = font.render("Oops, my bad!", False, (0, 0, 0))

        for line in data:
            cell = line.split(";")
            
            # Ground

            if(cell[0] == "ground"):
                self.ground = Sprite(0, 0, cell[1]+".png", False)
                _, screen_h = pygame.display.get_surface().get_size()
                ground_height = screen_h - self.ground.surface.get_height()
                self.ground.y = ground_height

            # Background

            elif(cell[0] == "background"):
                self.background = Sprite(0, 0, cell[1]+".png", False)

            # Hero

            elif(cell[0] == "hero"):
                height = 0
                if cell[3] == "ground":
                    height = -1
                self.hero = SpriteControlled(int(cell[2]), height, cell[1]+".png", True, int(cell[4]))
            
            # Sprites

            elif(cell[0] == "sprite"):
                height = 0
                if cell[3] == "ground":
                    height = -1
                sprite = Sprite(int(cell[2]), height, cell[1]+".png", True)
                self.sprites.append(sprite)
           
            # Warps

            elif(cell[0] == "warp"):
                height = 0
                if cell[3] == "ground":
                    height = -1
                warp = Warp(int(cell[2]), height, cell[1]+".png", False, cell[4])
                self.warps.append(warp)

        # Set heights

        if(self.hero.y == -1):
            self.hero.y = ground_height
        for s in self.sprites:
            if(s.y == -1):
                s.y = ground_height
        for w in self.warps:
            if(w.y == -1):
                w.y = ground_height - w.surface.get_height() / 2

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                if(mouse_click[1] > self.ui_top.elements[0].h): #trick to not move player on button click
                    self.hero.move_to(mouse_click[0])
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_F5]:
                    self.load(self.filename)
        self.ui_top.inputs(events)
                

    def update(self, change_scene):
        self.cursor.set_position(pygame.mouse.get_pos())
        self.hero.update()
        for w in self.warps:
            if(self.hero.intersects(w)):
                change_scene(w.to_scene)

        #self.panel.update()
        self.ui_top.update()

    def draw(self, screen):
        self.background.draw(screen)
        self.ground.draw(screen)
        for w in self.warps:
            w.draw(screen)
        for s in self.sprites:
            s.draw(screen)

            if(self.hero.intersects(s)):
                screen.blit(collision_text, (self.hero.x, self.hero.y - 100))
                #print("Collision")

        self.hero.draw(screen)
        
        #self.panel.draw(screen)
        self.ui_top.draw(screen)
        self.cursor.draw(screen)
    
