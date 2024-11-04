# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gh = Character('Призрак', color="#62496d", image='ghost')
define gg = Character("[playerName]", color="#225c58")
define fr = Character("[friendName]", color="#7a4040")
# Переменные, показывающие, много ли времени провел игрок в комнате общежития
define time = 0
define bool_time = False

# Переменные дружбы
define freindship_fr = 0

# Текущая локация - бар - для свободной навигации
default current_loc = "bar_front"

$ playerName = "Игрок"
$ friendName = "Игрок"
$ friendSprite = ""

#Инициализация звука
init:
    $ hover_sound = "create_character.mp3"  # Путь к вашему звуковому файлу

    # Настраиваем стиль кнопок в меню
    style my_menu_button:
        background "#000"  # Цвет фона по умолчанию
        hover_background "#f00"  # Красный цвет при наведении

# Функция для воспроизведения звука при наведении
python:
    def play_hover_sound():
        renpy.sound.play(hover_sound)


# Игра начинается здесь:
label start:

    scene bg table1

    "Место действия: общежитие"

    "Главный герой звонит узнать, приняли ли его на работу"

    "Игрок" "Здравствуйте, хотелось бы узнать, берете ли Вы меня в свою компанию?"

    "Работодатель" "Здравствуйте, скажите свое имя, чтобы я уточнил информацию"

    jump create_character

    return

label create_character:

    menu:
        "Кто вы?"

        "♂ Я приехал из другого города.":
            $ renpy.sound.play(hover_sound)
            $ playerName = renpy.input("Введите мужское имя", length=12).strip() or "Михаил"
            $ gender_symbol = "♂"
            $ friendSprite = "boy"
            $ friendName = "Владимир"
            # Настраиваем окончания для мужского рода
            $ verb_end = ""
            $ past_verb_end = "л"
            
        "♀ Я приехала из другого города.":
            $ renpy.sound.play(hover_sound)
            $ playerName = renpy.input("Введите женское имя", length=12).strip() or "Алиса"
            $ gender_symbol = "♀"
            $ friendSprite = "girl"
            $ friendName = "Лиза"
            # Настраиваем окончания для женского рода
            $ verb_end = "а"
            $ past_verb_end = "ла"

    # Показываем предупреждение, что пересоздать персонажа будет нельзя
    "Отнеситесь серьезно к созданию персонажа, так как потом пересоздать будет нельзя."

    menu:
        "Что вы хотите сделать?"
        "Продолжить":
            jump continue_start
        "Пересоздать":
            jump create_character

    return

label continue_start:

    gg "Мое имя - [playerName]"

    "Работодатель" "Извините, [playerName], Вы нам не подходите."

    gg "Какое же я ничтожество"

    jump room

    return

#Герой описывает комнату
label room:

    scene bg room2 with dissolve

    "Герой описывает комнату."

    jump move_in_room

    return

label move_in_room:

    window hide

    if not persistent.background_shown:
        show bg room2 with dissolve
        $ persistent.background_shown = True

    show screen mapScreen with dissolve

    $ result = ui.interact()

#Коридор общаги
label go_to_hall:

    show bg hall2 with dissolve

    "Спустя некоторое время блужданий по общаге..."

    # Проверяем, если игрок "тыкался" больше 15 раз
    if time >= 7:
        $ bool_time = True

    "Главный герой идет в бар"

    jump bar_outside

    return

label bar_outside:

    # Очистка экрана, чтобы убрать предыдущие текст и изображения
    scene bg bar_outside with dissolve

    #вставить спрайт персонажа-друга с плавным появлением

    # Проверка, провел ли игрок слишком много времени в комнате
    if bool_time:
        fr "[playerName], ты чего так долго? Я уже уста[past_verb_end] тебя ждать!!!"
        gg "Прости, действительно много времени уже прошло..."
    else:
        fr "Привет, [playerName], давно не виделись с тобой!"
        gg "Рад[verb_end] тебя видеть, [friendName]!"

    fr "Рассказывай, как у тебя дела?"

    menu:
        "Внимание! Ваш выбор повлияет на отношения с данным персонажем."

        "Рассказать о проблемах в поиске работы":
            $ freindship_fr += 1
            gg "Да никак не могу найти себе работу..."
            fr "Не волнуйся, у тебя все обязательно получится, я в тебя верю!"

        "Не доверять другу свои проблемы":
            $ freindship_fr -= 1
            gg "Все нормально. Пожалуйста, не устраивай мне допросы."
            fr "...Вижу ты не в настроении...хаха..извини, что заде[past_verb_end] тебя..."

    "Друзья поговорили. Друг предлагает зайти в бар. Вход подсвечивается."

    if not persistent.background_shown:
        show bg bar_outside with dissolve
        $ persistent.background_shown = True

    show screen barScreen with dissolve

    $ result = ui.interact()

    jump bar_inside

    return

label bar_inside:

    show bg bar_people
    with fade

    "Герои зашли в бар"

    "Диалог в баре"

    jump bar_interact

    return

# Свободная навигация в баре
label bar_interact:

    show bg bar_people
    with dissolve

    "Запущено свободное перемещение по бару"

    $ current_loc = "bar_front"

    jump showbuttons

    return


label bar_up:
    scene bg bar_up with dissolve

    $ current_loc = "bar_up"

    "Вы находитесь в баре посередине"

    # Покажите кнопки после показа фона
    jump showbuttons

    return

# Переход на внутреннюю локацию
label move_bar_up:
    hide screen movebuttons

    if current_loc == "bar_front":
        jump bar_up
    elif current_loc == "bar_down":
        jump bar_interact
    else:
        "location not available"
        jump showbuttons

    return

label bar_right:
    scene bg bar_right with dissolve

    $ current_loc = "bar_right"

    "Вы находитесь в баре с правой стороны"

    # Покажите кнопки после показа фона
    jump showbuttons

    return

# Переход на внутреннюю локацию
label move_bar_right:
    hide screen movebuttons

    if current_loc == "bar_front":
        jump bar_right
    elif current_loc == "bar_left":
        jump bar_interact
    else:
        "location not available"
        jump showbuttons

    return

label bar_left:
    scene bg bar_left with dissolve

    $ current_loc = "bar_left"

    "Вы находитесь в баре с левой стороны"

    # Покажите кнопки после показа фона
    jump showbuttons

    return

# Переход на внутреннюю локацию
label move_bar_left:
    hide screen movebuttons

    if current_loc == "bar_front":
        jump bar_left
    elif current_loc == "bar_right":
        jump bar_interact
    else:
        "location not available"
        jump showbuttons

    return

label bar_down:
    scene bg bar_down with dissolve

    $ current_loc = "bar_down"

    "Вы вышли из бара"

    # Покажите кнопки после показа фона
    jump showbuttons

    return

# Переход на внутреннюю локацию
label move_bar_down:
    hide screen movebuttons

    if current_loc == "bar_front":
        jump bar_down
    elif current_loc == "bar_up":
        jump bar_interact
    else:
        "location not available"
        jump showbuttons

    return




    


