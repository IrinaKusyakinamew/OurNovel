#определяем персонажей игры
define gh = Character('Призрак', color="#6d457e", image='ghost') #призрак
define gg = Character("[playerName]", color="#3b2f73") #гг
define fr = Character("[friendName]", color="#5f2626") #друг гг
define par = Character("[partnerName]", color="#481919") #любовный интерес гг
define barman = Character('Бармен', color="#294232", image='barman') #бармен

#определяем телефонных персонажей
define gg_nvl = Character("я", kind=nvl, callback=Phone_SendSound)
define fr_nvl = Character("Заноза", kind=nvl, callback=Phone_ReceiveSound)
define hr_nvl = Character("HR", kind=nvl, callback=Phone_ReceiveSound)

#переменные для плавного исчезновения телефона
define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

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

    g.button("ending1")
    g.condition("persistent.ending1")
    g.image("lonely_end_b")

    g.button("ending2")
    g.condition("persistent.ending2")
    g.image("lonely_end_g")

#переменные, отвечающие за расположение персонажей сбоку
init:
    $ left2 = Position(xalign = 0.2)
    $ right2 = Position(xalign = 0.7)

#переменные, необходимые для грамотного отображения текста в интерактивном режиме
define barman_click = 0
define girl_click = 0

#переменная, хранящая текущую локацию
default current_state = "default"

# Переменные, показывающие, много ли времени провел игрок в комнате общежития
define time = 0
define bool_time = False

# Переменная для отслеживания состояния подсказки
define info_panel_closed = False
define info_panel_closed_1 = False
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

#Инициализация звука НЕ РАБОТАЕТ
init:
    $ hover_sound = "sounds/create_character.mp3"

# Переменная для отслеживания состояния всплывающей подсказки в баре (свободная навигация)
init python:
    # Канал с фоновыми звуками
    renpy.music.register_channel("ambient", loop=True, mixer="ambient")
    renpy.music.register_channel("hover", loop=False, mixer = "hover")
    renpy.music.register_channel("sound2", loop=False, mixer="sfx")
    renpy.music.register_channel("music1", "music", True)

    if not hasattr(persistent, 'info_panel_shown'):
        persistent.info_panel_shown = False

# Функция для воспроизведения звука при наведении НЕ РАБОТАЕТ
python:
    def play_hover_sound():
        renpy.sound.play(hover_sound)



