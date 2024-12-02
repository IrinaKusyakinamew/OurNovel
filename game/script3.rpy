label act3_start:
    # # Обнуляем нажатие на подсказку
    # $ info_panel_closed_3 = False

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

    jump act3_continue

label act3_continue:

    scene bg univer_front with dissolve

    $ renpy.pause(1.0)

    scene bg univer_side with dissolve
    show ghost normal with dissolve
    gh "Это место выглядит знакомо."
    gg "Отлично, пойдем внутрь."

    jump act3_hall_pred

    return

# Блок диалога перед интерактивностью или СН в холле вуза
label act3_hall_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg hall with dissolve


    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_hall_interact==0:
        if important1:
            gg "Здесь так красиво, ощущается творческая атмосфера. Я бы хотел здесь учиться."
        else:
            gg "Здесь ощущается простор, интересная атмосфера."

        show ghost normal with dissolve
        gh "Да, мне тоже нравится. Пойдем посмотрим на холл со 2 этажа."


        # Меняем значение переменной
        $ count_hall_interact = 1


        jump act3_ladder_pred

    # show screen info_panel

    # # Показываем подсказку относительно перемещения по локациям, если она ещё не была закрыта
    # if not info_panel_closed_3:
    #     show screen info_panel_3

    # # Цикл для ожидания закрытия подсказки
    # while not info_panel_closed_3:
    #     # Ждем, пока подсказка не будет закрыта
    #     $ renpy.pause(0.1)

    # # Перемещаемся в блок интерактивности в главном зале бара 
    # jump act3_hall

    # return

# Блок интерактивности в холле вуза
label act3_hall:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "hall"

    scene bg hall with dissolve


    # # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    # while not closed:
    #     # Закрываем диалоговое окно
    #     window hide
    #     # Показываем фон главного зала в баре, если он не был показан ранее
    #     if not persistent.background_shown:
    #         show bg hall with dissolve
    #         # Меняем глобальную переменную на True, так как фон был показан
    #         $ persistent.background_shown = True

    #     # Запускаем интерактивный экран
    #     show screen unikHall with dissolve

    #     # Включаем интерактивное взаимодействие
    #     $ result = ui.interact()

    # hide unikHall

    jump showbuttons_unik

    return



# Блок диалога перед интерактивностью или СН в кордиоре с кабинетами
label act3_classes_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg classes with dissolve


    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_classes_interact==0:
        
        gg "Хм, может стоит зайти в кабинет?"

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

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_canteen_interact==0:
        show bg canteen with pixellate
        show f2 normal with dissolve
        f2 "Не расстраивайся! Главное, не прекращать попытки и тогда…"
        "???" "…!"
        show f2 upset
        f2 "Прости…{w} Я забыл, что все намного сложнее. Я тоже считаю, что Николай Петрович поступил неправильно."
        "???" "…"
        f2 "Может, все-таки поешь?"
        hide f2 with dissolve

        $ count_canteen_interact = 1

        if count_canteen_interact == 1 and dean_door_click > 0:
            gg "Получается, ты рисовала в стиле импрессионизма и какой-то преподаватель хотел поддержать твое стремление и взять работу на конкурс."
            gh "Да, но кто-то {b}{color=#5f2626}попросил{/color}{/b} пресечь это…"
            gg "Мда, зреет что-то нехорошее"
            gh "И не говори"

        $ friendshp_gh_temp += 1

    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_canteen

    return

# Блок интерактивности в холле вуза
label act3_canteen:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "canteen"

    scene bg canteen with dissolve

    # # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    # while not closed:
    #     # Закрываем диалоговое окно
    #     window hide
    #     # Показываем фон главного зала в баре, если он не был показан ранее
    #     if not persistent.background_shown:
    #         show bg canteen with dissolve
    #         # Меняем глобальную переменную на True, так как фон был показан
    #         $ persistent.background_shown = True

    #     # Запускаем интерактивный экран
    #     show screen unikCanteen with dissolve

    #     # Включаем интерактивное взаимодействие
    #     $ result = ui.interact()

    # hide unikCanteen

    jump showbuttons_unik

    return


# Блок диалога перед интерактивностью или СН на 2 этаже у лестницы
label act3_ladder_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg ladder with dissolve


    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_ladder_interact==0:

        $ count_ladder_interact = 1
        
        $ renpy.pause(1.0)
        jump act3_frescoes_pred


    # Перемещаемся в блок интерактивности в главном зале бара 
    jump act3_ladder

    return

# Блок интерактивности в холле вуза
label act3_ladder:

    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "ladder"

    scene bg ladder with dissolve

    # # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    # while not closed:
    #     # Закрываем диалоговое окно
    #     window hide
    #     # Показываем фон главного зала в баре, если он не был показан ранее
    #     if not persistent.background_shown:
    #         show bg ladder with dissolve
    #         # Меняем глобальную переменную на True, так как фон был показан
    #         $ persistent.background_shown = True

    #     # Запускаем интерактивный экран
    #     show screen unikLadder with dissolve

    #     # Включаем интерактивное взаимодействие
    #     $ result = ui.interact()

    # hide unikLadder

    jump showbuttons_unik

    return


# Блок диалога перед интерактивностью или СН в лекционной аудитории
label act3_lecture_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg lecture with dissolve

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_lecture_interact==0:
        show bg lecture with pixellate
        show f1 with dissolve
        f1 "Слушай, у тебя есть конспекты прошлой лекции?"
        "???" "…"
        f1 "Можно сфоткать?...{w} Блин, я не понимаю твой почерк."
        "???" "…"
        f1 "Хаха, именно так."
        hide f1 with dissolve

        gg "Хе-хе"
        gh "Что?"
        gg "Непонятный почерк? Знакомо, я, например даже сам[verb_end] свой прочитать не могу"
        gh "Хах, забавно"

        $ friendshp_gh_temp += 1

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

    # # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    # while not closed:
    #     # Закрываем диалоговое окно
    #     window hide
    #     # Показываем фон главного зала в баре, если он не был показан ранее
    #     if not persistent.background_shown:
    #         show bg lecture with dissolve
    #         # Меняем глобальную переменную на True, так как фон был показан
    #         $ persistent.background_shown = True

    #     # Запускаем интерактивный экран
    #     show screen unikLecture with dissolve

    #     # Включаем интерактивное взаимодействие
    #     $ result = ui.interact()

    hide unikLecture

    jump showbuttons_unik

    return


# Блок диалога перед интерактивностью или СН в коридоре с фресками
label act3_frescoes_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg frescoes with dissolve

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_frescoes_interact==0:
        
        show ghost happy with dissolve
        gh "Посмотри на эти фрески, они прекрасны."
        hide ghost with dissolve

        show bg frescoes with pixellate
        show f1 at left2 with dissolve
        gh "!!!"
        f1 "Какие же неудобные скамейки в этой аудитории!"
        show f2 normal at right2 with dissolve
        f2 "И не говори…{w} Мне кажется, что моя 5 точка превратилась в квадрат."
        f1 "А у нас сейчас еще пара по искусствоведению. Ты идешь?"
        "???" "…"
        f2 "Ну кто бы сомневался, ты ведь почти никогда не пропускаешь пары."
        "???" "…"
        hide f1 with dissolve
        hide f2 with dissolve

        gg "Что это было?..."
        show ghost surprised
        gh "Я знаю этих людей. Я училась с ними.{w} Кажется, мы увидели сцену из прошлого."
        gg "Все чудесатее и чудесатее… Получается, это было видение, где они говорили с тобой? Видимо нам стоит еще походить по универу, есть шанс, что мы сможем найти здесь что-то."
        gh normal "Ты прав[verb_end]."

        $ note_fantoms1 = True
        $ renpy.notify("В заметках появилась новая запись")

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

    # # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    # while not closed:
    #     # Закрываем диалоговое окно
    #     window hide
    #     # Показываем фон главного зала в баре, если он не был показан ранее
    #     if not persistent.background_shown:
    #         show bg frescoes with dissolve
    #         # Меняем глобальную переменную на True, так как фон был показан
    #         $ persistent.background_shown = True

    #     # Запускаем интерактивный экран
    #     show screen unikFrescoes with dissolve

    #     # Включаем интерактивное взаимодействие
    #     $ result = ui.interact()

    # hide unikFrescoes

    jump showbuttons_unik

    return


# Блок диалога перед интерактивностью или СН перед деканатом
label act3_dean_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg dean with dissolve

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_dean_interact==0:

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

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_awards_interact==0:
        gg "Как много призов и грамот."
        gh "И большая часть принадлежит Наоми."
        gg "Я погляжу, она прямо звезда."
        gh "За всем этим стоит огромный труд."
        gg "Не спорю. Пойдем дальше?"

        $ friendshp_gh_temp += 1

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

    # # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся
    # while not closed:
    #     # Закрываем диалоговое окно
    #     window hide
    #     # Показываем фон главного зала в баре, если он не был показан ранее
    #     if not persistent.background_shown:
    #         show bg awards with dissolve
    #         # Меняем глобальную переменную на True, так как фон был показан
    #         $ persistent.background_shown = True

    #     # Запускаем интерактивный экран
    #     show screen unikAwards with dissolve

    #     # Включаем интерактивное взаимодействие
    #     $ result = ui.interact()

    # hide unikAwards

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
    $ note_fantoms2 = True
    $ renpy.notify("В заметках появилась новая запись")

    "{i}{color=#626262}Я невольно сравниваю эти коридоры и аудитории с тем, что, казалось, уже забыто…{/color} {/i}"

    scene bg flashback2_awakening with pixellate
    #звук выливания воды из ведра
    show dad with dissolve
    dad "Вставай, бестолочь!"
    gg "Ты че творишь?!"
    dad "Что-что? Бужу тебя, дубина.{w} Твои пьянки не являются причиной для пропусков пар. Собирайся."
    hide dad with dissolve

    scene bg flashback2_room with dissolve
    gg "Как же болит голова… Я не хочу никуда идти, но лежать в мокрой кровати плохой вариант."
    
    scene bg flashback2_bathroom with dissolve
    gg ```
    И почему все так? До того, как он попал в тюрьму, он был совсем другим человеком. Как бы сложилась наша жизнь, если бы не та ошибка 5 лет назад? Если бы он не доверял своему партнеру по бизнесу, который в итоге его подставил? 
    
    Мать, заядлая домохозяйка, вероятно, не угробила бы свое здоровье, в попытках заработать себе и мне на жизнь. Сколько у нее одновременно было подработок? 3?
    
    От меня бы не отвернулись школьные друзья, родители которых просили не общаться с «тем самым ребенком, у которого отец уголовник».
    
    Кстати[past_end] бы я по учебе? Дружил[verb_end] бы с «не самой хорошей компанией?» Впрочем, какая разница какими их считают? Они единственные все еще общаются со мной и зовут куда-то.
    
    Сейчас этот человек совсем не похож на того самого любимого папу… Мать регулярно терпит от него побои, а он только и делает, что лежит на диване и бухает. Эх, лучше бы он остался в тюрьме до конца своих дней.
    
    Пора одеваться и идти в шарагу.
    ```

    scene bg flashback2_street with dissolve
    gg ```
    Никогда не перестану задавать себе вопрос: «Зачем я вообще туда хожу?». Я поступил[verb_end] в медицинский колледж только из-за матери. 
    
    Она считает, что хоть какое-нибудь образование, помимо школы обязано быть у человека, не хочет чтобы я повторял[verb_end] ее ошибки. 
    
    Но нужно ли мне это все…
    ```

    scene bg flashback2_med with dissolve
    $ renpy.pause(0.7)

    scene bg flashback2_hall with dissolve
    $ renpy.pause(0.5)

    scene bg flashback2_coridor with dissolve
    $ renpy.pause(0.7)

    scene bg flashback2_anatomy with dissolve
    "{i}{color=#626262}До пары еще есть немного времени. Посмотрю шортсы.{/color} {/i}"

    par "Привет."
    show expression par_normal with dissolve
    gg "Привет?"
    par "Я переве[past_end1] сюда пару дней назад и почти никого тут не знаю. Не против, если я сяду рядом?"
    gg "Садись."
    par "Я [partnerName]."
    gg "Я [playerName]."
    par "Приятно познакомиться."
    hide par_normal with dissolve
    gg "И мне. {i}{color=#626262}Все это так странно...{/color} {/i}"

    show bg flashback2_anatomy with fade
    "После пары"
    show expression par_normal with dissolve
    par "Слушай, а где тут можно недорого перекусить?"
    gg "Пойдем, тут недалеко есть хорошее кафе."
    par "Отлично, пошли."

    scene bg flashback2_summer_day2 with fade
    "Спустя пару дней"
    nvl clear
    gg_nvl "{image=images/phone_icons/mem.jpg}"
    par1_nvl "Ахахаха, люблю каламбуры"
    gg_nvl "Ты пойдешь завтра на пары?"
    par1_nvl "Да, а ты?"
    gg_nvl "Тоже"

    "{i}{color=#626262}Блин, с [needPronoun1] как интересно общаться, я хочу чтобы так было всегда{/color} {/i}"

    scene bg flashback2_room with fade
    "Через пару недель"
    nvl clear
    par1_nvl "[playerName], ты сделал[verb_end] таблицу по гистологии?"
    gg_nvl "Да"
    gg_nvl "Щас скину"
    par1_nvl "Кстати, как у тебя успехи с закрытием долгов?"
    gg_nvl "С анатомией разобра[past_end]. Осталась химия и психология"
    par1_nvl "Молодец!!! Если нужна будет помощь, пиши"
    gg_nvl "Конечно"

    "{i}{color=#626262}С [needPronoun1] колледж уже не кажется таким отвратительным местом. Он[verb_end] стимулирует меня ходить на пары, помогает с закрытием хвостов. Может, все не так плохо?{/color} {/i}"

    scene bg flashback2_winter_day2 with fade
    "Прошел примерно месяц"
    nvl clear
    par2_nvl "[playerName], хочешь встретиться сегодня?"
    gg_nvl "Хочу, куда пойдем?"
    par2_nvl "Секрет"
    par2_nvl "Во сколько ты освободишься?"
    gg_nvl "Часам к 6"
    par2_nvl "Хорошо, я заеду за тобой"
    "{i}{color=#626262}Хм, как неожиданно. Интересно, что [partnerName] придумал[verb_end1]?{/color} {/i}"

    scene bg flashback2_winter_day1 with fade
    "Этим же вечером"
    gg "Каток, вау! Я давно хотел[verb_end] сюда сходить!"
    show expression par_winks with dissolve
    par "Я помню, именно поэтому мы здесь."
    gg "Ты лучше всех, спасибо!"
    hide par_winks with dissolve

    show bg flashback2_winter_day1 with fade
    gg "Отлично покатались."
    show expression par_winks with dissolve
    par "Пойдем, это еще не все."
    gg "Ого, веди."

    scene bg bar_right with dissolve #НУЖЕН ФОН РЕСТОРАНА
    show expression par_winks with dissolve
    par "Заказывай, что хочешь."
    gg "Хорошо."
    "{i}{color=#626262}Он[verb_end1] привел[verb_end1] меня в недешевое место. Даже не знаю, что взять, чтобы не напрягать [friendPronoun1]{/color} {/i}"
    "Официант" "Здравствуйте, вы готовы сделать заказ?"
    gg "Я буду карбонару и чашку эрл грея."
    par "Мне тоже самое."

    show expression par_normal
    par "[playerName]"
    gg "М?"
    par "Держи, это тебе."
    gg "О, спасибо. А что это?"
    par "Всего лишь небольшой подарок в честь месяца отношений."
    "{i}{color=#626262}Блин, сегодня праздник… Я и не думал[verb_end], что для н[friendPronoun1] эта дата важна{/color} {/i}"
    par "Я понимаю, месяц - это довольно мало, но разве нам бы не помешало почаще находить поводы для маленьких праздников?"
    gg "Ты так постара[past_end1], устроил[verb_end1] все это. Мне неловко, что я ничего не сделал[verb_end] в ответ…"
    show expression par_winks
    hide par_normal
    par "Не переживай, мне главное видеть, как ты радуешься."
    gg "Ты самый замечательный человек."
    "{i}{color=#626262}Надо будет обязательно подарить что-то хорошее в ответ{/color} {/i}"
    "Остаток вечера прошел прекрасно."

    scene bg flashback2_room with fade
    nvl clear
    fr_nvl "Хей, от тебя давно не было вестей, мб хочешь встретиться, выпить?"
    "{i}{color=#626262}Не буду отвечать...{/color} {/i}"

    scene bg flashback2_winter_day2 with fade
    "Через пару недель"
    "{i}{color=#626262}На носу уже новый год. Как быстро летт время. Я очень рад[verb_end], что в моей жизни появи[past_end1] [partnerName].{/color} {/i}"
    nvl clear
    par2_nvl "[playerName], помнишь про новогоднюю вечеринку у меня дома, ты же придешь?"
    gg_nvl "Еще спрашиваещь? Конечно!"
    par2_nvl "Ты будешь самым желанным гостем"

    scene bg flashback2_winter_night2 with fade
    "День X"
    "{i}{color=#626262}Уф, я на месте.{/color} {/i}"


    scene bg flashback2_partner_home with dissolve
    "{i}{color=#626262}Как много людей... Я тут почти никого не знаю.{w} Так волнуюсь, не сказануть бы чего-то не то.{/color} {/i}"
    "{i}{color=#626262}Надо найти [friendPronoun1].{/color} {/i}"

    show bg flashback2_partner_home with fade
    "Разгар праздника"
    show expression par_winks with dissolve
    par ```
    Прошу всех, внимание!

    Я хочу сказать небольшой тост. Тут собралось довольно много народу, даже немного волнительно.

    Сегодня мы собрались здесь, чтобы отметить замечательный праздник. И я хочу поднять бокал за тебя, [playerName]. 

    Ты делаешь мою жизнь ярче и интереснее. Рядом с тобой я чувствую себя самым счастливым человеком на свете, потому что… нет, пожалуй перейду сразу к делу.
    ```
    show expression par_grin
    par "Я хочу признаться тебе в одной вещи.{w} Всё это время я встреча[past_end1] с тобой на спор. Я поспорил[verb_end1] с друзьями на деньги, что смогу завоевать твоё сердце." 
    "{i}{color=#626262}Что…{/color} {/i}"
    par "Это был вызов, который я принял[verb_end1], и я его выполнил[verb_end1]. А ты просто оказалась лёгкой добычей."
    "{i}{color=#626262}Нет…{/color} {/i}"
    par "Мне не жаль, что я поступил[verb_end1] так. Я хотел[verb_end1] доказать себе и другим, что могу добиться любой цели. И я доказал[verb_end1]. Не вижу смысла сожалеть о своих действиях." 
    "{i}{color=#626262}Как… Почему?{/color} {/i}"
    par "Давайте же выпьем, друзья! За мою победу!"

    gg "{sc=1}[partnerName], скажи, что это неправда!{/sc}"
    par "Увы…"
    gg "{sc=1}Ты не мог[past_verb_end1] так со мной поступить!{/sc}"
    par "Мог[past_verb_end1] и поступил[verb_end1]."
    "{sc=1}{i}{color=#626262}Нет…{w} Не может быть, это все просто дурной сон{/color} {/i}{/sc}"

    scene bg flashback2_partner_home with dissolve
    "{sc=2}{i}{color=#626262}Это просто кошмар, это не может быть правдой!{/color} {/i}{/sc}"
    #всхлипы перед плачем
    "{i}{color=#626262}[partnerName] даже не смотрит в мою сторону{/color} {/i}"
    "{sc=2}{i}{color=#626262}Я хочу убраться отсюда{/color} {/i}{/sc}"

    show bg flashback2_winter_night2 with wipeleft
    $ renpy.pause(1)
    if gender_symbol == "♂":
        scene flashback2b with fade
        $ persistent.flashback2b = True
    else:
        scene flashback2g with fade
        $ persistent.flashback2g = True

    pause
    gg "Почему, как только я начинаю верить во что-то хорошее, меня спускают с небес на землю? Почему…"
    fr "Эй, что случилось? Ты сначала несколько месяцев не выходил[verb_end] на связь, а теперь я застаю тебя в таком состоянии в новогоднюю ночь!"
    gg "Да… Много всего случилось, не хочу сейчас об этом"
    fr "Хорошо, давай просто выпьем, с праздником, дружище"

    scene bg hall2 with fade
    gg ```
    Вскоре после этих событий я отчисли[past_end] из колледжа

    Я не мог[past_verb_end] больше видеть {b}{color=#5f2626}это лицо{/color}{/b}

    Да и какой смысл был оставаться? Учеба? Смешно

    После этого родители, видимо, возненавидели меня. Они выгнали меня из квартиры и сказали катиться на все 4 стороны.

    [friendName] в очередной раз выручил[verb_end] меня, подкинув работу на первое время. Конечно, мне не очень нравился род деятельности, но разве у меня был выбор?
    ```
    jump act3_present

    return

label act3_present:
    scene bg classes with pixellate
    show ghost uncomprehending with dissolve
    gh "Эй, [playerName], прием! Ты опять погряз[past_verb_end] в мыслях?"
    gg "Ммм… Да."
    gh" Ты что плачешь?"
    gg "Нет!"
    "по щеке течет слеза"
    gg "Или да…"
    gh "Что вызвало в тебе эти чувства?"
    
    if friendshp_gh >= 7:
        gg "Я резко вспомнил[verb_end] о том, о чем не хотелось бы вспоминать"
        "[playerName] вкратце рассказывает о своих печалях"
        gh surprised "Боже, это просто кошмар. Я не могу представить, какую сильную боль ты пережил[verb_end]! [partnerName] поступил[verb_end1] просто отвратительно!"
        gg "С этих событий прошло 2 года. В моей жизни мало что поменялось за это время."
        gh "Получается, ты продолжаешь «помогать» с бизнесом своему другу?"
        gg "Да"
        gh "Тебя и правда это устраивает?"

        menu:
            "Что ответить?"
            "Не устраивает":
                $ important2 = True
                $ renpy.notify("Вы приняли важное решение.")
                gg "Нет… Я оказа[past_end] в чертовом замкнутом круге: из-за этих подработок у меня появились проблемы с законом."
                gg "А из-за проблем с законом меня не хотят брать даже бариста. И в итоге я вынужден[verb_end] снова брать «подработки»…"
                gh normal "Я понимаю, с тобой много раз поступали ужасно, но не все люди такие как [partnerName]."
                gh "[friendName] может и помогает тебе, но, мне кажется, тебе это только вредит."
                gh "Возможно, от незнакомки вроде меня этот совет прозвучит странно, но… ты молод[verb_end], у тебя вся жизнь впереди. Тебе стоит завязать с этими подработками. Все в жизни поправимо, пока ты жив."
                gg "Мне были нужны эти слова, спасибо. Я обязательно подумаю обо всем этом. Но для начала нам бы надо выбраться из нашей непростой ситуации."
                gh" Точно, мы же собирались зайти в этот кабинет."
                $ friendshp_gh += 1
                $ renpy.notify("Отношения с персонажем Призрак улучшились")
                gg "Пошли"

                $ note_gang1 = True
                $ renpy.notify("В заметках появилась новая запись.")

            "Устраивает":
                gg "Знаешь, вполне."
                $ friendshp_gh -= 3
                $ renpy.notify("Отношения с персонажем Призрак резко ухудшились.")
                gh upset "Я… Пожалуй не буду это никак комментировать. Пойдем дальше."
                gg "Мы собирались зайти в этот кабинет"
                gh "Угу…"

                $ note_gang2 = True
                $ renpy.notify("В заметках появилась новая запись.")

    else:
        gg "Я не намерен[verb_end] делиться своими переживаниями с той, кого я совсем не знаю."
        $ friendshp_gh -= 1
        $ renpy.notify("Отношения с персонажем Призрак ухудшились.")
        gh upset "Как грубо… Прости. Я больше не буду лезть к тебе с расспросами. Мы собирались зайти в этот кабинет."
        gg "Пошли."

        $ note_gang3 = True
        $ renpy.notify("В заметках появилась новая запись.")

    scene bg class with pixellate
    show aizek normal with dissolve
    aik "Слушай, мне уже надоело прикрывать тебя перед родителями. Может, пока завязывать с твоим хобби? "
    "???" "..."

    gh "Этот человек… Это мой брат."
    gg "Ох…"

    aik "Ты ходишь одна в темное время суток черт знает где. Ты действительно думаешь, что твой способ самовыражения хорош? Ты уже пол города «разукрасила» своими картинами."
   
    gg "Чего?"
    gh "Так значит…"

    "???" "..."
    show aizek calm
    aik "Нет, послушай! Я не считаю это чем-то плохим, но я переживаю за тебя! И родители тоже. Может, они и избирают немного жесткие методы, но это и правда ради твоего блага…"
    "???" "...!"
    show aizek normal
    aik "Ты собираешься сегодня в то место, о котором говорила?"
    "???" "..."
    aik "Пожалуйста, будь осторожна, Наоми."
    hide aizek with dissolve
    
    gg "Что…?!"
    show ghost surprised with dissolve
    gh "Так, стоп… Мне надо переварить это."
    gg "Не тебе одной…"
    gh normal "Получается… Меня зовут Наоми. Я училась в этом универе и предпочитала рисовать в жанре импрессионизма"
    gg "Но кто-то…"
    gh "Мои родители"
    gg "Но твои родители не хотели этого. Они {b}{color=#5f2626}попросили{/color}{/b}, чтобы твои стремления к этому жанру не поощрялись. Судя по картине в галерее, они хотели чего-то более классического."
    gh "И я в качестве отдушины решила вымещать свои творческие порывы на городе"
    gg "Значит ты тот самый таинственный художник"
    gh "Получается, что так."
    gg "Охренеть…"
    gh upset "Да, по-другому и не скажешь…"
    $ note_Naomi = True
    $ renpy.notify("В заметках появилась новая запись.")
    pause
    
    menu:
        "Что делать?"
        "Поддержать Наоми":
            gg "Я в шоке, не представляю даже как тебе сейчас тяжело… Но смотри сколько мы всего узнали! Это просто невероятно, ты сочетаешь в себе столько разных граней. Я поражен(а)."
            gh happy "Хех, спасибо, приятно слышать."
            $ friendshp_gh += 1
            $ renpy.notify("Отношения с Персонажем Призрак улучшились.")
            gg "Я рад[verb_end], что смог[past_verb_end] познакомиться с тем самым таинственным художником"
            gh "Я тоже рада, что познакомилась с тобой."

        "Поторопить Наоми":
            gg "Я понимаю твою печаль... Но хотелось бы знать, что мы планируем делать дальше."
            gh upset "А... Мне надо немного подумать."

    gh normal "Этот диалог заставил меня вспомнить многое. В частности, я знаю, куда я пошла после разговора. Думаю, нам следует отправиться туда."
    gg "Хорошо, веди."

    jump act3_end
    
label act3_end:
    scene bg classes with wipeleft
    scene bg hall with wipeleft
    # ВСТАВИТЬ РЕПЛИКИ
    jump act4_start
    return

