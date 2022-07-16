import pygame as py, sys
from settings import *
from tiles import Tile
#pygame setup
py.init()
screen_width = 1200
screen_height = 700
screen = py.display.set_mode((screen_width, screen_height))
clock = py.time.Clock()
test_tile = py.sprite.Group(Tile((100, 100), 200)) #(pos, size)
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    screen.fill('black')
    test_tile.draw(screen) 
    py.display.update()
    clock.tick(60)
#3:12