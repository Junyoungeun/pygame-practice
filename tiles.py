import pygame as py
class Tile(py.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = py.Surface((size, size))#x, y
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos) #사각형 위치 정하기
        