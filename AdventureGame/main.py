import pygame, sys, math, time
from sprite import Sprite
from sprite_controlled import SpriteControlled
from scene import Scene
from warp import Warp
from level00 import Warp

def main():

    #load 

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.mouse.set_visible(False)

    level00 = Level00("Background.png", "Ground.png")
    level01 = Level01("Background.png", "Ground_01.png")

    scenes = {}
    scenes["level00"] = level00
    scenes["level01"] = level01

    current_scene = level00

    def change_scene(name):
        nonlocal current_scene
        current_scene = scenes[name]
        current_scene.hero.x = x
        current_scene.player.is_moving = False

    quit = False

    while not(quit):

        #inputs

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
        current_scene.inputs(events)

        # update

        current_scene.update(change_scene)

        # Draw

        screen.fill((0, 0, 0))
        current_scene.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()