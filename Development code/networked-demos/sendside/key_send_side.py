#sweep test!
import network
import time
import pygame
ip = "169.254.126.87"
pygame.init()
window = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()

network.call(ip)
jointdata = [90,90,90,90,90,110]
 #           0   1  2  3  4  5
def sayNet():
    for i in range(0,6):
        network.say("{0},{1}".format(i,jointdata[i]))
        print("{0},{1}".format(i,jointdata[i]))

network.say("8,1")

while network.isConnected():


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                jointdata[0] += 1
            if event.key == pygame.K_a:
                jointdata[0] -= 1
            if event.key == pygame.K_w:
                jointdata[1] += 1
            if event.key == pygame.K_s:
                jointdata[1] -= 1
            if event.key == pygame.K_e:
                jointdata[2] += 1
            if event.key == pygame.K_d:
                jointdata[2] -= 1
            if event.key == pygame.K_r:
                jointdata[3] += 1
            if  event.key == pygame.K_f:
                jointdata[3] -= 1
            if  event.key == pygame.K_t:
                jointdata[4] += 1
            if  event.key == pygame.K_g:
                jointdata[4] -= 1
            if  event.key == pygame.K_y:
                jointdata[5] += 1
            if  event.key == pygame.K_h:
                jointdata[5] -= 1


            print(jointdata)
            sayNet()