import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
import pygame.time


# Класс для кнопки
class Button:
    def __init__(self, screen, msg, width=200, height=50, pos=(0, 0)):
        self.screen = screen
        self.msg = msg
        self.width = width
        self.height = height
        self.x, self.y = pos
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_image = self.font.render(self.msg, True, self.text_color)
        text_rect = text_image.get_rect()
        text_rect.center = self.rect.center
        self.screen.blit(text_image, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# Функция для отображения главного меню
def show_main_menu(screen):
    screen.fill((0, 0, 0))  # Черный фон для меню
    button_start = Button(screen, "Начать игру", pos=(300, 250))
    button_quit = Button(screen, "Выход", pos=(300, 350))

    button_start.draw()
    button_quit.draw()
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_start.is_clicked(mouse_pos):
                    return "start"
                elif button_quit.is_clicked(mouse_pos):
                    return "quit"


# Основная функция для запуска игры
def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Коты-защитники")

    stats = Stats()
    sc = Scores(screen, stats)
    bg_color = (220, 220, 220)

    # Показываем главное меню и ждем действия пользователя
    menu_result = show_main_menu(screen)

    if menu_result == "quit":
        pygame.quit()
        exit()

    # После того как игрок выбрал "Начать игру"
    gun = Gun(screen)
    bullets = Group()
    mouses = Group()
    controls.create_army(screen, mouses)

    # Основной игровой цикл
    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, mouses, bullets)
            controls.update_bullets(screen, stats, sc, mouses, bullets)
            controls.update_mouses(stats, screen, sc, gun, mouses, bullets)


# Запуск игры
run()
