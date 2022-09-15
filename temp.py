from math import sin, cos, sqrt, pi, asin
import pygame
from colour import Color

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def translate(coords):
    return (coords[0] + 300, coords[1] + 150)

def coords(ang, r, origin):
    x = origin[0] + r * sin(ang)
    y = origin[1] + r * cos(ang)
    return [x, y]
    
def main():
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    pygame.init()
    
    SIZE = (600, 600)
    PATH_TO_LOGO = "files\Pulse_Rickyyy.png"
    CAPTION = "Double Pendulum"
    
    m1 = 400    #massa 1
    ang1 = pi/4   #angulo1
    r1 = 80     #comprimento 1
    FPS = 10
    ag = 10     #aceleracao gravitica
    vx = 0
    vy = 0
    
    LOGO = pygame.image.load(PATH_TO_LOGO)
    pygame.display.set_icon(LOGO)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    bola1 = (coords(ang1, r1, (0, 0)))
    #Em = m1 * ag * bola1[1]
    
    running = True
    pause = False
    
    while running:
        
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_SPACE:
                    if pause == False:
                        pause = True
                    else:
                        pause = False
            if event.type == pygame.QUIT:
                running = False
        
        while pause == True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause = False
                        running = False
                    if event.key == K_SPACE:
                        if pause == False:
                            pause = True
                        else:
                            pause = False
                if event.type == pygame.QUIT:
                    running = False
        
        #altura = r1 - bola1[1]
        #Ep = m1 * ag * altura
        
        #Ec = Em - Ep
        #v = sqrt(2 * Ec)
        #vx = v * cos(ang1)
        #vy = v * sin(ang1)
        
        at = ag * sin(ang1)
        an = ag * cos(ang1)
        
        ax = at * cos(ang1)
        ay = at * sin(ang1)
        if bola1[0] >= 0:
            vx -= ax
            vy += ay
        else:
            vx += ax
            vy -= ay
        
        bola1[0] += vx
        bola1[1] += vy
        
        ang1 = asin((bola1[0])/r1)
        
        pygame.draw.line(screen, BLACK, translate((0,0)), translate(bola1), 2)
        pygame.draw.circle(screen, BLACK, translate(bola1), sqrt(m1/pi))
        clock.tick(FPS)
        pygame.display.flip()

if __name__== "__main__":
    main()