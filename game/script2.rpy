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
    
    show ghost normal 
    gg "Итак, что будем делать?"
    gh "Полагаю, стоит осмотреть этот двор. Именно здесь начинаются странности, возможно тут найдутся какие-нибудь зацепки."
    gg "Разумная мысль."
    hide ghost

    jump act2_front_pred

    return

# Блок диалога перед интерактивностью или СН в центральной части улицы
label act2_front_pred:
    $ count_act2_front_pred += 1

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg bar_down_ghost with dissolve

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_interact==0:

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

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_up==0:
        "Пусто..."

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

    jump showbuttons_street

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вверх"
label move_street_up:

    # Убираем экран с кнопками
    hide screen movebuttons_street

    # Если текущая позиция - центр улицы, то при нажатии на кнопку "вверх"
    if current_loc == "street_front":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в верхней части улицы
        jump act2_up_pred
    # Иначе локация недоступна
    elif current_loc == "street_down":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        jump act2_front_pred

    return

# Блок диалога перед интерактивностью или СН в правой части улицы    
label act2_right_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    # Показываем фон верхней части улицы
    scene bg street_right with dissolve

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_right==0:

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
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в центре улицы
        jump act2_right_pred
    # Иначе если текущая позиция - левая часть улицы, то при нажатии на кнопку "вправо"
    elif current_loc == "street_left":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в центр улицы
        jump act2_front_pred

    return


# Блок диалога перед интерактивностью или СН в левой части улицы
label act2_left_pred:

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    # Показываем фон верхней части улицы
    scene bg street_left with dissolve

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_left==0:

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
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в левой части бара
        jump act2_left_pred
    # Иначе если текущая позиция - правая часть бара, то при нажатии на кнопку "влево"
    elif current_loc == "street_right":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в главном зале бара
        jump act2_front_pred

    return

# Блок диалога перед интерактивностью или СН в нижней части улицы
label act2_down_pred:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    # Показываем фон верхней части улицы
    scene bg street_down with dissolve

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_down==0:
        "Здесь ничего нет."

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

    jump showbuttons_street

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_street_down:
    # Убираем экран с кнопками
    hide screen movebuttons_street

    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "street_up":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в главном зале бара
        jump act2_front_pred

    elif current_loc == "street_front":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        jump act2_down_pred

    return

label act2_bag:
    hide screen streetFront
    scene bg street_bag with dissolve
    # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ

label act2_bag_interact:
    show screen bagInteract with dissolve
    # Включаем интерактивное взаимодействие
    $ result = ui.interact()

label pre_goout:
    scene bg bar_down with dissolve
    gg "В целом, ничего необычного."
    show ghost normal with dissolve
    gh "Тебе удалось что-нибудь найти?"
    gg "Вообще ничего, никаких подсказок или зацепок."
    $ note_cooperate = True
    $ renpy.notify("В заметках появилась новая запись")
    gh "Это очень странно. Тогда что будем делать дальше?"
    gg "Раз тут тупик, можем попытаться пока выяснить, что произошло с тобой. Есть идеи?"
    gh "Есть одно место, меня туда как будто бы тянет. Но я ходила туда… и ничего."
    gg "В любом случае, других идей у нас нет. Веди."
    gh "Хорошо, это недалеко."

    play sound "sounds/shagi-23 (mp3cut.net).mp3"

label act2_gallery:
    # Логические переменные для отслеживания того, впервые мы появляемся в блоке локации или нет
    # Если впервые, то запускается диалог (КУДА НУЖНО ВСТАВИТЬ РЕПЛИКИ), иначе ничего не происходит
    $ count_pred_interact = 0
    $ count_pred_up = 0
    $ count_pred_right = 0
    $ count_pred_left = 0
    # Нашли картину или нет
    $ found_painting = False

    # Обнуляем нажатие на подсказку
    $ info_panel_closed_2 = False

    scene bg gallery_entrance with dissolve

    $ renpy.pause(0.5)

    scene bg gallery_up with dissolve

    stop sound

    stop music fadeout 2
    play music1 "music/classic_music.mp3" fadein 2

    show ghost normal with dissolve
    gg "Тебя тянет сюда?"
    gh "Да, именно к этой картине."
    gg "Главный экспонат выставки, довольно внушительных размеров. Наверно долго писалась, много маленьких деталей."
    gh uncomprehending "Лица будто бы каменные, ни единой эмоции, четко выверенные пропорции тел."
    gg "Классицизм, чтоб его. Не люблю работы в этом стиле. Им часто не хватает жизни и чувств."
    gh "Да, согласна. Я бы предпочла провести время за просмотром более ярких работ, возможно что-то из импрессионизма."
    gh happy "Особенно мне нравится, как художники этого направления передают эмоции и атмосферу момента."
    gh "Кажется, они словно заставляют нас чувствовать, а не просто смотреть на картину."
    "{i}{color=#626262} Ого, не думал[verb_end], что у нас сойдутся вкусы, первое впечатление иногда обманчиво. {/color} {/i}"
    gg '''
    Да, именно! Мне кажется, это одна из основополагающих идей импрессионизма — запечатлеть мгновение.

    Взять те же картины Моне, его «Впечатление. Восход солнца» — каждый раз, когда я на нее смотрю, ощущаю, как свет меняется.

    И вообще, мне кажется, такой подход к живописи делает каждую работу уникальной.

    
    Каждый зритель может интерпретировать картину по-своему. Я люблю, как различные оттенки и мазки создают атмосферу.
    '''

    gh "Согласна. И эта свобода в технике — это то, что делает импрессионизм таким особенным."
    gh "Художники отказались от жестких правил, начали использовать цвет, чтобы передать свои ощущения от увиденного, а не только реальность."
    gg "Именно! Это отражает не только природу, но и внутренние переживания художника."
    gg "Я особенно впечатлен[verb_end] работами Ренуара. У него такие яркие и теплые цвета, что прямо чувствуешь радость от жизни!"
    gh surprised "Ренуар, да! Его картины всегда такие живые и полные энергии. Особенно «Обед в саду» — в ней такая атмосфера дружеского общения и счастья. Хочется быть частью этого момента."
    gg "Да, это потрясающе! Даже сейчас среди современных художников есть невероятные таланты."
    gg "Слышала о загадочном художнике, недавно появившемся в нашем городе? Он разукрашивает пустые стены города яркими граффити в стиле импрессионизма."
    gh uncomprehending "Не слышала, расскажешь поподробней?"
    gg "Если честно, информации не сильно много. Никто никогда не видел этого художника за работой, у него есть телеграмм канал, там он поддерживает связь со своими подписчиками."
    gg "Он заявил, что главная его цель – преобразить этот серый город. Его работы по истине впечатляют, я обязательно покажу их тебе, когда мы разберемся с нашими проблемами."
    gh "Вообще, я немного удивлена твоей увлеченностью. При первом разговоре ты показа[past_end] мне немного другим человеком."

    menu:
        "Поделиться информацией о себе":
            play sound "sounds/create_character.mp3"
            $ friendshp_gh += 1
            $ renpy.notify(f"Отношения с персонажем Призрак улучшились")

            gg "Я раньше занима[past_end] рисованием, мне очень нравилось. Однако это было давно. Фактически, до новостей о появлении загадочного художника я уже лет 7 как был[verb_end] не в теме."
            $ note_pictures1 = True
            $ renpy.notify("В заметках появилась новая запись")

        "Поделиться, но сухо":
            play sound "sounds/create_character.mp3"
            gg "Когда-то я увлека[past_end] рисованием, но уже давно как забросил[verb_end]."
            $ note_pictures2 = True
            $ renpy.notify("В заметках появилась новая запись")

    "{i}{color=#626262} И правда, как же давно это было.{w} Средняя школа…{/color} {/i}"

    jump act2_flashback_start

    return

label act2_flashback_start:
    stop music1 fadeout 2

    play music gallery1 fadein 2

    scene bg flashback_lesson with pixellate

    $ is_flashback = True

    "Урок математики"
    "[playerName] рисует в тетради"
    #мб сделать фон тетради?

    scene bg school_paint with dissolve
    "{i}{color=#626262}Так, а вот здесь наверно стоит добавить красного.{w} Нет, лучше использовать оранжевый, он лучше передаст то, что я хочу показать. {/color} {/i}"

    scene bg flashback_lesson with dissolve
    show teacher silhouette with dissolve
    play sound "sounds/jenskiy-golos-nevnyatnoe-slovo.mp3"
    tchr "*неразборчиво*"
    hide teacher with dissolve
    scene bg school_paint with dissolve
    "{i}{color=#626262}Хм, а может лучше наоборот сделать акцент вот здесь? Тогда использую эту форму. {/color} {/i}"
    scene bg flashback_lesson with dissolve
    show teacher silhouette with dissolve
    play sound "sounds/jenskiy-golos-nevnyatnoe-slovo.mp3"
    tchr "*неразборчиво!*"
    hide teacher with dissolve
    scene bg school_paint with dissolve
    "{i}{color=#626262}Первый вариант все же был лучше…{/color} {/i}"
    scene bg flashback_lesson with dissolve
    show teacher angry with dissolve
    tchr "Ковалев[verb_end]!{w} Сколько тебя можно звать, ты оглох[past_verb_end]?!"
    gg "Простите.. Я просто задума[past_end]. Что вы спросили?"
    tchr "Ишь ты, что я спросила. [playerName], ты когда за голову возьмешься?!{w} Мало того, что на уроках ничего не слушаешь, так еще и по оценкам скати[past_end]. Завтра же мать в школу."
    gg "Хорошо."
    show teacher normal
    tchr "Продолжаем урок."
    play sound "sounds/call_for_break.mp3"
    hide teacher with dissolve
    play ambient "sounds/noise_at_break.mp3" fadein 2
    "{i}{color=#626262}Тоже мне… Докопалась, карга старая. Так, на чем я останови[past_end]? {/color} {/i}"
    show expression fr_yo_grin with dissolve
    fr "Здорово ты, конечно, ее разозлил[verb_end]. Мне понравилось, молодца."
    gg "А? Спасибо?..."
    fr "Что делаешь? Рисуешь?"
    "*[friendName] заглядывает в тетрадь*"
    "{i}{color=#626262}Блин, что [friendName] пристал[verb_end]? За 6 лет совместной учебы мы ни разу не общались. {/color} {/i}"
    hide fr_yo_grin
    show expression fr_yo_smile
    fr "Ого, очень красиво. Ты ходишь в художку?"
    gg "Нет, но хотелось бы."
    fr "А знаешь где бы хорошо смотрелся твой рисунок?"
    gg "Понятия не имею."
    fr "Мы сегодня компанией планировали пойти рисовать граффити. Нам бы очень пригодился такой умелый художник."
    gg "Ты хочешь, чтобы я присоедини[past_end]?"
    fr "Ну да, а зачем мне еще это тебе говорить. Приходи около 8 вечера к подъезду моего дома."
    "{i}{color=#626262}Неужели меня и правда куда-то зовут?{w} Я думал[verb_end], что в этой школе уже никто со мной не заговорит. Это мой шанс найти друзей, стоит попытаться. {/color} {/i}"
    gg "Я приду."
    fr "Отлично! Буду ждать тебя."
    hide fr_yo_smile with dissolve
    "{i}{color=#626262}Осталось отсидеть 1 урок. Надеюсь, мама отпустит меня вечером погулять{/color} {/i}"
    stop ambient

    play sound "sounds/shagi-23.mp3"

    scene bg flashback_hall with dissolve
    $ renpy.pause(0.5)

    scene bg flashback_mom_room with dissolve
    
    gg "Мам, я дома."
    show mom angry
    stop sound
    mom "Мне звонила классная руководительница."
    "{i}{color=#626262}Ой-ей{/color} {/i}"
    mom "Она сказала, что ты опять рисовал[verb_end] вместо того, чтобы заниматься. Сколько уже можно?! Ты обязан[verb_end] хорошо учиться." 
    mom "У нас нет денег нанимать тебе кучу репетиторов, сегодня остаешься без компьютера. Чтобы весь вечер посвятил[verb_end] математике!"
    "{i}{color=#626262}Мда, вот тебе и прогулка…{/color} {/i}"
    gg "Я пойду к себе в комнату…"


    scene bg flashback_room with dissolve

    "{i}{color=#626262}Я не могу упустить этот шанс, меня впервые позвали куда-то. Я хочу завести себе друзей! Нужно дождаться, когда мама уйдет на вечернюю подработку{/color} {/i}"

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

label button_wait:
    "Нужно подождать, пока мама уйдет."
    jump act2_flashback_interact_room


label act2_flashback_graffity:
    show bg flashback_room with dissolve
    gg "Она наконец ушла. Нужно поторопиться, я не хочу опаздывать."

    stop music fadeout 2
    play music1 "music/Dreaming.mp3" fadein 2

    scene bg flashback_padik with dissolve

    show expression fr_yo_normal with dissolve
    fr "Я же говорил[verb_end], что он[verb_end] придет! Ты вовремя, мы уже уходить собирались"
    gg "Простите, мама оставила дома сидеть над матешей, пришлось ждать, пока она уйдет"
    show expression fr_yo_normal at right with moveinright
    play sound "sounds/zvuk-tolpa-smeetsya-3-24183.mp3"
    show gang at left with dissolve
    gang "Ууу, а говорили, что ты паинька, художник"
    "{i}{color=#626262}Какие-то они…{w} Странные, ладно, посмотрим, что будет дальше{/color} {/i}"
    stop sound
    gg "Хе-хе, не всегда"
    hide fr_yo_normal
    show expression fr_yo_grin at right
    fr "Пойдемте уже, пока совсем не стемнело. У нас еще куча дел"

    scene bg flashback_play with dissolve

    gg "Детская площадка? Я думал[verb_end] мы найдем какую-нибудь пустующую скучную стену"
    show gang with dissolve
    gang "А эта площадка тоже скучная, ей не помешало бы добавить красок"
    "{i}{color=#626262}Но… Это же вандализм! Что же мне делать? {/color} {/i}"
    play ambient "sounds/a3af11d3a0fb6b0.mp3"
    gang``` 
    Давай, художник. Бери баллончик, не стесняйся!

    Если тебе что-то не нравится, конечно, можешь уйти, мы насильно тебя не держим

    ```
    stop ambient
    play sound "sounds/zvuk-tolpa-smeetsya-3-24183.mp3"

    gang "Да, ну. А в начале крутышкой показа[past_end]"

    gang "Пфф, струсил[verb_end] чтоль?"

    "{i}{color=#626262}Черт… Я не могу сейчас повернуть назад{/color} {/i}"
    gg "Ладно"
    stop sound
    hide gang
    play sound "sounds/hold_spray.mp3"
    "*[playerName] берет баллончик*"
    show expression fr_yo_grin with dissolve
    fr "Маску не забудь, а то травануться можешь"
    hide fr_yo_grin with dissolve
    play sound "sounds/face-mask-ear-loop-put-on-surgeon-surgery.mp3"
    "*[playerName] надевает маску, взбалтывает баллончик и начинает рисовать*" #надо звуков добавить
    play sound "sounds/sprayer_30d0f.mp3"
    gang "Я знал, что ты свой человек!"
    "{i}{color=#626262}Так, надо постараться не сильно испортить площадку. Попробую нарисовать что-то красивое. {/color} {/i}"
    play sound "sounds/sprayer_30d0f.mp3"
    gang```
    Ого, здорово получается, [friendName], ты не зря [friendPronoun] позвал[verb_end]

    Ха, и правда художник

    Разбавит наши скучные "художества"

    Ну да, а то твой предел это "йух" написать!

    Сам будто круче что-то можешь!

    Ну теперь-то у нас появился профи, с ним будет веселее
    ```
    
    "{i}{color=#626262}Им правда нравится? Никто давно так не хвалил мои рисунки… Может, все в жизни не так уж и плохо? {/color} {/i}"
    play sound "sounds/shagi-12.mp3"
    #ТУТ ЖЕЛАТЕЛЬНО КАКИЕ-НИБУДЬ ГРУЗНЫЕ ШАГИ ПО ЗЕМЛЕ


    stop music1 fadeout 2
    play music "music/Leaving Home.mp3" fadein 2
    show fat_policeman at right2 with dissolve
    f_pol "Так, шпана! Что это вы тут делаете?!"
    show tall_policeman at left2 with dissolve
    t_pol "Петрович, лови их!"
    stop sound
    play sound "sounds/run.mp3"
    fr "Черт, мусора! Бежим!"
    "{i}{color=#626262} А? Куда? Кого? {/color} {/i}"
    "*Компания разбегается, [playerName] стоит столбом*"
    stop sound
    t_pol "Кто это у нас тут? Пойдешь с нами, вандал." 
    "{i}{color=#626262}Почему я не сообразил[verb_end] и не побежал[verb_end]? Что теперь делать? Придется идти с ними. {/color} {/i}"

    jump act2_flashback_policy
    
    return

label act2_flashback_policy:

    play sound "sounds/shagi-23.mp3"

    scene bg flashback_policy1 with dissolve
    $ renpy.pause(1)

    scene bg flashback_policy with dissolve
    show fat_policeman with dissolve
    stop sound
    f_pol "Как тебя зовут, где твои родители?"
    gg "[playerName] Ковалев[verb_end], мама ушла на вечернюю подработку"
    f_pol "Знаешь ее номер?"
    gg "Да"
    "*[playerName] называет номер матери*"
    "{i}{color=#626262}Блин, влип[past_verb_end] так влип[past_verb_end] {/color} {/i}"
    hide fat_policeman with dissolve

    "Через 30 минут"
    show mom street with dissolve
    mom "Простите пожалуйста [friendPronoun]. Раньше он[verb_end] подобным не занима[past_end]."
    show mom street at right2 with moveinright
    show fat_policeman at left2 with dissolve
    f_pol "Не переживайте, на первый раз даже на учет не поставим."
    f_pol "В следующий раз следите лучше за своим ребенком."
    hide fat_policeman with dissolve
    mom "Дома поговорим."

    play sound "sounds/shagi-23 (mp3cut.net).mp3"

    jump act2_flashback_home
    
    return

label act2_flashback_home:
    stop music fadeout 2
    play music1 "music/Abuse In The Orphanage.ogg" fadein 2
    scene bg flashback_kitchen with dissolve
    show mom street with dissolve
    stop sound
    "Мама снимает кепку, проходит на кухню"
    mom "Иди сюда."
    "{i}{color=#626262}Кажется, мне хана... {/color} {/i}"
    show mom shout with dissolve
    mom "У меня нет слов. Я сказала тебе сидеть дома и заниматься уроками, а что сделал[verb_end] ты?!{w}{sc=1} СМЫ[past_end_shout] И \nНАЧАЛ[verb_end_shout] ПОРТИТЬ ДЕТСКУЮ ПЛОЩАДКУ!{/sc}"
    "{i}{color=#626262}Черт, черт, черт{/color} {/i}"
    mom "{sc=1}ТАК И ЭТОГО МАЛО. ТЫ УГОДИЛ[verb_end_shout] В УЧАСТОК МИЛИЦИИ!{/sc}{w} Тебе всего 13, хочешь пойти по стопам отца?!"
    gg "Ты же говорила, что его подставили…"
    mom "Это не важно, он сидит в тюрьме, а наша жизнь и репутация упали ниже плинтуса из-за этого, у нас нет денег и поддержки!"
    gg "Но мам…"
    mom "Не мамкай мне тут. Это все из-за твоих поганых рисунков. Мне это надоело. С этого дня ты под домашним арестом.{w} Ты обязан[verb_end] взяться за голову, пока еще не поздно, этими рисульками ты на жизнь не заработаешь. С этого дня никакого рисования!"
   
    play sound "sounds/z_uki-r_ut-bumagu.mp3"
   
    hide mom with dissolve
    #слышится звук рвущейся бумаги
    "{i}{color=#626262}Что это за звук?{/color} {/i}"
    stop sound
    play sound "sounds/19557.mp3"
    show bg flashback_room with wipeleft
    gg "{sc=1}Мама, что ты делаешь?!{/sc}"
    stop sound
    play sound "sounds/z_uki-r_ut-bumagu.mp3"
    show mom shout with dissolve
    mom "Как что? Избавляюсь от этого мусора. Мое терпение лопнуло. Если я еще раз увижу, что ты рисуешь, пеняй на себя."
    "*Мать забирает еще целые альбомы с рисунками*"
    hide mom with dissolve
    stop sound
    show bg flashback_room with vpunch
    $ renpy.pause(1)
    if gender_symbol == "♂":
        play sound "sounds/cartoon-dramatic-male-crying_zk7gssvd.mp3"
        scene flashback1b with fade
        $ persistent.flashback1b = True
    else:
        play sound "sounds/df8e786138341fc.mp3"
        scene flashback1g with fade
        $ persistent.flashback1g = True
    
    pause 
    #звуки плача
    "{sc=2}Как же… Почему все так получилось? Мои рисунки… Все, что я нарисовал[verb_end] за свою жизнь{/sc}"

    stop sound
    jump act2_present
    return


label act2_present:
    stop music fadeout 2

    play music1 "music/classic_music.mp3" fadein 2

    $ is_flashback = False

    scene bg gallery_up with pixellate
    show ghost surprised with dissolve
    gh "[playerName], прием! Ты тут? Я тебя уже пару минут зову, а ты не откликаешься"
    gg "Прости, задума[past_end]"
    gh "Все в порядке?"
    gg "Да, давай продолжать наше расследование.{w} Раз картина не навевает тебе никаких воспоминаний, то в этом месте должно быть что-то другое, что тянуло тебя сюда"
    gh normal "Логично. Может, информационная табличка?"
    gg "Давай посмотрим. И так, картину нарисовала Наоми Кортезе. Тебе о чем-то говорит это имя?"
    gh "Вообще нет"
    gg "Хм, тут сказано, что она окончила местный университет искусства. Странно, она иностранка, почему не выбрала столичный вуз?{w} Наш город, конечно, не маленький, но делать тут особо нечего"
    gh uncomprehending "Действительно странно"
    gg "И так, мы снова в тупике. Картина тебе ни о чем не говорит, имя художницы тоже…"
    gh normal "Не совсем, я не уверена, но кое-что все-таки есть"
    gg "Что?"
    gh "Когда мы прочитали об универе, что-то отозвалось во мне. Может, я училась там?"
    gg "Значит стоит направиться туда"

    scene bg gallery_front with dissolve

    show ghost normal with dissolve 
    gh "Стой, может мы немного походим по выставке?"
    gg "Хм, в принципе, идея неплохая"
    hide ghost with dissolve
    jump act2_front_pred_gallery

    return


label act2_front_pred_gallery:
    scene bg gallery_front with dissolve

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_interact==0:

        # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ ИМЕННО СЮДА!!!

        # Меняем значение переменной
        $ count_pred_interact = 1

    # Перемещаемся в блок интерактивности в центральной части галереи
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
        # Показываем фон, если он не был показан ранее
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

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_up==0:
        
        gg "Уродская картина..."

        # Меняем значение переменной
        $ count_pred_up = 1

    # Перемещаемся в блок интерактивности в дальней части галереи
    jump act2_up_gallery

    return

label act2_up_gallery:
    # ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ НИКАКИХ ДИАЛОГОВ, ВСЕ ДИАЛОГИ ВСТАВЛЯТЬ В БЛОК ВЫШЕ

    scene bg gallery_up with dissolve

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "gallery_up"

    jump showbuttons_gallery

    return

label act2_right_pred_gallery:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg gallery_right with dissolve
    
    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_right==0:
        gh "Как много пейзажей."

        # Меняем значение переменной
        $ count_pred_right = 1

    # Перемещаемся в блок интерактивности в правой части галереи
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
        # Показываем фон, если он не был показан ранее
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

label act2_left_pred_gallery:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    scene bg gallery_left with dissolve

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_left==0:
        gg "Хм..."

        # Меняем значение переменной
        $ count_pred_left = 1

    # Перемещаемся в блок интерактивности в левой части галереи 
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
        # Показываем фон, если он не был показан ранее
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

label move_gallery_up:
    # Убираем экран со стрелками
    hide screen movebuttons_gallery

    # Если текущая позиция - центральная часть галереи, то при нажатии на кнопку "вверх"
    if current_loc == "gallery_front":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в дальней части галереи
        jump act2_up_pred_gallery
    
    return

label move_gallery_right:
    # Убираем экран со стрелками
    hide screen movebuttons_gallery

    # Если текущая позиция - центральная часть галереи, то при нажатии на кнопку "вправо"
    if current_loc == "gallery_front":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в правой части галереи
        jump act2_right_pred_gallery
    # Иначе если текущая позиция - левая часть галереи, то при нажатии на кнопку "вправо"
    elif current_loc == "gallery_left":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в главной части галереи
        jump act2_front_pred_gallery

    return

label move_gallery_left:
    # Убираем экран со стрелками
    hide screen movebuttons_gallery

    # Если текущая позиция - главная часть галереи, то при нажатии на кнопку "влево"
    if current_loc == "gallery_front":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в левой части галереи
        jump act2_left_pred_gallery
    # Иначе если текущая позиция - правая часть галереи, то при нажатии на кнопку "влево"
    elif current_loc == "gallery_right":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в главной части галереи
        jump act2_front_pred_gallery

    return

label move_gallery_down:
    # Убираем экран со стрелками
    hide screen movebuttons_gallery

    # Если текущая позиция - дальняя часть галереи, то при нажатии на кнопку "вниз"
    if current_loc == "gallery_up":
        play sound "sounds/shagi-23 (mp3cut.net).mp3"
        # Перемещаемся в блок диалога в центральной части галереи
        jump act2_front_pred_gallery

    # Иначе если текущая позиция - центральная часть галереи, то при нажатии на кнопку "вниз"
    elif current_loc == "gallery_front":
        # Отображается меню выбора
        menu:
            "Внимание! Если вы подтвердите выбор, то покинете локацию!"
            "Покинуть картинную галерею":
                play sound "sounds/create_character.mp3"
                gh "Наверно, нам пора уходить"
                gg "Да, загулялись мы тут"


                jump act2_street
            "Еще рано":
                play sound "sounds/create_character.mp3"
                jump act2_front_pred_gallery

    return

label act2_street:

    play sound "sounds/shagi-23.mp3"

    stop music1 fadeout 2
    play music gallery1 fadein 2
    scene bg gallery_down with dissolve
    show ghost uncomprehending with dissolve
    gh "И все-таки, почему ты бросил[verb_end] рисовать?"
    gg "Да так… Вырос[past_verb_end], сменились увлечения, не до этого стало"
    stop sound
    gh surprised "Но я видела, как у тебя загорелись глаза, когда ты заговорил[verb_end] о живописи! Человек не может говорить о том, что ему не интересно с такими глазами."
    "{i}{color=#626262}Что же ответить… Все тогда так навалилось. Действительно ли я хочу об этом вспоминать? Не будет ли это ворошить прошлые раны? {/color} {/i}"

    menu:
        "Что ответить?"
        "Возможно, когда-нибудь я попробую снова заняться рисованием":
            play sound "sounds/create_character.mp3"
            $ renpy.notify("Вы приняли важное решение.")
            $ important1 = True
            $ note_painter1 = True
            gg "Возможно, когда-нибудь я вновь попробую заняться рисованием"
            gh happy "Хорошее решение"
            $ renpy.notify("В заметках появилась новая запись")

            gh "Мы почти пришли."

            jump act3_start

        "Это было простым детским увлечением":
            play sound "sounds/create_character.mp3"
            $ renpy.notify("Вы приняли важное решение.")
            $ note_painter2 = True
            gg "Это было простым детским увлечением, я не хочу к нему возвращаться"
            gh upset "Эх… Не в моей власти переубеждать тебя"
            $ renpy.notify("В заметках появилась новая запись")

            gh "Мы почти пришли."

            jump act3_start
    return
