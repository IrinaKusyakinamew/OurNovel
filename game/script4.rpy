label act4_start:
    "Вы перешли в 4 акт"
    scene bg graffity with dissolve
    "Сцена у граффити"
    scene bg estate with dissolve
    "Усадьба"
    jump act4_estate
    return

label act4_estate:
    # Логические переменные для отслеживания того, впервые мы появляемся в блоке локации или нет
    # Если впервые, то запускается диалог (КУДА НУЖНО ВСТАВИТЬ РЕПЛИКИ), иначе ничего не происходит
    $ count_pred_interact = 0
    $ count_pred_right = 0
    $ count_pred_left = 0
    $ count_pred_down = 0
    $ k = 0
    jump act4_estate_hall_pred
    return

label act4_estate_hall_pred:
    scene bg estate_hall with dissolve

    "Вы в холле"

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_interact==0:

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act4_estate_hall

    return

label act4_estate_hall:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "estate_hall"

    scene bg estate_hall with dissolve

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg estate_hall with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen estateHall with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide estateHall

    jump showbuttons_estate

    return

label act4_estate_room_pred:
    scene bg estate_room with dissolve

    "Вы в комнате Наоми"

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_right==0:

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_right = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act4_estate_room

    return

label act4_estate_room:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "estate_room"

    scene bg estate_room with dissolve

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg estate_room with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen estateRoom with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide estateRoom

    jump showbuttons_estate

    return

label act4_estate_kitchen_pred:
    scene bg estate_kitchen with dissolve

    "Вы на кухне"

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_left==0:

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_left = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act4_estate_kitchen

    return

label act4_estate_kitchen:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "estate_kitchen"

    scene bg estate_kitchen with dissolve

    jump showbuttons_estate

    return

label act4_estate_balkon_pred:
    scene bg estate_balkon with dissolve

    "Вы на балконе"

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_down==0:

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_down = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act4_estate_balkon

    return

label act4_estate_balkon:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "estate_balkon"

    scene bg estate_balkon with dissolve

    jump showbuttons_estate

    return

# # Блок перехода на другую локацию, запускается при нажатии на кнопку "вверх"
# label move_estate_up:
#     # Убираем экран с кнопками
#     hide screen movebuttons_estate

#     # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вверх"
#     if current_loc == "estate_balkon":
#         # Перемещаемся в блок диалога в главном зале бара
#         jump act4_estate_hall_pred
#     # Иначе локация недоступна
#     else:
#         "Локация недоступна"
#         # Переходим в блок, который открывает экран с кнопками навигации
#         jump showbuttons_estate

#     return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_estate_right:
    # Убираем экран с кнопками
    hide screen movebuttons_estate

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "estate_kitchen":
        # Перемещаемся в блок диалога в главном зале бара
        jump act4_estate_hall_pred
    elif current_loc == "estate_hall":
        jump act4_estate_room_pred
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_estate

    return


# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_estate_left:
    # Убираем экран с кнопками
    hide screen movebuttons_estate

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "estate_room":
        # Перемещаемся в блок диалога в главном зале бара
        jump act4_estate_hall_pred
    elif current_loc == "estate_hall":
        jump act4_estate_kitchen_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_estate

    return


# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_estate_down:
    # Убираем экран с кнопками
    hide screen movebuttons_estate

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "estate_hall":
        # Перемещаемся в блок диалога в главном зале бара
        jump act4_estate_balkon_pred
    elif current_loc == "estate_balkon":
        jump act4_estate_hall_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_estate

    return

label act4_continue:
    scene bg estate_room with dissolve
    "Эта картина получилась поистине великолепной"
    jump act5_start
    return
