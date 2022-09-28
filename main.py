from math import sin, cos, sqrt, pi
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
    return (x, y)
    
def main():
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FPS = 60
    pygame.init()
    
    SIZE = (600, 600)
    #PATH_TO_LOGO = "files\Pulse_Rickyyy.png"
    CAPTION = "Double Pendulum"
    
    pos1 = []
    pos2 = []
    m1 = 800                #massa 1
    m2 = 800                #massa 2
    ang1 = pi/2             #angulo1
    ang2 = pi/4             #angulo2
    r1 = 120                #comprimento 1
    r2 = 120                #comprimento 2
    g = 0.5                 #aceleracao gravitica
    aceleracao1 = 0         #aceleracao inicial da bola 1
    aceleracao2 = 0         #aceleracao inicial da bola 2
    velocidade1 = 0         #velocidade inicial da bola 1
    velocidade2 = 0         #velocidade inicial da bola 2
    resistance = True       #True: há dissipação de energia
    resistanceperc = 1     #percentagem de dissipação
    
    #LOGO = pygame.image.load(PATH_TO_LOGO)
    #pygame.display.set_icon(LOGO)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    
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
        
        num11 = -1 * g * (2 * m1 + m2) * sin(ang1)
        num12 = -1 * m2 * g * sin(ang1 - 2 * ang2)
        num13 = -2 * sin(ang1 - ang2) * m2
        num14 = (velocidade2 * velocidade2 * r2 + velocidade1 * velocidade1 * r1 * cos(ang1 - ang2))
        den11 = r1 * (2 * m1 + m2 - m2 * cos(2 * ang1 - 2 * ang2))
        
        aceleracao1 = (num11 + num12 + num13 * num14) / den11
        velocidade1 += aceleracao1
        if resistance == True:
            velocidade1 *= (100-resistanceperc) * 0.01
        ang1 += velocidade1
        
        num21 = 2 * sin(ang1 - ang2) 
        num22 = velocidade1 * velocidade1 * r1 * (m1 + m2)
        num23 = g * (m1 + m2) * cos(ang1)
        num24 = velocidade2 * velocidade2 * r2 * m2 * cos(ang1 - ang2)
        den21 = r2 * (2 * m1 + m2 - m2 * cos(2 * ang1 - 2 * ang2))
        
        aceleracao2 = (num21 * (num22 + num23 + num24)) / den21
        velocidade2 += aceleracao2
        if resistance == True:
            velocidade2 *= (100-resistanceperc) * 0.01
        ang2 += velocidade2
        
        bola1 = (coords(ang1, r1, (0, 0)))
        bola2 = (coords(ang2, r2, bola1))
        
        pos1.append(bola1)
        pos2.append(bola2)
        # for coord in pos1:
        #     pygame.draw.circle(screen, BLACK, translate(coord), 2)
        for coord in pos2:
            pygame.draw.circle(screen, BLACK, translate(coord), 2)
        pygame.draw.line(screen, BLACK, translate((0,0)), translate(bola1), 2)
        pygame.draw.circle(screen, BLACK, translate(bola1), sqrt(m1/pi))
        pygame.draw.line(screen, BLACK, translate(bola1), translate(bola2), 2)
        pygame.draw.circle(screen, BLACK, translate(bola2), sqrt(m2/pi))
        
        clock.tick(FPS)
        pygame.display.flip()




if __name__== "__main__":
    main()