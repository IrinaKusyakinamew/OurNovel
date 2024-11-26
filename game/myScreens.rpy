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

    # imagebutton:
    #     xpos 1640
    #     ypos 346
    #     idle "bar_interact_objects/bar_interact_man1_idle.png"
    #     hover "bar_interact_objects/bar_interact_man1_hover.png"
    #     action Jump("bar_interact_man1")

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

# Интерактивный экран центральной части улицы
screen streetFront:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("streetFront"), Jump("act2_front")]

    imagebutton:
        xpos 332
        ypos 575
        idle "street_interact_objects/ghost_idle.png"
        hover "street_interact_objects/ghost_hover.png"
        action Jump("ghost")

    imagebutton:
        xpos 1483
        ypos 0
        idle "street_interact_objects/street_interact_house_idle.png"
        hover "street_interact_objects/street_interact_house_hover.png"
        action Jump("street_interact_house")

# Интерактивный экран верхней части улицы
screen streetUp:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("streetUp"), Jump("act2_up")]

# Интерактивный экран правой части улицы
screen streetRight:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("streetRight"), Jump("act2_right")]

    imagebutton:
        xpos 0
        ypos 255
        idle "street_right_interact_objects/street_right_clouds_idle.png"
        hover "street_right_interact_objects/street_right_clouds_hover.png"
        action Jump("street_right_clouds")

    imagebutton:
        xpos 793
        ypos 171
        idle "street_right_interact_objects/street_right_tree_idle.png"
        hover "street_right_interact_objects/street_right_tree_hover.png"
        action Jump("street_right_tree")

# Интерактивный экран левой части улицы
screen streetLeft:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("streetLeft"), Jump("act2_left")]

    imagebutton:
        xpos 1360
        ypos 0
        idle "street_left_interact_objects/street_left_house_idle.png"
        hover "street_left_interact_objects/street_left_house_hover.png"
        action Jump("street_left_house")

    imagebutton:
        xpos 331
        ypos 25
        idle "street_left_interact_objects/street_left_tree_idle.png"
        hover "street_left_interact_objects/street_left_tree_hover.png"
        action Jump("street_left_tree")

# Интерактивный экран левой части улицы
screen streetDown:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("streetDown"), Jump("act2_down")]


screen galleryFront:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("galleryFront"), Jump("act2_front_gallery")]

    imagebutton:
        xpos 830
        ypos 522
        idle "gallery_interact_objects/gallery_interact_arc_idle.png"
        hover "gallery_interact_objects/gallery_interact_arc_hover.png"
        action Jump("gallery_interact_arc")

    imagebutton:
        xpos 1618
        ypos 165
        idle "gallery_interact_objects/gallery_interact_window_idle.png"
        hover "gallery_interact_objects/gallery_interact_window_hover.png"
        action Jump("gallery_interact_window")

    imagebutton:
        xpos 397
        ypos 620
        idle "gallery_interact_objects/gallery_interact_award_idle.png"
        hover "gallery_interact_objects/gallery_interact_award_hover.png"
        action Jump("gallery_interact_award")

screen galleryUp:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("galleryUp"), Jump("act2_up_gallery")]

screen galleryRight:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("galleryRight"), Jump("act2_right_gallery")]

    imagebutton:
        xpos 508
        ypos 37
        idle "gallery_right_interact_objects/gallery_right_wall_idle.png"
        hover "gallery_right_interact_objects/gallery_right_wall_hover.png"
        action Jump("gallery_right_wall")

screen galleryLeft:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("galleryLeft"), Jump("act2_left_gallery")]

    imagebutton:
        xpos 681
        ypos 173
        idle "gallery_left_interact_objects/gallery_left_beautiful_painting_idle.png"
        hover "gallery_left_interact_objects/gallery_left_beautiful_painting_hover.png"
        action Jump("gallery_left_beautiful_painting")

screen galleryDown:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("galleryDown"), Jump("act2_down_gallery")]

screen roomScreen:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("roomScreen"), Jump("act2_flashback_graffity")]

    imagebutton:
        xpos 0
        ypos 626
        idle "room_objects/room_objects_bed_idle.png"
        hover "room_objects/room_objects_bed_hover.png"
        action Jump("room_objects_bed")

    imagebutton:
        xpos 307
        ypos 606
        idle "room_objects/room_objects_lamp_idle.png"
        hover "room_objects/room_objects_lamp_hover.png"
        action Jump("room_objects_lamp")

    imagebutton:
        xpos 570
        ypos 202
        idle "room_objects/room_objects_window_idle.png"
        hover "room_objects/room_objects_window_hover.png"
        action Jump("room_objects_window")

    imagebutton:
        xpos 720
        ypos 649
        idle "room_objects/room_objects_table_idle.png"
        hover "room_objects/room_objects_table_hover.png"
        action Jump("room_objects_table")

    imagebutton:
        xpos 1590
        ypos 153
        idle "room_objects/room_objects_door_idle.png"
        hover "room_objects/room_objects_door_hover.png"
        action Jump("room_objects_door")


screen unikHall:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("unikHall"), Jump("act3_hall")]

screen unikCanteen:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("unikCanteen"), Jump("act3_canteen")]

screen unikClasses:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("unikClasses"), Jump("act3_classes")]

    imagebutton:
        xpos 196
        ypos 33
        idle "unik_classes_interact_objects/unik_classes_door1_idle.png"
        hover "unik_classes_interact_objects/unik_classes_door1_hover.png"
        action Jump("unik_classes_door1")

    imagebutton:
        xpos 591
        ypos 196
        idle "unik_classes_interact_objects/unik_classes_door2_idle.png"
        hover "unik_classes_interact_objects/unik_classes_door2_hover.png"
        action Jump("unik_classes_door2")

screen unikAwards:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("unikAwards"), Jump("act3_awards")]

screen unikLadder:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("unikLadder"), Jump("act3_ladder")]

screen unikDean:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("unikDean"), Jump("act3_dean")]

    imagebutton:
        xpos 610
        ypos 136
        idle "unik_dean_interact_objects/unik_dean_door_idle.png"
        hover "unik_dean_interact_objects/unik_dean_door_hover.png"
        action Jump("unik_dean_door")

screen unikFrescoes:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("unikFrescoes"), Jump("act3_frescoes")]

screen unikLecture:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [SetVariable("closed", True), Hide("unikLecture"), Jump("act3_lecture")]

screen bagInteract:
    # Кнопка выхода из интерактивного режима
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "blue_idle"
        hover "blue_hover"
        action [Hide("bagInteract"), Jump("act2_gallery")]

    imagebutton:
        xpos 504
        ypos 324
        idle "street_interact_objects/street_interact_bag_idle.png"
        hover "street_interact_objects/street_interact_bag_hover.png"
        action Jump("street_interact_bag")
        
    imagebutton:
        xpos 594
        ypos 744
        idle "street_interact_objects/street_interact_phone_idle.png"
        hover "street_interact_objects/street_interact_phone_hover.png"
        action Jump("street_interact_phone")


# Экран с подсказкой
screen info_panel:
    # Показывать экран только если подсказка ещё не была показана
    if not info_panel_closed:
        frame:
            padding(30, 30)
            xalign 0.5
            yalign 0.5
            xsize 1470
            vbox:
                xsize 1470
                text "Внимание! Вы находитесь в режиме интерактивности."
                text "Для того, чтобы выйти из данного режима, нажмите на кнопку выхода в правом нижнем углу."
                text "Когда вы сделаете это, в левом нижнем углу появятся стрелки навигации."
                text "Используйте их для перемещения между локациями."
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
            xsize 1470
            vbox:
                xsize 1470
                text "Внимание! Вы вошли в интерактивный режим. После завершения исследования локации нажмите на кнопку выхода внизу слева."
                null height 15
                textbutton "ЗАКРЫТЬ" action [
                    Hide("info_panel_door"), 
                    SetVariable("info_panel_closed_1", True)  # Устанавливаем флаг, что подсказка была показана и закрыта
                ] xalign 0.5

# Экран с подсказкой
screen info_panel_2:
    # Показывать экран только если подсказка ещё не была показана
    if not info_panel_closed_2:
        frame:
            padding(30, 30)
            xalign 0.5
            yalign 0.5
            xsize 1470
            vbox:
                xsize 1470
                text "Внимание! Вы находитесь в режиме интерактивности."
                text "Для того, чтобы выйти из данного, нажмите на кнопку выхода в правом нижнем углу."
                text "Когда вы сделаете это, в левом нижнем углу появятся стрелки навигации."
                text "Используйте их для перемещения между локациями."
                null height 15
                textbutton "ЗАКРЫТЬ" action [
                    Hide("info_panel_2"), 
                    SetVariable("info_panel_closed_2", True)  # Устанавливаем флаг, что подсказка была показана и закрыта
                ] xalign 0.5


# Экран с подсказкой
screen info_panel_3:
    # Показывать экран только если подсказка ещё не была показана
    if not info_panel_closed_3:
        frame:
            padding(30, 30)
            xalign 0.5
            yalign 0.5
            xsize 1470
            vbox:
                xsize 1470
                text "Внимание! На различных локациях перед вами будет стоять выбор подключения к режиму интерактивности."
                text "Если вы осуществите подключение, по окончании исследования фона не забудьте нажать голубую кнопку для выхода из интерактивного режима."
                text "Пока вы не нажмете голубую кнопку в правой нижней части экрана, стрелки для перемещения по локациям отображены не будут"
                text "Если вы хотите выйти из режима свободной навигации, нажмите стрелочку вниз, находясь в начальной локации бара"
                null height 15
                textbutton "ЗАКРЫТЬ" action [
                    Hide("info_panel_3"), 
                    SetVariable("info_panel_closed_3", True)  # Устанавливаем флаг, что подсказка была показана и закрыта
                ] xalign 0.5

