#определяем персонажей игры
define gh = Character('Призрак', color="#6d457e", image='ghost') #призрак
define gg = Character("[playerName]", color="#3b2f73") #гг
define fr = Character("[friendName]", color="#5f2626") #друг гг
define par = Character("[partnerName]", color="#5f2626") #любовный интерес гг
define barman = Character('Бармен', color="#221e3a", image='barman') #бармен

define tchr = Character('Наталья Васильевна', color="#221e3a", image='minor/teacher')
define mom = Character('Мама', color="#67682b", image='parents/mom')
define gang = Character('Компания', color="#5f2626", image='minor/gang')
define f_pol = Character('Грузный миллиционер', color="#221e3a", image='minor/fat_policeman')
define t_pol = Character('Высокий миллиционер', color="#221e3a", image='minor/tall_policeman')

define f1 = Character("Студентка", color="#6d457e", image='minor/fantoms')
define f2 = Character("Студент", color="#6d457e", image='minor/fantoms')
define f_np = Character("Николай Петрович", color="#6d457e", image='minor/fantoms')
define f_dean = Character("Декан", color="#6d457e", image='minor/fantoms')
define dad = Character('Отец', color="#67682b", image='parents/dad')
define aik = Character('Айзек', color="#6d457e", image='korteze/aizek')

define na = Character('Наоми', color="#6d457e", image='korteze/naomi')
define nd = Character('Отец Наоми', color="#6d457e", image='korteze/n_dad')

define nu = Character('Медсестра', color="#221e3a", image='minor/nurse')

#определяем телефонных персонажей
define gg_nvl = Character("я", kind=nvl, callback=Phone_SendSound)
define fr_nvl = Character("Заноза", kind=nvl, callback=Phone_ReceiveSound)
define hr_nvl = Character("HR", kind=nvl, callback=Phone_ReceiveSound)
define par1_nvl = Character("Хлебушек", kind=nvl, callback=Phone_ReceiveSound)
define par2_nvl = Character("Хлебушек <3", kind=nvl, callback=Phone_ReceiveSound)

label splashscreen:
    scene black 
    pause(0.5)
    scene disclaimer with fade
    pause(2)
    scene sound_rec with fade
    pause(2)
    scene black with fade

#переменные для плавного исчезновения телефона
define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#переменные для разового отображения уведомления о получении достижения
define persistent.late_notify = 0
define persistent.listen_notify = 0

define persistent.bookworm_notify = 0
define persistent.painting_notify = 0

define persistent.history_notify = 0
define persistent.conversation_notify = 0

define persistent.running_notify = 0

define persistent.jos_notify = 0

#переменные, отвечающие за отображение заметок в конкекстном меню
define note_meet_fr1 = False
define note_meet_fr2 = False
define note_meet_gh1 = False
define note_meet_gh2 = False

define note_cooperate = False
define note_pictures1 = False
define note_pictures2 = False
define note_painter1 = False
define note_painter2 = False

define note_fantoms1 = False
define note_fantoms2 = False
define note_gang1 = False
define note_gang2 = False
define note_gang3 = False
define note_Naomi = False

define note_Naomi_flashback = False


define important1 = False
define important2 = False
define jos = False

define is_flashback = False

#создание анимации в главном меню
image menu_slideshow:
    "gui/bg menu1.jpg"
    pause 1.2
    "gui/bg menu2.jpg"
    pause 1.2
    "gui/bg menu3.jpg"
    pause 1.2
    "gui/bg menu4.jpg"
    pause 1.2
    "gui/bg menu5.jpg"
    pause 1.2
    "gui/bg menu6.jpg"
    pause 1.2
    repeat

#добавление кнопок в экран галереи
init python:
    g = Gallery()

    g.locked_button = "images/Splash_arts/locked_poster.jpg"
   
    g.button("meeting")
    g.condition("persistent.meeting")
    g.image("meet_ghost")

    g.button("ending1b")
    g.condition("persistent.ending1b")
    g.image("lonely_end_b")

    g.button("ending1g")
    g.condition("persistent.ending1g")
    g.image("lonely_end_g")

    g.button("flashback1b")
    g.condition("persistent.flashback1b")
    g.image("flashback1b")

    g.button("flashback1g")
    g.condition("persistent.flashback1g")
    g.image("flashback1g")

    g.button("flashback2b")
    g.condition("persistent.flashback2b")
    g.image("flashback2b")

    g.button("flashback2g")
    g.condition("persistent.flashback2g")
    g.image("flashback2g")

    g.button("naomi_draws")
    g.condition("persistent.Naomi_flashback")
    g.image("naomi_draws")
    
    g.button("naomi_disappear")
    g.condition("persistent.Naomi_disappear")
    g.image("naomi_disappear")

    g.button("ending2b")
    g.condition("persistent.ending2b")
    g.image("ending2b")

    g.button("ending2g")
    g.condition("persistent.ending2g")
    g.image("ending2g")

    g.button("ending2jos")
    g.condition("persistent.ending2jos")
    g.image("ending2jos")

    g.button("ending3b")
    g.condition("persistent.ending3b")
    g.image("ending3b")

    g.button("ending3g")
    g.condition("persistent.ending3g")
    g.image("ending3g")

    g.button("ending4b")
    g.condition("persistent.ending4b")
    g.image("ending4b")

    g.button("ending4g")
    g.condition("persistent.ending4g")
    g.image("ending4g")

    g.button("ending5b")
    g.condition("persistent.ending5b")
    g.image("ending5b")

    g.button("ending5g")
    g.condition("persistent.ending5g")
    g.image("ending5g")

    g.button("ending6b")
    g.condition("persistent.ending6b")
    g.image("ending6b")

    g.button("ending6g")
    g.condition("persistent.ending6g")
    g.image("ending6g")

    g.button("ending7b")
    g.condition("persistent.ending7b")
    g.image("ending7b")

    g.button("ending7g")
    g.condition("persistent.ending7g")
    g.image("ending7g")

#добавление кнопок в экрана достижений
init python:
    ach = Gallery()

    ach.locked_button = "images/achievements/locked_achievement.png"

    ach.button("late_fr")
    ach.condition("persistent.late")
    ach.image("late_img")

    ach.button("listen_smn")
    ach.condition("persistent.listen")
    ach.image("listen_img")

    ach.button("tolstoi")
    ach.condition("persistent.bookworm")
    ach.image("bookworm_img")

    ach.button("painting")
    ach.condition("persistent.painting")
    ach.image("painting_img")

    ach.button("history")
    ach.condition("persistent.history")
    ach.image("history_img")

    ach.button("prisoner")
    ach.condition("persistent.running")
    ach.image("running_img")

    ach.button("jos")
    ach.condition("persistent.ending2jos")
    ach.image("black_cat_img")


# Теперь создаём экран для текста, который будет использоваться
screen text_window(message):
    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        # Здесь вы можете настроить внеш вид своего текстового окна
        text message

#переменные, отвечающие за расположение персонажей сбоку
init:
    $ left2 = Position(xalign = 0.2)
    $ right2 = Position(xalign = 0.7)

#переменные, необходимые для грамотного отображения текста в интерактивном режиме
define barman_click = 0
define girl_click = 0
define tree_click = 0
define flashback1_click = 0
define dean_door_click = 0

define friendshp_gh_temp = 0

#переменная, хранящая текущую локацию
default current_state = "default"

# Переменные, показывающие, много ли времени провел игрок в комнате общежития
define time = 0
define bool_time = False

# Переменная для отслеживания состояния подсказки
define info_panel_closed = False
define info_panel_closed_1 = False
define info_panel_closedd_1 = False

define info_panel_closed_2 = False
define info_panel_closed_3 = False

#переменные взаимоотношений 
define friendship_fr = 0
define friendshp_gh = 0

# Начальная (опорная) локация в баре - центральный зал бара (для свободной навигации)
default current_loc = "bar_front"

# Переменные отображения микшеров по умолчанию
# Используйте обычные переменные или словарь для хранения настроек
default has_sound = True
default has_music = True
default has_voice = False

# Музыка и звуки
define audio.bar1 = "music/music_bar_1.mp3"
define audio.bar2 = "music/music_bar_2.mp3"
define audio.createpers = "sounds/create_character.mp3"
define audio.vibro = "sounds/phone-vibration-96623.mp3"
define audio.stepshall = "sounds/steps_dormitory_hall.mp3"
define audio.stepsstreer = "sounds/steps_street.mp3"
define audio.drink = "sounds/drink_sound.mp3"
define audio.start_music_0 = "music/Triangle.mp3"
define audio.start_music_1 = "music/AcrylicOnCanvas.mp3"
define audio.start_music_2 = "music/Friends.ogg"
define audio.choise_1 = "music/AMomentsReflection.mp3"
define audio.bar_interact = "music/Assasins.mp3"
define audio.gallery1 = "music/Kiss And Goodbye.ogg"
define audio.singing = "sounds/singing.mp3"

# Логическая переменная, показывающая звучала ли музыка
define werePlayed = False

#инициализация начальных имен и спрайтов
$ playerName = "Игрок"
$ friendName = "Игрок"
$ friendSprite = ""
$ partnerName = "Игрок"
$ partnerSprite = ""
$ gender = "None"

#Инициализация звука
init:
    $ hover_sound = "sounds/create_character.mp3"  # Путь к вашему звуковому файлу


# Переменная для отслеживания состояния всплывающей подсказки в баре (свободная навигация)
init python:
    # Канал с фоновыми звуками
    renpy.music.register_channel("ambient", loop=True, mixer="ambient")
    renpy.music.register_channel("hover", loop=False, mixer = "hover")
    renpy.music.register_channel("sound2", loop=False, mixer="sfx")
    renpy.music.register_channel("music1", "music", True)

    if not hasattr(persistent, 'info_panel_shown'):
        persistent.info_panel_shown = False

    onn = ImageDissolve("eye.jpg", 2.0, 80, reverse=False)
    off = ImageDissolve("eye.jpg", 2.0, 20, reverse=True)

# # Функция для воспроизведения звука при наведении НЕ РАБОТАЕТ
# python:
#     def play_hover_sound():
#         renpy.sound.play(hover_sound)

# script.rpy





# init python:
#     import sys
#     import os
#     import renpy
    
#     # Получаем путь к директории игры
#     game_dir = renpy.config.base
    
#     # Добавляем путь к папке game_pygame
#     game_pygame_dir = os.path.join(game_dir, "game_pygame")
    
#     # Проверяем, что путь корректен
#     if not os.path.exists(game_pygame_dir):
#         raise FileNotFoundError(f"Директория {game_pygame_dir} не найдена.")
    
#     sys.path.append(game_pygame_dir)

#     # Теперь можно импортировать модули из game_pygame
#     import pygame
#     import controls
#     from gun import Gun
#     from pygame.sprite import Group
#     from stats import Stats
#     from scores import Scores
#     import pygame.time


#     def StartGame():
#         pygame.init()
#         screen = pygame.display.set_mode((800, 700))
#         pygame.display.set_caption("Коты-защитники")

#         stats = Stats()
#         sc = Scores(screen, stats)
#         bg_color = (220, 220, 220)

#         # Показываем главное меню и ждем действия пользователя
#         menu_result = show_main_menu(screen)

#         if menu_result == "quit":
#             pygame.quit()
#             exit()

#         # После того как игрок выбрал "Начать игру"
#         gun = Gun(screen)
#         bullets = Group()
#         mouses = Group()
#         controls.create_army(screen, mouses)

#         # Основной игровой цикл
#         while True:
#             controls.events(screen, gun, bullets)
#             if stats.run_game:
#                 gun.update_gun()
#                 controls.update(bg_color, screen, stats, sc, gun, mouses, bullets)
#                 controls.update_bullets(screen, stats, sc, mouses, bullets)
#                 controls.update_mouses(stats, screen, sc, gun, mouses, bullets)

#             pygame.display.flip()