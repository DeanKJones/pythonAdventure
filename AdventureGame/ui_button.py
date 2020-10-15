import pygame
from ui_element import UiElement
from sprite import Sprite

class UiButton(UiElement):
    def __init__(self, x, y, w, h, filename):
        UiElement.__init__(self, x, y, w, h)
        #self.color = (0, 0, 255)
        UiElement.set_event(self, "hover_in", self.on_hover_in)
        UiElement.set_event(self, "hover_out", self.on_hover_out)
        UiElement.set_event(self, "click", self.on_click)
        UiElement.set_event(self, "release", self.on_release)
        self.is_hover = False
        self.is_clicked = False
        self.sprite_idle = Sprite(x, y, 'Button_idle.png', False)
        self.sprite_hover = Sprite(x, y, 'Button_hover.png', False)
        self.sprite_click = Sprite(x, y, 'Button_click.png', False)
        self.current_sprite = self.sprite_idle  #defines the current button that will be drawn

    def on_hover_in(self):
        self.current_sprite = self.sprite_hover

    def on_hover_out(self):
        self.current_sprite = self.sprite_idle

    def on_click(self):
        self.current_sprite = self.sprite_click

    def on_release(self):
        if(self.is_hover):
            self.current_sprite = self.sprite_hover
        else:
            self.current_sprite = self.sprite_idle

    #def change_color(self, color):
        #self.color = color

    def inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if(mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h):
                    self.is_clicked = True
                    self.events["click"]()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.is_clicked = False
                    self.events["release"]()

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if(
            not(self.is_hover)
            and(mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h)
        ):
            self.is_hover = True
            self.events["hover_in"]()  #selects the callback and calls it
        if(
            self.is_hover
            and not(mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h)
        ):
            self.is_hover = False
            self.events["hover_out"]()

    def draw(self, screen):
        #pygame.draw.rect(screen, self.current_sprite, pygame.Rect(self.x, self.y, self.w, self.h))  # for standard rectangle
        self.current_sprite.draw(screen)  # draw button by sprites, using the images made
