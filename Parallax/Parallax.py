import pygame, random, math, os

white = [255, 255, 255]
black = [0, 0, 0]

running = True
width = 1080
height = 360

screen = pygame.display.set_mode((width,height))


picture = {}
st = 0
Pictures = []
entries = os.listdir('Images')
for entry in entries:
    picture[st] = pygame.image.load("images/block_textures/"+entry).convert_alpha()
    Pictures.append(picture[st])


def Background_Parallax(object):
    def __init__(self, Images):
