import pygame

class Mouse(pygame.sprite.Sprite):
    """класс одной мышки"""

    def __init__(self, screen):
        """инициализация и задание начальной позиции мышки"""
        super(Mouse, self).__init__()
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('мыф_cut-photo.ru.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод мышки на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещение мышей"""
        self.y += 0.05
        self.rect.y = self.y

    def update_mouses(mouses):
        """обновление позиции мышей"""
        mouses.update()
