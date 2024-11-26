label act3_start:
    # Обнуляем нажатие на подсказку
    $ info_panel_closed_3 = False

    # Логические переменные для отслеживания того, впервые мы появляемся в блоке локации или нет
    # Если впервые, то запускается диалог (КУДА НУЖНО ВСТАВИТЬ РЕПЛИКИ), иначе ничего не происходит
    $ count_lecture_interact = 0
    $ count_frescoes_interact = 0
    $ count_dean_interact = 0
    $ count_ladder_interact = 0
    $ count_hall_interact = 0
    $ count_classes_interact = 0
    $ count_class_interact = 0
    $ count_canteen_interact = 0
    $ count_awards_interact = 0

    "Вы перешли в акт 3"

    # ВСТАВИТЬ ДИАЛОГ

    jump act3_continue

label act3_continue:

    scene bg univer_front with dissolve
    "Вид университета издалека"

    scene bg univer_side with dissolve
    "Вид университета вблизи"
    
    jump act3_hall_pred

    return

# Блок диалога перед интерактивностью или СН в холле вуза
label act3_hall_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg hall with dissolve

    "Вы находитесь в холле с лестницей"  

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_hall_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_hall_interact = 1

    show screen info_panel

    # Показываем подсказку относительно перемещения по локациям, если она ещё не была закрыта
    if not info_panel_closed_3:
        show screen info_panel_3

    # Цикл для ожидания закрытия подсказки
    while not info_panel_closed_3:
        # Ждем, пока подсказка не будет закрыта
        $ renpy.pause(0.1)

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_hall

    return

# Блок интерактивности в холле вуза
label act3_hall:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "hall"

    scene bg hall with dissolve

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg hall with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen unikHall with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide unikHall

    jump showbuttons_unik

    return



# Блок диалога перед интерактивностью или СН в кордиоре с кабинетами
label act3_classes_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg classes with dissolve

    "Вы находитесь в коридоре с кабинетами"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_classes_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_classes_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_classes

    return

# Блок интерактивности в коридоре с кабинетами
label act3_classes:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "classes"

    scene bg classes with dissolve

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg classes with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen unikClasses with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide unikClasses

    jump showbuttons_unik

    return



# Блок диалога перед интерактивностью или СН в столовой
label act3_canteen_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg canteen with dissolve

    "Вы находитесь в столовой"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_canteen_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_canteen_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_canteen

    return

# Блок интерактивности в холле вуза
label act3_canteen:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "canteen"

    scene bg canteen with dissolve

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg canteen with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen unikCanteen with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide unikCanteen

    jump showbuttons_unik

    return


# Блок диалога перед интерактивностью или СН на 2 этаже у лестницы
label act3_ladder_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg ladder with dissolve

    "Вы находитесь на 2 этаже у лестницы"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_ladder_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_ladder_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_ladder

    return

# Блок интерактивности в холле вуза
label act3_ladder:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "ladder"

    scene bg ladder with dissolve

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg ladder with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen unikLadder with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide unikLadder

    jump showbuttons_unik

    return


# Блок диалога перед интерактивностью или СН в лекционной аудитории
label act3_lecture_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg lecture with dissolve

    "Вы находитесь в лекционной аудитории"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_lecture_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_lecture_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_lecture

    return

# Блок интерактивности в лекционной аудитории
label act3_lecture:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "lecture"

    scene bg lecture with dissolve

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg lecture with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen unikLecture with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide unikLecture

    jump showbuttons_unik

    return


# Блок диалога перед интерактивностью или СН в коридоре с фресками
label act3_frescoes_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg frescoes with dissolve

    "Вы находитесь в коридоре с фресками"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_frescoes_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_frescoes_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_frescoes

    return

# Блок интерактивности в холле вуза
label act3_frescoes:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "frescoes"

    scene bg frescoes with dissolve  

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg frescoes with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen unikFrescoes with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide unikFrescoes

    jump showbuttons_unik

    return


# Блок диалога перед интерактивностью или СН перед деканатом
label act3_dean_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg dean with dissolve

    "Вы находитесь перед деканатом"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_dean_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_dean_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_dean

    return

# Блок интерактивности в холле вуза
label act3_dean:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "dean"

    scene bg dean with dissolve 

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg dean with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen unikDean with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide unikDean

    jump showbuttons_unik

    return

label act3_awards_pred:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg awards with dissolve

    "Вы находитесь перед витринами с наградами"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_awards_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_awards_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_awards

    return

label act3_awards:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "awards"

    scene bg awards with dissolve 

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg awards with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen unikAwards with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide unikAwards

    jump showbuttons_unik

    return


# Блок перехода на другую локацию, запускается при нажатии на кнопку "вверх"
label move_unik_up:
    # Убираем экран с кнопками
    hide screen movebuttons_unik

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вверх"
    if current_loc == "hall":
        # Перемещаемся в блок диалога в главном зале бара
        jump act3_ladder_pred

    elif current_loc == "ladder":
        jump act3_frescoes_pred
    elif current_loc == "classes":
        jump act3_awards_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_unik

    return


# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_unik_right:
    # Убираем экран с кнопками
    hide screen movebuttons_unik

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "hall":
        # Перемещаемся в блок диалога в главном зале бара
        jump act3_classes_pred

    elif current_loc == "canteen":
        jump act3_hall_pred
    # Иначе локация недоступна
    elif current_loc == "ladder":
        jump act3_dean_pred
    elif current_loc == "lecture":
        jump act3_ladder_pred
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_unik

    return


# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_unik_left:
    # Убираем экран с кнопками
    hide screen movebuttons_unik

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "hall":
        # Перемещаемся в блок диалога в главном зале бара
        jump act3_canteen_pred

    elif current_loc == "classes":
        jump act3_hall_pred
    elif current_loc == "ladder":
        jump act3_lecture_pred
    elif current_loc == "dean":
        jump act3_ladder_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_street

    return


# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_unik_down:
    # Убираем экран с кнопками
    hide screen movebuttons_unik

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "ladder":
        # Перемещаемся в блок диалога в главном зале бара
        jump act3_hall_pred
    elif current_loc == "frescoes":
        jump act3_ladder_pred
    elif current_loc == "awards":
        jump act3_classes_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_unik

    return

label act3_flashback_start:
    scene bg classes with dissolve
    "Начинается флешбек"
    # ДИАЛОГ, ПОСЛЕ КОТОРОГО ПЕРЕНОСИМСЯ ВО ФЛЕШБЕК
    scene bg flashback2_awakening with dissolve
    "Героя бессовестным образом будят"
    scene bg flashback2_room with dissolve
    "Герой проснулся"
    scene bg flashback2_bathroom with dissolve
    "Герой идет в душ"
    scene bg flashback2_street with dissolve
    "Герой идет в колледж"
    scene bg flashback2_med with dissolve
    "Герой пришел в колледж"
    scene bg flashback2_hall with dissolve
    "Герой прошел пропускной пункт"
    scene bg flashback2_coridor with dissolve
    "Коридор"
    scene bg flashback2_anatomy with dissolve
    "Кабинет анатомии"

    scene bg flashback2_winter_day2 with dissolve
    "Сцены общения с партнером"

    scene bg flashback2_winter_day1 with dissolve

    "Герой и партнер хорошо проводят время"

    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback2_winter_night2 with dissolve

    "Герой и партнер хорошо проводят время"

    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback2_summer_day2 with dissolve

    "Герой и партнер хорошо проводят время"

    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback2_summer_day1 with dissolve

    "Герой и партнер хорошо проводят время"

    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback2_summer_night2 with dissolve

    "Герой и партнер хорошо проводят время"

    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback2_room with dissolve

    # ВСТАВИТЬ РЕПЛИКИ

    "Герою пишет друг"

    scene bg flashback2_partner_home with dissolve

    "Вечеринка, на которой морально уничтожили героя"

    scene bg bar_right with dissolve

    "Герой ушел в запой"

    jump act3_present

    return

label act3_present:
    scene bg classes with dissolve
    "Возвращаемся в коридор после флешбека"
    scene bg class with dissolve
    # ВСТАВИТЬ РЕПЛИКИ
    if friendshp_gh >=7:
        "Герой делится своими переживаниями"
        menu:
            "ВАЖНЫЙ ВЫБОР!"
            "Ты права, компания отравляла мне жизнь, но в мире есть и хорошие люди - например, ты":
                #ВСТАВИТЬ РЕПЛИКИ
                jump act3_end
            "Компания хотела мне только хорошего, они неплохие люди":
                # ВСТАВИТЬ РЕПЛИКИ
                jump act3_end

    else:
        "Герой не делится своими переживаниями"
    
label act3_end:
    scene bg classes with wipeleft
    scene bg hall with wipeleft
    # ВСТАВИТЬ РЕПЛИКИ
    jump act4_start
    return



