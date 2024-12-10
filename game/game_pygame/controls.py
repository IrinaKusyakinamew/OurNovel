import pygame, sys
from bullet import Bullet
from mouse import Mouse
import time

def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, mouses, bullets):
    """обновление экрана"""
    # При каждом проходе функции перерисовывается экран
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.blitme()
    mouses.draw(screen)
    # Отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets(screen, stats, sc, mouses, bullets):
    """обновление позиций пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, mouses, True, True)
    if collisions:
        for mouses in collisions.values():
            stats.score += 10 * len(mouses)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(mouses) == 0:
        bullets.empty()
        create_army(screen, mouses)

def gun_kill(stats, screen, sc, gun, mouses, bullets):
    """столкновение кота и мышей"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        mouses.empty()
        bullets.empty()
        create_army(screen, mouses)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_mouses(stats, screen, sc, gun, mouses, bullets):
    """обновление позиции мышей"""
    mouses.update()
    if pygame.sprite.spritecollideany(gun, mouses):
        gun_kill(stats, screen, sc, gun, mouses, bullets)
    mouses_check(stats, screen, sc, gun, mouses, bullets)

def mouses_check(stats, screen, sc, gun, mouses, bullets):
    """проверка, добрались ли мыши до края экрана"""
    screen_rect = screen.get_rect()
    for mouse in mouses.sprites():
        if mouse.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, mouses, bullets)
            break

def create_army(screen, mouses):
    """создание армии мышей"""
    mouse = Mouse(screen)
    mouse_width = mouse.rect.width
    number_mouse_x = int((800 - 2 * mouse_width) / mouse_width)
    mouse_height = mouse.rect.height
    number_mouse_y = int((700 - 150 - 2 * mouse_height) / mouse_height)

    for row_number in range(number_mouse_y-2):
        for mouse_number in range(number_mouse_x-1):
            mouse = Mouse(screen)
            mouse.x = mouse_width + (mouse_width * mouse_number)
            mouse.y = mouse_height + (mouse_height * row_number)
            mouse.rect.x = mouse.x
            mouse.rect.y = mouse.rect.height + (mouse.rect.height * row_number)
            mouses.add(mouse)

def check_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))





