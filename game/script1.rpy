python:
    def play_hover_sound():
        renpy.sound.play(hover_sound)


label start:
    stop music fadeout 0.5
    # Фон стола с компьютером от первого лица
    scene bg table1
    play sound "sounds/phone-vibration-96623.mp3"
    # Играет бодрая композиция
    play music1 start_music_2 fadein 2
    #"ГГ открывает глаза, просыпается" #в будущем - анимация
    "{i}{color=#626262} Ммм… {w}Уже вечер, засыпать за просмотром сериала становится дурной привычкой.{/color}{/i}"
    nvl_narrator "Заноза"
    fr_nvl "мы сегодня собирались в бар, помнишь? не опаздывай!!"
    gg_nvl "да как тут забудешь"
    gg_nvl "скоро выхожу"
    "{i}{color=#626262}Хм, а мне ведь так и не позвонили с последнего собеседования. Нужно написать им, пока помню.{/color}{/i}"
    jump create_character

    return

# Блок создания персонажа
label create_character:
    # Меню выбора одного из двух вариантов
    menu:
        #Подсказка в диалоговом окне
        "Выберите пол персонажа"

        #гг - парень, его друг - тоже парень, любовный интерес - девушка
        "♂ Я хотел бы узнать...":
            # Звук кликанья
            play sound "sounds/create_character.mp3"

            # При наведении на вариант, должен играть звук НЕ РАБОТАЕТ
            $ renpy.sound.play(hover_sound)

            #вводим имя гг и запоминаем его в переменной
            $ playerName = renpy.input("По умолчанию главному герою будет дано имя Миша. Введите имя персонажа, если желаете его заменить. ", length=12).strip() or "Миша"
            $ gender_symbol = "♂"
            $ gender = "male"

            #спрайт друга будет находиться в папке characters/yarik
            $ friendSprite = "yarik"
            $ friendSpriteYo = "yarik_young"
            #имя друга и местоимение
            $ friendName = "Ярик"
            $ friendPronoun = "его"
            $ needPronoun = "ним"

            #настраиваем окончания для мужского рода (используются гг и другом)
            $ verb_end = "" #глаголы
            $ past_verb_end = "" #глаголы прошедшего времени
            $ past_end = "лся"

            $ verb_end_shout = "" #глаголы
            $ past_verb_end_shout = "" 
            $ past_end_shout = "ЛСЯ"

            #инициализируем переменные, отвечающие за имя, спрайт, окончания глаголов у любовного интереса гг
            $ partnerName = "Олеся"
            $ partnerSprite = "olesya"
            $ verb_end1 = "а" 
            $ past_verb_end1 = "ла" 
            $ past_end1 = "лась"
            $ friendPronoun1 = "её"
            $ needPronoun1 = "ней"

        #гг - девушка, ее друг - тоже девушка, любовный интерес - парень
        "♀ Я хотела бы узнать...":
            # Звук кликанья
            play sound "sounds/create_character.mp3"
            # При наведении на вариант, должен играть звук НЕ РАБОТАЕТ
            $ renpy.sound.play(hover_sound)

            #вводим имя гг и запоминаем его в переменной
            $ playerName = renpy.input("По умолчанию главной героине будет дано имя Алиса. Введите имя персонажа, если желаете его заменить. ", length=12).strip() or "Алиса"
            $ gender_symbol = "♀"
            $ gender = "female"

            #спрайт друга будет находиться в папке characters/lisa
            $ friendSprite = "lisa"
            $ friendSpriteYo = "lisa_young"
            #имя друга и местоимение
            $ friendName = "Лиза"
            $ friendPronoun = "её"
            $ needPronoun = "ней"

            # Настраиваем окончания для женского рода (используются гг и подругой)
            $ verb_end = "а" #глаголы
            $ past_verb_end = "ла" #глаголы прошедшего времени
            $ past_end = "лась"

            $ verb_end_shout = "А" #глаголы
            $ past_verb_end_shout = "ЛА" 
            $ past_end_shout = "ЛАСЬ"

            #инициализируем переменные, отвечающие за имя, спрайт, окончания глаголов у любовного интереса гг
            $ partnerName = "Игорь"
            $ partnerSprite = "igor"
            $ verb_end1 = "" 
            $ past_verb_end1 = "" 
            $ past_end1 = "лся"
            $ friendPronoun1 = "его"
            $ needPronoun1 = "ним"
            

    # Показываем предупреждение, что пересоздать персонажа будет нельзя
    "Отнеситесь серьезно к созданию персонажа, в течении игры эти настройки будет не изменить."
    # Меню выбора: уверены ли вы в создании персонажа
    menu:
        # Подсказка в диалоговом окне
        "Что вы хотите сделать?"

        # Если уверены в создании персонажа
        "Подтвердить создание":
            play hover "sounds/create_character.mp3"
            #инициализируем переменные, отвечающие за эмоции друга и любовного интереса
            $ fr_normal = friendSprite + " normal"
            $ fr_angry = friendSprite + " angry"
            $ fr_winks = friendSprite + " winks"
            $ fr_uncomprehending = friendSprite + " uncomprehending"

            $ fr_yo_normal = friendSpriteYo + " normal"
            $ fr_yo_smile = friendSpriteYo + " smile"
            $ fr_yo_grin = friendSpriteYo + " grin"

            $ par_normal = partnerSprite + " normal"
            $ par_grin = partnerSprite + " grin"
            $ par_winks = partnerSprite + " happy"
            # Переходите в следующий блок
            jump continue_start

        # Если не уверены в создании персонажа
        "Пересоздать персонажа":
            play hover "sounds/create_character.mp3"
            # Возвращаетесь в блок создания персонажа
            jump create_character

    return

# Блок диалога с работодателем и мыслей героя по поводу ситуации
label continue_start:
    nvl clear
    nvl_narrator "Работа"
    gg_nvl "Здравствуйте, я хотел[verb_end] бы узнать по поводу собеседования на должность бариста, оно было 3 дня назад"
    hr_nvl "Добрый вечер! Вы - [playerName] Ковалёв[verb_end]?"
    gg_nvl "Да"
    hr_nvl "Одну минутку… "
    hr_nvl "К сожалению, вам отказано, вы нам не подходите."
    gg_nvl "Понятно."

    stop music1 fadeout 2

    # Играет депрессивная композиция
    play music start_music_1 fadein 2

    "{i}{color=#626262}Cнова мимо… Денег уже почти не осталось, видимо, опять придется просить {b}{color=#5f2626}[friendPronoun]{/color}{/b} подкинуть работу.{/color}{/i}"
    
    # Перемещаемся в блок с комнатой гг
    jump room

    return

# Блок, в котором гг находится в своей комнате
label room:
    # Фон комнаты гг в общежитии
    scene bg room2 with dissolve
 
    if not info_panel_closed_1:
        show screen info_panel_interactive

    # Цикл для ожидания закрытия подсказки
    while not info_panel_closed_1:
        # Ждем, пока подсказка не будет закрыта
        $ renpy.pause(0.1)

    gg "Пора собираться в бар."

    # Перемещаемся в блок с интерактивностью по комнате
    jump move_in_room

    return

# Блок, в котором можно изучить комнату гг (интерактивный фон)
label move_in_room:
    # Прячем диалоговое окно
    window hide

    # Показываем подсказку относительно перемещения по локациям, если она ещё не была закрыта
    if not info_panel_closed_1:
        show screen info_panel_door

    # Цикл для ожидания закрытия подсказки
    while not info_panel_closed_1:
        # Ждем, пока подсказка не будет закрыта
        $ renpy.pause(0.1)

    # Показываем фон комнаты, если он не был показан ранее
    if not persistent.background_shown:
        show bg room2 with dissolve
        # Меняем глобальную переменную на True, так как фон был показан
        $ persistent.background_shown = True

    # Запускаем интерактивный экран с плавным эффектом
    show screen mapScreen with dissolve

    # Включаем интерактивное взаимодействие
    $ result = ui.interact()

    return

# Блок: коридор общаги, гг идет на встречу к другу
# Если гг потыкался на количество предметов >=7, то он опоздает на встречу
label go_to_hall:
    # Показываем фон коридора общаги
    show bg hall2 with dissolve

    play hover "sounds/shagi-23.mp3"

    # Проверяем, если игрок "тыкался" больше 7 раз
    if time >= 7:
        "{i}{color=#626262}Кажется, я опаздываю.{/color}{/i}"
        # Меняем логическую переменную на True
        $ bool_time = True
        $ persistent.late = True
        if persistent.late_notify == 0:
            $ renpy.notify("Открыто новое достижение!")
            $ persistent.late_notify += 1
        
    "{i}{color=#626262}Пора идти.{/color}{/i}"

    # Перемещаемся в блок, где гг идет с другом в бар
    jump bar_outside

    return

# Блок: гг встретился с другом и идет в бар
label bar_outside:
    # Показываем фон перед входом в бар
    scene bg bar_outside with dissolve

    stop music fadeout 2
    play music1 start_music_2 fadein 2

    # Проверка, провел ли игрок слишком много времени в комнате
    if bool_time:
        $ note_meet_fr2 = True
        show expression fr_angry with dissolve
        fr "[playerName], когда ты научишься приходить вовремя?! Я тебя уже пол часа стою жду."
        hide fr_angry
        show expression fr_normal
        fr "Пошли внутрь, нам есть о чем поговорить."
        hide fr_normal with dissolve

    else:
        $ note_meet_fr1 = True
        show expression fr_normal with dissolve
        fr "Рад[verb_end], что ты вовремя. Пойдем внутрь, нам есть, что обсудить."
        hide fr_normal with dissolve

    $ renpy.notify("В заметках появилась новая запись")

    # Показываем фон перед входом в бар, если он не был показан ранее
    if not persistent.background_shown:
        show bg bar_outside with dissolve
        # Меняем глобальную переменную на True, так как фон был показан
        $ persistent.background_shown = True

    # Запускаем интерактивный экран (на нем при наведении будет подсвечиваться дверь)
    show screen barScreen with dissolve

    # Включаем интерактивное взаимодействие (пока не нажмем на дверь, не попадем внутрь бара)
    $ result = ui.interact()
    # Перемещаемся в блок внутри бара
    jump bar_inside

    return

# Блок внутри бара: подготовительный
label bar_inside:
    # Логические переменные для отслеживания того, впервые мы появляемся в блоке локации или нет
    # Если впервые, то запускается диалог, иначе ничего не происходит
    $ count_pred_interact = 0
    $ count_pred_up = 0
    $ count_pred_right = 0
    $ count_pred_left = 0

    # Показываем фон бара с людьми
    show bg bar_people with fade
    $ renpy.pause(0.5)

    stop music1 fadeout 2
    play music bar2 fadein 2

    #ЗВУК ШАГОВ?

    show bg bar_without_alcohol with fade
    show expression fr_normal with dissolve
    fr "Выбирай, что душе угодно, сегодня я угощаю."
    gg "Щедро. Есть повод?"
    hide fr_normal
    show expression fr_winks 
    fr "Ага, хороший договор удалось заключить. Теперь получится увеличить поставки в 1.5 раза."
    gg "Поздравляю. {i}{color=#626262}Значит, для меня тоже найдется работа. Почему же не получается радоваться?{/color}{/i}"
    show expression fr_winks at right2 with moveinright
    show barman normal at left2 with dissolve
    fr "Бармен, мне как обычно. [playerName], что выбрал[verb_end]?"
    gg "А? Да мне то же самое."
    barman angry "2 джин-тоника, через 5 минут будет готово."
    hide barman with dissolve
    show expression fr_winks at center with move
    hide fr_winks
    show expression fr_uncomprehending

    hide window

    if not info_panel_closedd_1:
        show screen info_panel_relationship

    # Цикл для ожидания закрытия подсказки
    while not info_panel_closedd_1:
        # Ждем, пока подсказка не будет закрыта
        $ renpy.pause(0.1)

    fr "Обычно ты более разговорчив[verb_end]. Все ок?"

    # Выбор, который повлияет на отношения с другом
    menu:
        "Как поступить?"

        "Рассказать о проблемах в поиске работы":
            play hover "sounds/create_character.mp3"
            # Плюс дружба
            $ friendship_fr += 1
            gg "Да что-то с работой все не ладится, хотел[verb_end] устроиться бариста, не взяли."
            hide fr_uncomprehending
            show expression fr_winks
            fr "Мда уж. Но ты не переживай, у нас тебе всегда найдется местечко."
            hide fr_winks
            show expression fr_normal
            $ renpy.notify(f"Отношения с персонажем {friendName} улучшились") #в будущем заменить на стрелочки вверх вниз зеленых и красных цветов мб с анимацией
            $ renpy.pause(0.2)

        "Не доверять другу свои проблемы":
            play hover "sounds/create_character.mp3"
            # Минус дружба
            $ friendship_fr -= 1
            gg "Да… просто спалось плохо"
            fr "Правда? Ну ладно, допытываться не буду"
            hide fr_uncomprehending
            show expression fr_normal
            $ renpy.notify(f"Отношения с персонажем {friendName} ухудшились")
            $ renpy.pause(0.2)

    show expression fr_normal at right2 with moveinright
    show barman normal at left2 with dissolve
    barman "Ваши коктейли."
    show bg bar_with_alcohol with dissolve
    fr "Благодарю."
    hide barman with dissolve
    fr "Держи, расслабься. Сегодня хороший вечер, не стоит думать о проблемах."
    
    # Звук питья
    play sound "sounds/drink_sound.mp3"

    gg "Спасибо, возможно, ты прав[verb_end], [friendName]. {i}{color=#626262}Отопью глоток.{/color}{/i}"
    # Звук питья
    play sound "sounds/drink_sound.mp3"
    gg "Сегодня неплохая погода, последние теплые осенние вечера."
    fr "Ага, мы как раз с нашей компанией на прошлых выходных на шашлыки гоняли к Андрею на дачу. [partnerName], кстати тоже там был[verb_end1]."
    "{i}{color=#626262}Мда, зачем [friendName] мне это говорит...{w} Вкусный напиток, отопью еще.{/color}{/i}"
    
    play sound "sounds/drink_sound.mp3"

    gg "А давно он[verb_end1] входит в «компанию»?"
    fr "{bt=1}Не, что ты. Совсем недавно удалось пересечься на одной тусе. \nМы разговорились, оказалось он[verb_end1] подзарез нуждается в деньгах, \nсам[verb_end] знаешь, как это бывает.{/bt}" 
    fr "{bt=2}Ну, я и предложил[verb_end] поработать у нас. Оказалось, он[verb_end1] обладает невероятным \nталантом искать новых клиентов, [partnerName] умеет так забалтывать людей, \nчто они ведутся и пробуют наш товар, а после подсаживаются на него, \nбинго.{/bt}"
    show expression fr_winks at right2
    fr "{bt=2}С тех пор он[verb_end1] член нашей небольшой, но очень дружной «семьи».{/bt}"
    "{i}{color=#626262}Не это я ожидал[verb_end] услышать.{w} Сделаю еще глоток.{/color}{/i}"
    
    play sound "sounds/drink_sound.mp3"

    gg "{bt=3}Зачем ты мне это рассказываешь? Ты же знаешь, в каких \nмы отношениях после того случая.{/bt}"
    hide fr_winks
    fr "{bt=3}[playerName], может уже пора помириться? Оставь обиды прошлого, \nработая в команде, вы могли бы получать огромную кучу \nденег.{/bt}"
    extend "{bt=4}Ты, возможно, сможешь наконец съехать со своей халупы…{/bt}"
    "{i}{color=#626262}Еще глоток...{/color}{/i}"
    
    play sound "sounds/drink_sound.mp3"

    show expression fr_uncomprehending at right2
    fr "{bt=5}Ты меня вообще слушаешь?{/bt}"
    gg "{bt=5}[friendName], о чем ты? Я тебя не расслышал[verb_end].{/bt}"
    fr "{bt=6}Эй, ты в порядке? Выглядишь бледно.{/bt}"
    gg "{bt=6}Да, наверно. Хочу подышать свежим воздухом.{/bt}"
    show bg bar_with_alcohol with vpunch
    "[playerName] пытается встать, [friendPronoun] шатает, [friendName] усаживает [friendPronoun] обратно на стул" 
    fr "{bt=6}Голова кружится? Может, стоит посидеть, когда пройдет, \nпойдем на улицу.{/bt}"
    hide fr_uncomprehending
    fr "{bt=10}На, попей, у тебя тут еще осталось.{/bt}"
    "{bt=10}{i}{color=#626262}Что это? Где я? Мне надо это выпить?{/color}{/i}{/bt}"
    gg "{bt=10}Наверно… Ты прав[verb_end]…{/bt}"

    # ЗВУК ПОТЕРИ СОЗНАНИЯ/ПАДАНИЯ

    hide fr_normal with dissolve

    # Перемещаемся в блок встречи с призраком
    jump meet_ghost

    return

# Блок встречи 
label meet_ghost:
    stop music fadeout 2
    # ДОБАВИТЬ ЭФФЕКТ ПРОБУЖДЕНИЯ
    stop music fadeout 2
    
    # Показываем фон дворика за баром
    play sound "sounds/singing.mp3"
    show bg street_center with fade
    $ renpy.pause(1.5)
    show bg street_animation_right with fade
    $ renpy.pause(1.5)
    show bg street_animation_left with fade
    "{i}{color=#626262}Я… Где?{w} Улица. Темно, ночь?{w} Кто-то поет?{/color}{/i}"

    "[playerName] оборачивается в поисках источника звука"

    show meet_ghost with fade
    $ persistent.meeting = True
    stop sound fadeout 2
    play music1 start_music_0

    stop sound fadeout 2
    play music1 start_music_0

    $ renpy.pause(1.2)
    gg "Это…{w} что такое?"
    gh "О, ты можешь меня видеть?! Невероятно!"
    "{i}{color=#626262}Что за...{/color}{/i}"
    show bg street
    hide meet_ghost with fade
    show ghost normal with dissolve
    gh "Подожди секунду, я подойду."
    gg "{sc=2}СТОЙ, НЕ ПОДХОДИ,{w} ЧТО ТЫ ТАКОЕ?{/sc}"
    gh surprised "Не переживай, я не причиню тебе вреда, я лишь хочу поговорить!"

    # Выбор, который повлияет на отношения с призраком
    menu:
        "Что делать? Внимание, ваш выбор повлияет на отношения с данным персонажем"

        "Успокоиться, поговорить с призраком":
            play hover "sounds/create_character.mp3"

            $ note_meet_gh1 = True
            gg "{sc=2}Хорошо, но не подходи ближе. Давай поговорим.{/sc}"

            $ friendshp_gh += 1
            $ renpy.notify(f"Отношения с персонажем Призрак улучшились")
            gh happy "Спасибо, я сейчас все объясню"

        "Бежать":
            play hover "sounds/create_character.mp3"
            $ note_meet_gh2 = True

            show bg street with vpunch
            "[playerName] пытается подняться, но не может из-за плохого самочувствия." #все это надо как-то обыграть с помощью анимаций и смены фонов
            "{sc=3}{i}{color=#626262}Черт, надо валить, но я не могу встать.{/color}{/i}{/sc}"
            "{sc=3}{i}{color=#626262}Где мой телефон, что мне делать?{w} Надо ползти.{/color}{/i}{/sc}" 
            hide ghost

            #ЗВУК ПОЛЗАНИЯ?

            show bg bar_down with wipeleft
            gg "{sc=4}НЕ ПОДХОДИ,{w} ИЗЫДИ{/sc}"
            gh "Стой же!"
            "{sc=4}{i}{color=#626262}Твою ж...{w} Моя спина уперлась в стенку. Что делать?!{/color}{/i}{/sc}"
            "{sc=4}{i}{color=#626262}Черт, черт, черт, почему именно я?{w} Оно уже рядом...{/color}{/i}{/sc}"
            show ghost surprised
            gh "Постой, я правда не хочу сделать ничего плохого, я тебя напугала? Прости пожалуйста, я все сейчас объясню!"

    gh normal "На самом деле, я очень рада, что ты меня видишь"
    gg "{sc=2}Ты и правда призрак, или это все какой-то дурацкий пранк?{/sc}"
    gh upset "Мне бы очень хотелось, чтобы это было пранком, но нет. Я умерла несколько дней назад."
    gg "Соболезную… А как это произошло?"
    gh "Если честно… Я не помню."
    gg "Это странно, призраки обычно связаны со своей смертью. Ты не помнишь ни одной детали?"
    gh "Нет, все как в тумане, скажу больше, я совершенно не знаю кто я."
    gh surprised "Ты первый человек, который смог меня увидеть, помоги мне, пожалуйста!"
    gg "Слушай, это все, конечно, звучит печально, мне тебя жаль, но у меня полно своих проблем. Мне некогда таскаться с призраком и искать его воспоминания."
    gh "Подожди! Пожалуйста, не уходи! Я действительно хочу понять, что со мной произошло..."
    gg "Я понимаю, но мне нужно расслабиться. У меня тяжёлый день, и я не готов[verb_end] к этому. Я сожалею о твоём положении, но это не делает это моим бременем."
    show ghost upset
    gg "Я вернусь позже, может быть."

    # Перемещаемся в блок диалога перед навигацией
    jump bar_interact_pred

# Блок диалога перед интерактивностью (или свободной навигацией) в главном зале бара
label bar_interact_pred:

    # Делаем так, чтобы при возвращении в главную локацию музыка не звучала заново
    if not werePlayed:

        #ЗВУК ШАГОВ?

        stop music1 fadeout 2

        play music bar_interact fadein 2

        $ werePlayed = True

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False

    # Инициализаруем переменную, проверяющую, нажата ли кнопка входа в интерактивный фон
    $ closed_1 = False

    # Показываем фон бара с людьми
    scene bg bar_people with dissolve
    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_interact==0:
        gg "Телефон, оказывается все это время был в кармане... Мда."
        $ renpy.notify("В заметках появилась новая запись")
        gg "Ну и денек… Надо выпить."
        # Меняем значение переменной
        $ count_pred_interact = 1
    # Перемещаемся в блок интерактивности в главном зале бара 
    jump bar_interact

    return

# Блок интерактивности в главном зале бара
label bar_interact:
    $ current_state = "bar_interact"

    # Показываем подсказку относительно перемещения по локациям, если она ещё не была закрыта
    if not info_panel_closed:
        show screen info_panel

    # Меняем текущее местоположение для осуществления правильной логики навигации
    $ current_loc = "bar_front"
    
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
    #                 show bg bar_people with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True

    #             # Запускаем интерактивный экран
    #             show screen barInteract with dissolve
    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"
    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_interact = 1
    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся

    while not closed:
        # Закрываем диалоговое окно
        window hide

        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg bar_people with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen barInteract with dissolve

        # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
        $ interactive_mode_ended_interact = 1

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()
    
    hide barInteract

    jump showbuttons

    return

# Блок диалога перед интерактивностью или СН в дальней части бара (в нее можно попасть с помощью стрелок навигации)
label bar_up_pred:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False
    # Показываем фон дальней части бара
    scene bg bar_up with dissolve
    
    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_up==0:
        gg "Дальние залы, редко сюда захожу."
        # Меняем значение переменной
        $ count_pred_up = 1
    # Перемещаемся в блок интерактивности в дальней части бара
    jump bar_up

    return

# Блок интерактивности в дальней части бара
label bar_up:
    $ current_state = "bar_up"
    # Показываем фон дальней части бара
    scene bg bar_up with dissolve
    # Меняем текущую локацию, так как мы переместились в другое место
    $ current_loc = "bar_up"

    # # Показываем меню выбора, если мы еще не включали интерактивный экран
    # if interactive_mode_ended_up == 0:
    #     menu:
    #         "Осмотреться":
    #             window hide
    #             # Показываем фон дальней части бара, если он не был показан ранее
    #             if not persistent.background_shown:
    #                 show bg bar_up with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True
    #             # Запускаем интерактивный экран
    #             show screen barUp with dissolve
    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"
    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_up = 1
    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся

    while not closed:
        # Закрываем диалоговое окно
        window hide

        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg bar_up with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen barUp with dissolve

        # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
        $ interactive_mode_ended_interact = 1

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()
    
    hide barUp

    jump showbuttons

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вверх"
label move_bar_up:
    # Убираем экран с кнопками
    hide screen movebuttons
    # Если текущая позиция - главный зал бара, то при нажатии на кнопку "вверх"
    if current_loc == "bar_front":
        # Перемещаемся в блок диалога в дальней части бара
        jump bar_up_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons

    return

# Блок диалога перед интерактивностью или СН в правой части бара (в нее можно попасть с помощью стрелок навигации)
label bar_right_pred:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False
    # Показываем фон правой части бара
    scene bg bar_right with dissolve
    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_right==0:
        gg "Так мало народу, странно."
        # Меняем значение переменной
        $ count_pred_right = 1
    # Перемещаемся в блок интерактивности в правой части бара
    jump bar_right

    return

# Блок интерактивности в правой части бара
label bar_right:
    $ current_state = "bar_right"
    # Показываем фон правой части бара
    scene bg bar_right with dissolve
    # Меняем текущую локацию
    $ current_loc = "bar_right"
    # # Показываем меню выбора, если мы еще не включали интерактивный экран
    # if interactive_mode_ended_right == 0:
    #     menu:
    #         "Осмотреться":
    #             window hide
    #             # Показываем фон правой части бара, если он не был показан ранее
    #             if not persistent.background_shown:
    #                 show bg bar_right with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True
    #             # Запускаем интерактивный экран
    #             show screen barRight with dissolve
    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"
    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_right = 1
    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся

    while not closed:
        # Закрываем диалоговое окно
        window hide
        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg bar_right with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen barRight with dissolve

        # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
        $ interactive_mode_ended_interact = 1

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()
    
    hide barRight

    jump showbuttons

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вправо"
label move_bar_right:
    # Убираем экран с кнопками
    hide screen movebuttons
    # Если текущая позиция - главный зал бара, то при нажатии на кнопку "вправо"
    if current_loc == "bar_front":
        # Перемещаемся в блок диалога в части бара
        jump bar_right_pred
    # Иначе если текущая позиция - левая часть бара, то при нажатии на кнопку "вправо"
    elif current_loc == "bar_left":
        # Перемещаемся в блок диалога в главном зале бара
        jump bar_interact_pred
    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons

    return

# Блок диалога перед интерактивностью или СН в левой части бара (в нее можно попасть с помощью стрелок навигации)
label bar_left_pred:
    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False
    # Показываем фон левой части бара
    scene bg bar_left with dissolve
    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_left==0:
        gg "Стоит подойти к бармену."
        # Меняем значение переменной
        $ count_pred_left = 1
    # Перемещаемся в блок интерактивности в левой части бара
    jump bar_left

    return

# Блок интерактивности в левой части бара
label bar_left:
    $ current_state = "bar_left"
    # Показываем фон левой части бара
    scene bg bar_left with dissolve
    # Меняем текущую локацию
    $ current_loc = "bar_left"

    # # Показываем меню выбора, если мы еще не включали интерактивный экран
    # if interactive_mode_ended_left == 0:
    #     menu:
    #         "Осмотреться":
    #             window hide
    #             # Показываем фон левой части бара, если он не был показан ранее
    #             if not persistent.background_shown:
    #                 show bg bar_left with dissolve
    #                 # Меняем глобальную переменную на True, так как фон был показан
    #                 $ persistent.background_shown = True
    #             # Запускаем интерактивный экран
    #             show screen barLeft with dissolve
    #             # Выведется только один раз
    #             "Нажмите на кнопку, если хотите выйти из интерактивного режима"
    #             # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
    #             $ interactive_mode_ended_left = 1
    #             # Включаем интерактивное взаимодействие
    #             $ result = ui.interact()

    #         "Исследовать локацию позже":
    #             "Продолжайте ходить по локациям"
    #             # Переходим в блок, который открывает экран с кнопками навигации
    #             jump showbuttons

    # # Если мы потыкались больше, чем на 1 предмет
    # else:
    #     # Пока не закроем интерактивный экран с помощью кнопки, кнопки навигации не появятся

    while not closed:
        # Закрываем диалоговое окно
        window hide

        # Показываем фон главного зала в баре, если он не был показан ранее
        if not persistent.background_shown:
            show bg bar_left with dissolve
            # Меняем глобальную переменную на True, так как фон был показан
            $ persistent.background_shown = True

        # Запускаем интерактивный экран
        show screen barLeft with dissolve

        # Меняем значение переменной, так как мы уже запустили интерактивный экран (больше нам не нужно меню выбора в этой локации)
        $ interactive_mode_ended_interact = 1

        # Включаем интерактивное взаимодействие
        $ result = ui.interact()
    
    hide barLeft

    jump showbuttons

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "влево"
label move_bar_left:
    # Убираем экран с кнопками
    hide screen movebuttons
    # Если текущая позиция - главный зал бара, то при нажатии на кнопку "влево"
    if current_loc == "bar_front":
        # Перемещаемся в блок диалога в левой части бара
        jump bar_left_pred
    # Иначе если текущая позиция - правая часть бара, то при нажатии на кнопку "влево"
    elif current_loc == "bar_right":
        # Перемещаемся в блок диалога в главном зале бара
        jump bar_interact_pred
    # Иначе локация недопступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons

    return

# Блок: дворик за баром, возвращаемся к призраку после заказа выпивки
label bar_down:
    # Показываем фон дворика
    scene bg bar_down with wipeleft

    #ЗВУК БЕГА?

    # Играем музыку, трогающую душу
    stop music fadeout 1
    play music1 choise_1 fadein 2

    show ghost happy
    gh "О, ты так быстро, не ожидала."
    gg "Только что сквозь меня прошел человек,{w}{sc=2} Я ЧЕРТОВ ПРИЗРАК!{/sc}"
    gh uncomprehending "Нет, ты не можешь быть призраком, я вижу тебя ровно так же, как и обычных людей, у тебя такой же облик."
    gh " Если бы ты был[verb_end] призраком, ты был[verb_end] бы похож[verb_end] на меня, наверно."
    gg "{sc=1}Это все очень странно и страшно, я не хочу этого, я хочу просто домой \nи лечь спать. Но какой в этом всем теперь этом смысл, если \nменя даже не видят другие люди?{/sc}"

    gh upset "Мне очень жаль, я понимаю твои чувства."
    gh normal "Если хочешь, мы можем объединиться, попробуем помочь друг другу."

    # Выбор, который повлияет на концовку
    menu:
        "Что же делать?"
 
        "Помочь призраку":
            play hover "sounds/create_character.mp3"
            $ renpy.notify("Вы приняли важное решение.")
            gg "Хорошо, выбора все равно особо нет, только ты видишь меня и только я вижу тебя."
            gh happy "Спасибо тебе. Уверена, вдвоем мы добьемся успехов."
            $ friendshp_gh += 2
            $ renpy.notify(f"Отношения с персонажем Призрак улучшились")
            gg "Кстати, забыл[verb_end] представиться, я – [playerName]."
            gh normal "Очень приятно.{w} Я не помню своего имени, так что зови меня просто Призрак."
            gg "Не переживай, мы выясним кто ты."

            # Переходим во 2 акт
            jump act2_start

        "Идти своей дорогой":
            play hover "sounds/create_character.mp3"
            $ renpy.notify("Вы приняли важное решение.")
            gg "Извини, я уже говорил[verb_end] раньше, у меня и так своих проблем куча, а тут еще это. Мне проще решать все в одиночку. Я пойду."
            # Переходим в блок концовки
            jump ending_first

    return

# Блок перехода на другую локацию, запускается при нажатии на кнопку "вниз"
label move_bar_down:
    # Убираем экран с кнопками
    hide screen movebuttons
    # Если текущая позиция - верхняя часть бара, то при нажатии на кнопку "вниз"
    if current_loc == "bar_up":
        # Перемещаемся в блок диалога в главном зале бара
        jump bar_interact_pred

    # Иначе локация недоступна
    else:
        "Локация недоступна"
        # Переходим в блок, который открывает экран с кнопками навигации
        jump showbuttons

    return

# Блок с концовкой №1
label ending_first:
    $ persistent.alone = True

    window hide

    if gender_symbol == "♂":
        $ persistent.ending1b = True
        scene lonely_end_b with fade
    else:
        $ persistent.ending1g = True
        scene lonely_end_g with fade

    pause

    "{glitch=2}Хорошее ли решение я принял[verb_end]?{/glitch}"
    "{glitch=2}Справлюсь ли я в одиночку с этой проблемой?{/glitch}"
    "{glitch=2}А хочу ли я справляться с ней?{/glitch}"
    "{glitch=2}Красивый вид, люблю ночной город...{/glitch}"

    show the_end with fade
    pause

    return

