# Блок: начало второго акта
label act2_start:
    # Обнуляем нажатие на подсказку
    $ info_panel_closed = False

    # Логические переменные для отслеживания того, впервые мы появляемся в блоке локации или нет
    # Если впервые, то запускается диалог (КУДА НУЖНО ВСТАВИТЬ РЕПЛИКИ), иначе ничего не происходит
    $ count_pred_interact = 0
    $ count_pred_up = 0
    $ count_pred_right = 0
    $ count_pred_left = 0
    $ count_pred_down = 0

    $ count_act2_front_pred = 0
    
    "Вы перешли во второй акт"

    # ВСТАВИТЬ ДИАЛОГ

    jump act2_front_pred

    return

# Блок диалога перед интерактивностью или СН в центральной части улицы
label act2_front_pred:
    $ count_act2_front_pred += 1

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg bar_down_ghost with dissolve

    "Вы находитесь в центре улицы"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_front

    return

# Блок интерактивности в центральной части улицы
label act2_front:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    scene bg bar_down_ghost with dissolve

    show screen info_panel

    # Показываем подсказку относительно перемещения по локациям, если она ещё не была закрыта
    if not info_panel_closed:
        show screen info_panel

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "street_front"

    # Цикл для ожидания закрытия подсказки
    while not info_panel_closed:
        # Ждем, пока подсказка не будет закрыта
        $ renpy.pause(0.1)  

    # # После того как подсказка закрыта, показываем меню выбора, если мы еще не включали интерактивный экран
    # if interactive_mode_ended_interact == 0:
    #     menu:
    #         "Осмотреться":
    #             # Закрываем диалоговое окно
    #             window hide

    #             # Показываем фон главного зала в баре, если он не был показан ранее
    #             if not persistent.background_shown:
    #                 show bg bar_down_ghost with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True

    #             # Запускаем интерактивный экран
    #             show screen streetFront with dissolve

    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"

    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_interact = 1

    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             $ count_act2_front_pred += 1
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons_street

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    #     while not closed:
    #         # Закрываем диалоговое окно
    #         window hide
    #         # Показываем фон главного зала в баре, если он не был показан ранее
    #         if not persistent.background_shown:
    #             show bg bar_down_ghost with dissolve
    #             # Меняем глобальную переменную на True, так как фон был показан
    #             $ persistent.background_shown = True

    #         # Запускаем интерактивный экран
    #         show screen streetFront with dissolve

    #         # Включаем интерактивное взаимодействие
    #         $ result = ui.interact()

    #     # Если цикл прервался, то мы нажали на кнопку, значит, можно поместить на экран кнопки навигации
    #     jump showbuttons_street

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg bar_down_ghost with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen streetFront with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide streetFront

    jump showbuttons_street

    return


# Блок диалога перед интерактивностью или СН в верхней части улицы
label act2_up_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    # Показываем фон верхней части улицы
    scene bg street_up with dissolve

    "Вы находитесь в верхней части улицы"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_up==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_up = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_up

    return

# Блок интерактивности в верхней части улицы
label act2_up:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "street_up"

    # Показываем фон верхней части улицы
    scene bg street_up with dissolve

    # # После того как подсказка закрыта, показываем меню выбора, если мы еще не включали интерактивный экран
    # if interactive_mode_ended_up == 0:
    #     menu:
    #         "Осмотреться":

    #             # Закрываем диалоговое окно
    #             window hide

    #             # Показываем фон главного зала в баре, если он не был показан ранее
    #             if not persistent.background_shown:
    #                 show bg street_up with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True

    #             # Запускаем интерактивный экран
    #             show screen streetUp with dissolve

    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"

    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_up = 1

    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons_street

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    #     while not closed:
    #         # Закрываем диалоговое окно
    #         window hide
    #         # Показываем фон главного зала в баре, если он не был показан ранее
    #         if not persistent.background_shown:
    #             show bg street_up with dissolve
    #             # Меняем глобальную переменную на True, так как фон был показан
    #             $ persistent.background_shown = True

    #         # Запускаем интерактивный экран
    #         show screen streetUp with dissolve

    #         # Включаем интерактивное взаимодействие
    #         $ result = ui.interact()

    #     # Если цикл прервался, то мы нажали на кнопку, значит, можно поместить на экран кнопки навигации
    #     jump showbuttons_street

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg street_up with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen streetUp with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide streetUp

    jump showbuttons_street

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вверх"
label move_street_up:

    # Убираем экран с кнопками
    hide screen movebuttons_street

    # Если текущая позиция - центр улицы, то при нажатии на кнопку "вверх"
    if current_loc == "street_front":
        # Перемещаемся в блок диалога в верхней части улицы
        jump act2_up_pred
    # Иначе локация недоступна
    elif current_loc == "street_down":
        jump act2_front_pred
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_street

    return

# Блок диалога перед интерактивностью или СН в правой части улицы    
label act2_right_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    # Показываем фон верхней части улицы
    scene bg street_right with dissolve

    "Вы находитесь в правой части улицы"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_right==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_right = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_right

    return

# Блок интерактивности в правой части улицы
label act2_right:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "street_right"

    # Показываем фон верхней части улицы
    scene bg street_right with dissolve

    # # После того как подсказка закрыта, показываем меню выбора, если мы еще не включали интерактивный экран
    # if interactive_mode_ended_right == 0:
    #     menu:
    #         "Осмотреться":

    #             # Закрываем диалоговое окно
    #             window hide

    #             # Показываем фон главного зала в баре, если он не был показан ранее
    #             if not persistent.background_shown:
    #                 show bg street_right with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True

    #             # Запускаем интерактивный экран
    #             show screen streetRight with dissolve

    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"

    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_right = 1

    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons_street

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    #     while not closed:
    #         # Закрываем диалоговое окно
    #         window hide
    #         # Показываем фон главного зала в баре, если он не был показан ранее
    #         if not persistent.background_shown:
    #             show bg street_right with dissolve
    #             # Меняем глобальную переменную на True, так как фон был показан
    #             $ persistent.background_shown = True

    #         # Запускаем интерактивный экран
    #         show screen streetRight with dissolve

    #         # Включаем интерактивное взаимодействие
    #         $ result = ui.interact()

    #     # Если цикл прервался, то мы нажали на кнопку, значит, можно поместить на экран кнопки навигации
    #     jump showbuttons_street

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg street_right with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen streetRight with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide streetRight

    jump showbuttons_street

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вправо"
label move_street_right:

    # Убираем экран с кнопками
    hide screen movebuttons_street

    # Если текущая позиция - центр улицы, то при нажатии на кнопку "вправо"
    if current_loc == "street_front":
        # Перемещаемся в блок диалога в центре улицы
        jump act2_right_pred
    # Иначе если текущая позиция - левая часть улицы, то при нажатии на кнопку "вправо"
    elif current_loc == "street_left":
        # Перемещаемся в блок диалога в центр улицы
        jump act2_front_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_street

    return


# Блок диалога перед интерактивностью или СН в левой части улицы
label act2_left_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    # Показываем фон верхней части улицы
    scene bg street_left with dissolve

    "Вы находитесь в левой части улицы"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_left==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_left = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_left

    return

# Блок интерактивности в левой части улицы
label act2_left:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "street_left"

    # Показываем фон левой части улицы
    scene bg street_left with dissolve

    # # После того как подсказка закрыта, показываем меню выбора, если мы еще не включали интерактивный экран
    # if interactive_mode_ended_left == 0:
    #     menu:
    #         "Осмотреться":

    #             # Закрываем диалоговое окно
    #             window hide

    #             # Показываем фон главного зала в баре, если он не был показан ранее
    #             if not persistent.background_shown:
    #                 show bg street_left with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True

    #             # Запускаем интерактивный экран
    #             show screen streetLeft with dissolve

    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"

    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_left = 1

    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons_street

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    #     while not closed:
    #         # Закрываем диалоговое окно
    #         window hide
    #         # Показываем фон главного зала в баре, если он не был показан ранее
    #         if not persistent.background_shown:
    #             show bg street_left with dissolve
    #             # Меняем глобальную переменную на True, так как фон был показан
    #             $ persistent.background_shown = True

    #         # Запускаем интерактивный экран
    #         show screen streetLeft with dissolve

    #         # Включаем интерактивное взаимодействие
    #         $ result = ui.interact()

    #     # Если цикл прервался, то мы нажали на кнопку, значит, можно поместить на экран кнопки навигации
    #     jump showbuttons_street

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg street_left with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen streetLeft with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide streetLeft

    jump showbuttons_street

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "влево"
label move_street_left:
    # Убираем экран с кнопками
    hide screen movebuttons_street

    # Если текущая позиция - главный зал бара, то при нажатии на кнопку "влево"
    if current_loc == "street_front":
        # Перемещаемся в блок диалога в левой части бара
        jump act2_left_pred
    # Иначе если текущая позиция - правая часть бара, то при нажатии на кнопку "влево"
    elif current_loc == "street_right":
        # Перемещаемся в блок диалога в главном зале бара
        jump act2_front_pred
    # Иначе локация недопступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_street

    return

# Блок диалога перед интерактивностью или СН в нижней части улицы
label act2_down_pred:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    # Показываем фон верхней части улицы
    scene bg street_down with dissolve

    "Вы находитесь в нижней части улицы"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_down==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_down = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_down

    return

# Блок интерактивности в нижней части улицы
label act2_down:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "street_down"

    # Показываем фон левой части улицы
    scene bg street_down with dissolve

    # # После того как подсказка закрыта, показываем меню выбора, если мы еще не включали интерактивный экран
    # if interactive_mode_ended_down == 0:
    #     menu:
    #         "Осмотреться":

    #             # Закрываем диалоговое окно
    #             window hide

    #             # Показываем фон главного зала в баре, если он не был показан ранее
    #             if not persistent.background_shown:
    #                 show bg street_down with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True

    #             # Запускаем интерактивный экран
    #             show screen streetDown with dissolve

    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"

    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_down = 1

    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons_street

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    #     while not closed:
    #         # Закрываем диалоговое окно
    #         window hide
    #         # Показываем фон главного зала в баре, если он не был показан ранее
    #         if not persistent.background_shown:
    #             show bg street_down with dissolve
    #             # Меняем глобальную переменную на True, так как фон был показан
    #             $ persistent.background_shown = True

    #         # Запускаем интерактивный экран
    #         show screen streetDown with dissolve

    #         # Включаем интерактивное взаимодействие
    #         $ result = ui.interact()

    #     # Если цикл прервался, то мы нажали на кнопку, значит, можно поместить на экран кнопки навигации
    #     jump showbuttons_street

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg street_down with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen streetDown with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide streetDown

    jump showbuttons_street

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_street_down:
    # Убираем экран с кнопками
    hide screen movebuttons_street

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "street_up":
        # Перемещаемся в блок диалога в главном зале бара
        jump act2_front_pred

    elif current_loc == "street_front":
        jump act2_down_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_street

    return

label act2_bag:
    hide screen streetFront
    scene bg street_bag with dissolve
    "Призрак нашел сумку и телефон"
    # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ

label act2_bag_interact:
    show screen bagInteract with dissolve
    # Включаем интерактивное взаимодействие (пока не нажмем на дверь, не попадем внутрь бара)
    $ result = ui.interact()

label act2_gallery:
    # Логические переменные для отслеживания того, впервые мы появляемся в блоке локации или нет
    # Если впервые, то запускается диалог (КУДА НУЖНО ВСТАВИТЬ РЕПЛИКИ), иначе ничего не происходит
    $ count_pred_interact = 0
    $ count_pred_up = 0
    $ count_pred_right = 0
    $ count_pred_left = 0

    # Обнуляем нажатие на подсказку
    $ info_panel_closed_2 = False

    stop music1 fadeout 2

    play music gallery1 fadein 2

    scene bg gallery_entrance with dissolve

    "Вы находитесь у входа в картинную галерею"

    scene bg gallery_up with dissolve

    stop music fadeout 2

    play music1 "music/classic_music.mp3" fadein 2

    # ВСТАВИТЬ РЕПЛИКИ ПРО СКУЧНУЮ КАРТИНУ

    "Тут идут реплики"

    menu:
        "Поделиться о себе информацией":
            $ renpy.notify("Вы улучшили отношения с призраком")
        "Поделиться, но сухо":
            $ renpy.notify("Ваши отношения с призраком не улучшились")

    "Погружение в мысли"

    # ВСТАВИТЬ РЕПЛИКИ

    jump act2_flashback_start

    return

label act2_flashback_start:
    stop music1 fadeout 2

    play music gallery1

    scene bg flashback_lesson with dissolve

    "Урок математики"

    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback_hall with dissolve

    "Гг возвращается домой"

    scene bg flashback_mom_room with dissolve

    "Происходит серьезный разговор матери с гг"

    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback_room with dissolve

    "Комната гг"

    jump act2_flashback_interact_room

    return

label act2_flashback_interact_room:
    # Прячем диалоговое окно
    window hide

    # Показываем фон комнаты, если он не был показан ранее
    if not persistent.background_shown:
        show bg flashback_room with dissolve
        # Меняем глобальную переменную на True, так как фон был показан
        $ persistent.background_shown = True

    # Запускаем интерактивный экран с плавным эффектом
    show screen roomScreen with dissolve

    # Включаем интерактивное взаимодействие
    $ result = ui.interact()
    
    return

label act2_flashback_graffity:
    scene bg flashback_padik with dissolve

    "Подъезд, у которого встречается компания"

    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback_play with dissolve

    "Ребята идут на детскую площадку"

    # ВСТАВИТЬ РЕПЛИКИ

    jump act2_flashback_policy
    
    return

label act2_flashback_policy:

    scene bg flashback_policy1 with dissolve
    "Гг привезли в участок полиции"
    # ВСТАВИТЬ РЕПЛИКИ

    scene bg flashback_policy with dissolve
    "Гг ставят на учет"
    # ВСТАВИТЬ РЕПЛИКИ

    jump act2_flashback_home
    
    return

label act2_flashback_home:
    scene bg flashback_kitchen with dissolve
    "Мама жестко отчитывает гг"
    # ВСТАВИТЬ РЕПЛИКИ
    "Конец флешбека"
    jump act2_present
    return


label act2_present:
    stop music fadeout 2

    play music1 "music/classic_music.mp3" fadein 2

    scene bg gallery_front with dissolve

    jump act2_front_pred_gallery

    return


label act2_front_pred_gallery:
    scene bg gallery_front with dissolve

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    "Вы находитесь в холле картинной галереи"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_interact==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_interact = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_front_gallery

    return

label act2_front_gallery:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    scene bg gallery_front with dissolve

    show screen info_panel_2

    # Показываем подсказку относительно перемещения по локациям, если она ещё не была закрыта
    if not info_panel_closed_2:
        show screen info_panel_2

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "gallery_front"

    # Цикл для ожидания закрытия подсказки
    while not info_panel_closed_2:
        # Ждем, пока подсказка не будет закрыта
        $ renpy.pause(0.1)  

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg gallery_front with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen galleryFront with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide galleryFront

    jump showbuttons_gallery

    return

label act2_up_pred_gallery:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg gallery_up with dissolve

    "Вы находитесь в центре картинной галереи"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_up==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_up = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_up_gallery

    return

label act2_up_gallery:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    scene bg gallery_up with dissolve

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "gallery_up"

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg gallery_up with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen galleryUp with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide galleryUp

    jump showbuttons_gallery

    return

label move_gallery_up:
    # Убираем экран с кнопками
    hide screen movebuttons_gallery

    # Если текущая позиция - центр улицы, то при нажатии на кнопку "вверх"
    if current_loc == "gallery_front":
        # Перемещаемся в блок диалога в верхней части улицы
        jump act2_up_pred_gallery
    # Иначе локация недоступна
    elif current_loc == "gallery_down":
        jump act2_front_pred_gallery
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_gallery

    return

label act2_right_pred_gallery:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg gallery_right with dissolve

    "Вы находитесь в правой части картинной галереи"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_right==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_right = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_right_gallery

    return

label act2_right_gallery:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    scene bg gallery_right with dissolve

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "gallery_right"

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg gallery_right with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen galleryRight with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide galleryRight

    jump showbuttons_gallery

    return


label move_gallery_right:
    # Убираем экран с кнопками
    hide screen movebuttons_gallery

    # Если текущая позиция - главный зал бара, то при нажатии на кнопку "вправо"
    if current_loc == "gallery_front":
        # Перемещаемся в блок диалога в части бара
        jump act2_right_pred_gallery
    # Иначе если текущая позиция - левая часть бара, то при нажатии на кнопку "вправо"
    elif current_loc == "gallery_left":
        # Перемещаемся в блок диалога в главном зале бара
        jump act2_front_pred_gallery
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_gallery

    return


label act2_left_pred_gallery:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg gallery_left with dissolve

    "Вы находитесь в левой части картинной галереи"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_left==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_left = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_left_gallery

    return

label act2_left_gallery:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    scene bg gallery_left with dissolve

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "gallery_left"

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg gallery_left with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen galleryLeft with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide galleryLeft

    jump showbuttons_gallery

    return

label move_gallery_left:
    # Убираем экран с кнопками
    hide screen movebuttons_gallery

    # Если текущая позиция - главный зал бара, то при нажатии на кнопку "влево"
    if current_loc == "gallery_front":
        # Перемещаемся в блок диалога в левой части бара
        jump act2_left_pred_gallery
    # Иначе если текущая позиция - правая часть бара, то при нажатии на кнопку "влево"
    elif current_loc == "gallery_right":
        # Перемещаемся в блок диалога в главном зале бара
        jump act2_front_pred_gallery
    # Иначе локация недопступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_gallery

    return

label act2_down_pred_gallery:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg gallery_down with dissolve

    "Вы находитесь в нижней части картинной галереи"

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_down==0:
        "Здесь будет длинный диалог"

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_down = 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act2_down_gallery

    return

label act2_down_gallery:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    scene bg gallery_down with dissolve

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "gallery_down"

    # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg gallery_down with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen galleryDown with dissolve

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()

    hide galleryDown

    jump showbuttons_gallery

    return

label move_gallery_down:
    # Убираем экран с кнопками
    hide screen movebuttons_gallery

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "gallery_up":
        # Перемещаемся в блок диалога в главном зале бара
        jump act2_front_pred_gallery

    elif current_loc == "gallery_front":
        menu:
            "Внимание! Если вы подтвердите выбор, то покинете локацию!"
            "Покинуть картинную галерею":
                jump act2_street
            "Еще рано":
                jump act2_front_pred_gallery
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons_gallery

    return

label act2_street:
    stop music1 fadeout 2
    play music gallery1 fadein 2
    scene bg gallery_down with dissolve
    "Вы вышли на улицу"
    menu:
        "ВАЖНОЕ РЕШЕНИЕ"
        "Возможно, когда-нибудь я попробую снова заняться рисованием":
            jump act3_start
        "Это было простым детским увлечением":
            jump act3_start
    return
