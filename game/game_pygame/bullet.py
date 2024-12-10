import pygame

#создание дочернего класса
from pygame.sprite import Sprite
class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создание пули в текущей позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 13)
        self.color = 60, 60, 60
        self.speed = 4.5 #скорость изменения позиции пули по оси у
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y) #изменение координаты пули по оси у

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self  ):
        """изображение пули на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
