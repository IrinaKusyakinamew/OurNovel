import pygame
from pygame.sprite import Sprite
""""Класс для хранения всех настроек игры"""
class Gun(Sprite):
    def __init__(self, screen):
        """Инициализация корабля"""
        super(Gun, self).__init__()
        self.screen = screen
        #параметры экрана
        self.image = pygame.transform.scale(pygame.image.load('коо_cut-photo.ru.png'), (55, 55))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)  #вывод корабля

    def update_gun(self):
        """обновления позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        """размещение кота по центру внизу"""
        self.center = self.screen_rect.centerx

