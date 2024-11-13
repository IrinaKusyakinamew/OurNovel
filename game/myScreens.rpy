# Блок, внутри которого определены экраны
label myScreens:

# Интерактивный экран комнаты общежития
screen mapScreen:

    # Интерактивный объект - стул
    imagebutton:
        # Координаты стула
        xpos 400
        ypos 395
        # Изображение объекта, когда он не активен
        idle "room_interact_objects/room_chair_idle.png"
        # Изображение объекта при наведении на него курсора
        hover "room_interact_objects/room_chair_hover.png"
        # Действия, выполняющиеся при нажатии на объект
        action [SetVariable("time", time + 1), Jump("room_chair")] # Инкрементация переменной time и переход в блок описания объекта

    # Интерактивный объект - ноутбук
    imagebutton:
    # Координаты ноутбука
        xpos 322
        ypos 319
        # Изображение объекта, когда он не активен
        idle "room_interact_objects/room_laptop_idle.png"
        # Изображение объекта при наведении на него курсора
        hover "room_interact_objects/room_laptop_hover.png"
        # Действия, выполняющиеся при нажатии на объект
        action [SetVariable("time", time + 1), Jump("room_laptop")] # Инкрементация переменной time и переход в блок описания объекта

    # Интерактивный объект - кровать
    imagebutton:
        xpos 998
        ypos 355
        idle "room_interact_objects/room_bed_idle.png"
        hover "room_interact_objects/room_bed_hover.png"
        action [SetVariable("time", time + 1), Jump("room_bed")]

    # Интерактивный объект - мусор
    imagebutton:
        xpos 716
        ypos 523
        idle "room_interact_objects/room_trash_idle.png"
        hover "room_interact_objects/room_trash_hover.png"
        action [SetVariable("time", time + 1), Jump("room_trash")]
        

    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        # Закрываем интерактивный экран, инкрементируем переменную и перемещаемся в новый блок
        action [Hide('mapScreen'), SetVariable("time", time + 1), Jump("go_to_hall")]

screen barScreen:
    imagebutton:
        xpos 765
        ypos 288
        idle "bar_outside_interact_object/bg bar_idle.jpg"
        hover "bar_outside_interact_object/bg bar_hover.jpg"
        action [Hide("barScreen"), Jump("bar_inside")]


screen barInteract:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("barInteract"), Jump("bar_interact")]


    imagebutton:
        xpos 751
        ypos 371
        idle "bar_interact_objects/bar_interact_girl1_idle.png"
        hover "bar_interact_objects/bar_interact_girl1_hover.png"
        action Jump("bar_interact_girl1")

    imagebutton:
        xpos 969
        ypos 383
        idle "bar_interact_objects/bar_interact_girl2_idle.png"
        hover "bar_interact_objects/bar_interact_girl2_hover.png"
        action Jump("bar_interact_girl2")

    imagebutton:
        xpos 1640
        ypos 346
        idle "bar_interact_objects/bar_interact_man1_idle.png"
        hover "bar_interact_objects/bar_interact_man1_hover.png"
        action Jump("bar_interact_man1")

    imagebutton:
        xpos 54
        ypos 385
        idle "bar_interact_objects/bar_interact_man2_idle.png"
        hover "bar_interact_objects/bar_interact_man2_hover.png"
        action Jump("bar_interact_man2")

screen barUp:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("barUp"), Jump("bar_up")]

    imagebutton:
        xpos 734
        ypos 509
        idle "bar_up_interact_objects/bottles1_idle.png"
        hover "bar_up_interact_objects/bottles1_hover.png"
        action Jump("bottles1")

    imagebutton:
        xpos 0
        ypos 178
        idle "bar_up_interact_objects/bottles2_idle.png"
        hover "bar_up_interact_objects/bottles2_hover.png"
        action Jump("bottles2")

    imagebutton:
        xpos 1515
        ypos 84
        idle "bar_up_interact_objects/bar_up_stand_idle.png"
        hover "bar_up_interact_objects/bar_up_stand_hover.png"
        action Jump("bar_up_stand")

    imagebutton:
        xpos 381
        ypos 52
        idle "bar_up_interact_objects/bar_up_window_idle.png"
        hover "bar_up_interact_objects/bar_up_window_hover.png"
        action Jump("bar_up_window")    

    imagebutton:
        xpos 705
        ypos 834
        idle "bar_up_interact_objects/bar_up_blood_idle.png"
        hover "bar_up_interact_objects/bar_up_blood_hover.png"
        action Jump("bar_up_blood")   

screen barRight:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("barRight"), Jump("bar_right")]

    imagebutton:
        xpos 0
        ypos 0
        idle "bar_right_interact_object/bar_right_bottles_idle.png"
        hover "bar_right_interact_object/bar_right_bottles_hover.png"
        action Jump("bar_right_bottles")

    imagebutton:
        xpos 1794
        ypos 316
        idle "bar_right_interact_object/bar_right_stand_idle.png"
        hover "bar_right_interact_object/bar_right_stand_hover.png"
        action Jump("bar_right_stand")

    imagebutton:
        xpos 987
        ypos 526
        idle "bar_right_interact_object/bar_right_bottles1_idle.png"
        hover "bar_right_interact_object/bar_right_bottles1_hover.png"
        action Jump("bar_right_bottles1")

    imagebutton:
        xpos 1569
        ypos 385
        idle "bar_right_interact_object/bar_right_woman_idle.png"
        hover "bar_right_interact_object/bar_right_woman_hover.png"
        action Jump("bar_right_woman")

screen barLeft:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("barLeft"), Jump("bar_left")]

    imagebutton:
        xpos 1520
        ypos 0
        idle "bar_left_interact_objects/bar_left_bottles1_idle.png"
        hover "bar_left_interact_objects/bar_left_bottles1_hover.png"
        action Jump("bar_left_bottles1")

    imagebutton:
        xpos 612
        ypos 670
        idle "bar_left_interact_objects/bar_left_glass_idle.png"
        hover "bar_left_interact_objects/bar_left_glass_hover.png"
        action Jump("bar_left_glass")

    imagebutton:
        xpos 928
        ypos 546
        idle "bar_left_interact_objects/bar_left_bottle_idle.png"
        hover "bar_left_interact_objects/bar_left_bottle_hover.png"
        action Jump("bar_left_bottle")

    imagebutton:
        xpos 1199
        ypos 296
        idle "bar_left_interact_objects/bar_left_man_idle.png"
        hover "bar_left_interact_objects/bar_left_man_hover.png"
        action Jump("bar_left_man")


# Экран с подсказкой
screen info_panel:
    # Показывать экран только если подсказка ещё не была показана
    if not info_panel_closed:
        frame:
            padding(30, 30)
            xalign 0.5
            yalign 0.5
            xsize 1270
            vbox:
                xsize 1270
                text "Внимание! На различных локациях перед вами будет стоять выбор подключения к режиму интерактивности."
                text "Если вы осуществите подключение, по окончании исследования фона не забудьте нажать голубую кнопку для выхода из интерактивного режима."
                text "Пока вы не нажмете голубую кнопку в правой нижней части экрана, стрелки для перемещения по локациям отображены не будут"
                text "Если вы хотите выйти из режима свободной навигации, нажмите стрелочку вниз, находясь в начальной локации бара"
                null height 15
                textbutton "ЗАКРЫТЬ" action [
                    Hide("info_panel"), 
                    SetVariable("info_panel_closed", True)  # Устанавливаем флаг, что подсказка была показана и закрыта
                ] xalign 0.5

# Экран с подсказкой
screen info_panel_door:
    # Показывать экран только если подсказка ещё не была показана
    if not info_panel_closed:
        frame:
            padding(30, 30)
            xalign 0.5
            yalign 0.5
            xsize 970
            vbox:
                xsize 970
                text "Внимание! Нажмите на дверь, чтобы зайти в бар."
                null height 15
                textbutton "ЗАКРЫТЬ" action [
                    Hide("info_panel_door"), 
                    SetVariable("info_panel_closed_1", True)  # Устанавливаем флаг, что подсказка была показана и закрыта
                ] xalign 0.5

