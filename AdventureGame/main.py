import pygame, sys, math
from sprite import Sprite

def main():

    #load 
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 24)
    quit = False
    path = 'D:\JONES_Dean\Exercises\AdventureGame\\'
    background = pygame.image.load(path+'Background.png').convert()
    hero = Sprite(200, 500, "Hero.png", True)
    cursor = Sprite(0, 0, "Cursor.png", False)
    ground = Sprite(400, 600, "Ground.png", True)
    friend = Sprite(500, 500, "Friend.png", True)

    spr_is_moving = False
    spr_speed = 2
    goal_x = 0
    spr_x, spr_y = 100, 500

    collision_text = font.render("Oops, sorry!", False,(0, 0, 0))

    while not(quit):
        #inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.KEYDOWN:
                    quit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                goal_x = mouse_click[0]
                spr_is_moving = True
                #print(mouse_click[0])


        # update

        cursor_pos = pygame.mouse.get_pos()
        cursor.set_position(cursor_pos)
        if(spr_is_moving):
            goal_x = mouse_click[0]
            
            if(spr_x < goal_x):
                spr_x = spr_x + spr_speed
            if(spr_x > goal_x):
                spr_x = spr_x - spr_speed
            if(math.fabs(goal_x - spr_x) < spr_speed):
                spr_is_moving = False

            spr_pos = spr_x, spr_y

            hero.set_position(spr_pos)
            #print("click")


        # Draw
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        ground.draw(screen)
        hero.draw(screen)
        friend.draw(screen)
        if(hero.intersects(friend)):
            screen.blit(collision_text, (hero.x, hero.y - 100))
            #print(hero.x, hero.y)
        cursor.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()