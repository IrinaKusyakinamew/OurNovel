label act4_start:
    scene bg graffity with dissolve
    show ghost normal with dissolve
    gh "Пришли."
    gg "Помню, ты писала на канале тг, что ты планируешь очень большой проект. Это он?"
    gh "Да… Но как видишь, я почти ничего не успела."
    gg "Что помешало?"
    gh "Давай подойдем поближе."

    scene bg graffity with pixellate
    show naomi normal with dissolve
    play sound "sounds/paint_brush_artists_dabs_brushes_on_wood_palett_005_41143.mp3"
    #Наоми рисует, звук
    na "Отлично, половина работы выполнена. Надеюсь, сегодня получится закончить. Через пару часов уже надо сворачиваться и идти домой, пока родители ничего не заподозрили."
    stop sound
    play sound "sounds/vauxhall-carlton-podyezjaet.mp3"
    #подъезжает машина, звук
    $ renpy.pause(8)
    stop sound
    show naomi normal at right2 with moveinright
    show n_dad angry at left2 with dissolve
    nd "Вот ты где."
    show naomi angry at right2
    na "Отец? Что ты здесь делаешь?"
    nd "Это ты мне скажи, что ТЫ здесь делаешь? Ты разве не должна быть на открытой лекции по портретному рисунку?"
    na "Тебе рассказал Айзек?"
    nd "Да. И я очень сильно разочарован в тебе, Наоми. Мы с матерью возлагали на тебя большие надежды, твои работы обязаны попасть в лучшие галереи мира."
    na "Но ты же сам не даешь мне рисовать так как я хочу!"
    nd "То, что ты называешь рисунком – бессмысленная мазня. Я жду от тебя настоящих шедевров, как у Жак-Луи Давида или Николы Пуссена."
    na "Но мне не нравится такой жанр живописи! Я хочу рисовать так, как считаю нужным."
    nd "И то что ты, юная леди, обманывая своих родителей, по вечерам шляешься непонятно где и занимаешься вандализмом меня расстраивает еще больше."
    na "Это не вандализм. Я создаю настоящие произведения искусства и делаю это только на старых заброшенных зданиях."
    show n_dad normal at left2
    nd "Я не хочу слушать эти отговорки. Садись в машину. С этого дня ты под домашним арестом."
    show naomi normal at right2
    na "Я не поеду с тобой."
    nd "Сядь по-хорошему, Наоми."
    show naomi angry at right2
    na "Нет!"
    nd "Усади ее в машину."
    hide n_dad with dissolve
    show guard at left2 with dissolve
    "Охранник" "Наоми, не вынуждайте меня применять грубую силу."
    play sound "sounds/mashina-startuet-i-byistro-uezjaet-34233.mp3"
    #уезжают, звук
    $ renpy.pause(10)
    stop sound
    scene bg estate with dissolve
    $ renpy.pause(0.7)
    scene bg estate_hall with dissolve
    show n_dad normal at left2 with dissolve
    nd "Тебе запрещено покидать поместье. Твой телефон я также забираю."
    show naomi angry at right2 with dissolve
    na "Что?!"
    nd "Через 3 месяца в этом городе будет выставка картин. Я уже договорился, твоя картина должна стать главным экспонатом. Ты обязана нарисовать картину, достойную нашей семьи."
    na "Ты не можешь просто запереть меня здесь! Я не стану рисовать то, что ты хочешь!"
    show n_dad smile at left2
    nd "Станешь, если захочешь еще когда-нибудь выйти отсюда, увидеться со своими друзьями."
    hide n_dad with dissolve
    na "Урод… Ненавижу его."
    na "Еще и Айзек… Почему он сдал меня? Когда я его увижу, я ему устрою."
    hide naomi with dissolve
    na "Надо попробовать сбежать."

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


    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_interact==0:

        na "Нужно убираться отсюда"

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

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_right==0:

        na "Я не хочу делать то, о чем просит отец."

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

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_left==0:

        na "Я не голодна."

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

    # Инициализаруем переменную, проверяющую, нажата ли кнопка выхода из интерактивного фона
    $ closed = False 

    # Если мы впервые в этой локации, запускается диалог (иначе происходит переход к др. блоку без диалога)
    if count_pred_down==0:

        na "Внизу только море и скалы. Прыгать - верная смерть."

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
    if k >= 3:
        $ persistent.running = True
        if persistent.running_notify == 0:
            $ renpy.notify("Открыто новое достижение!")
            $ persistent.running_notify += 1

    show naomi_draws with dissolve
    pause
    na "Видимо, у меня нет выбора. Сейчас за мной пристально следят. Нарисую эту уродскую картину, а потом буду думать о том, как убраться навсегда из этого дома."
    hide naomi_draws with dissolve
    "Прошло 3 месяца"
    show n_dad smile at left2 with dissolve
    nd "Молодец, вот можешь, когда хочешь"
    show naomi normal at right2 with dissolve
    na "Угу. Теперь я могу идти?"
    nd "Да, ты свободна в своем перемещении."
    hide n_dad with dissolve
    na "Айзек за все это время ни разу не навестил меня. Время уже позднее. Пожалуй, наведаюсь к нему на работу…"

    #Место действия: VIP комната бара
    #звук открывания двери с ноги
    stop music1 fadeout 2
    play sound "sounds/e36add97d2dbebd.mp3"
    scene bg vip_bar with dissolve #заменить
    play music "music/Leaving Home.mp3" fadein 2
    stop sound
    show aizek normal at left2 with dissolve
    aik "Наоми?"
    show naomi rage at right2 with dissolve
    na "Айзек! Какого хера ты сдал меня отцу? Ты хоть знаешь, что со мной сделали?"
    show aizek calm at left2
    aik "Тебя посадили под домашний арест и заставили рисовать картину."
    na "Именно!"
    aik "Но ведь с тобой ничего не случилось. Ты была дома в тепле, сытая, одетая. Тебя просто ограничили в перемещении и связи."
    na "Ты не понимаешь! Неужели для тебя посягательство на свободу являются нормой?"
    show aizek angry at left2
    aik "Это было сделано только ради твоей безопасности!"
    na "Нет! Это было сделано просто, потому что отец так захотел, по его прихоти! Ты знаешь, как я отношусь к его псевдоаристократическим замашкам и вот этому «мы должны вести себя как достойная семья»."
    aik "Наоми, успокойся."
    show naomi angry at right2
    na "Ты знаешь, как я к этому отношусь! То, что мы являемся какими-то там потомками испанской аристократии, не дает ничего! Не дает ему права так поступать. А ты, зная все, просто рассказал ему все!"
    play sound "sounds/zvuk-padeniya-cheloveka-456.mp3"
    "Наоми толкает брата" #Звук толчка
    stop sound
    aik "Да успокойся ты! Его методы может и жестоки, но ты должна понимать, почему он так поступает!"
    na "Не понимаю и не хочу понимать!"
    play sound "sounds/shumnoe-rezkoe-padenie-s-vyisotyi.mp3"
    "Наоми толкает брата сильнее" #Звук сильного толчка. 
    "Разгоряченный алкоголем Айзек начинает закипать"
    stop sound
    aik "Да угомонись ты!"
    play sound "sounds/zvuk-upal.mp3"
    "Айзек толкает Наоми в ответ, не рассчитав силу"
    "Наоми падает, ударяясь головой об угол стола." #Звук удара/хруста черепа
    show aizek normal at left2
    aik "Наоми? Ты в порядке?"
    "Наоми не отвечает"
    #Конец флешбека

    scene bg vip_bar with dissolve #заменить
    gg "Охренеть…"
    show ghost upset with dissolve
    gh "Ты тоже это видел[verb_end]?"
    gg "Да." 
    gh "Судя по всему, именно так я и умерла." 
    gg "Что будем делать?"
    gh "Если честно, не знаю… С тех пор как я умерла, прошло пару дней. Если это все еще неизвестно, вероятно брат решил скрыть произошедшее."

    $ persistent.Naomi_flashback = True
    $ note_Naomi_flashback = True
    $ renpy.notify("В заметках появилась новая запись.")

    gg "Но, как так?"
    gh "Он вполне мог сказать родителям, что я просто сбежала. Он хозяин того бара, к тому же он обладает довольно обширными связями. Скрыть мою смерть не составило бы проблемы."
    gg "Не слишком ли поспешные выводы? Разве он не любил тебя?"
    gh normal "Любил, но себя он любит больше. Ты видел[verb_end] слишком мало, чтобы правильно оценить ситуацию."
    gg "Хорошо, я доверюсь тебе. Но вопрос о дальнейших действиях все еще открыт."
    show ghost normal dis with dissolve
    gg "Что происходит?"
    gh "Не знаю…"
    gh "[playerName]…"
    gg "Наоми!"
    gh "Видимо, на этом мой путь закончен."
    gg "Но мы ведь еще так мало сделали!"
    gh "Судя по всему, дальше тебе придется действовать в одиночку."

    if friendshp_gh > 8:
        if important1:
            gh "[playerName]… Я… не хочу, чтобы мое дело остановилось. Пожалуйста, продолжи его, стань новым таинственным художником."
            gg "Что? Но справлюсь ли я? Я давно не рисовал[verb_end], это очень ответственная задача."
            show ghost happy dis
            gh "Я верю в тебя. Рисование для тебя, как и для меня является чем-то очень важным. Преобрази этот город, ты справишься."
            gg "Хорошо."
            gh "Держи логин и пароль от моего аккаунта. И… спасибо тебе за все."
            hide ghost with dissolve
            gg "Наоми!"
        else:
            gh "[playerName], спасибо тебе за все. Ты очень сильно помог[past_verb_end] мне."
            gg "Наоми…"      
            gh "У меня есть просьба."
            gg "Какая?"
            gh "Не оставляй мою смерть безнаказанной. Из-за глупости брата мое дело прервалось. Я знаю, что своими граффити вдохновляла многих, но что будет с этими людьми теперь?"
            gh "Они ждали новой картины, для меня и моих подписчиков рисунки были очень важны."
            gg "Но что я могу сделать?"
            gh "Выведи всех на чистую воду: моего брата и тех, кто помог ему. Я дам тебе логин и пароль от своего аккаунта. Сообщи всем правду."
            gg "Но ведь у меня нет никаких доказательств."
            show ghost happy dis
            gh "К сожалению, мое время подходит к концу, я чувствую это. Я уверена, что ты со всем справишься. Ты куда сильнее, чем ты думаешь. Удачи…"
            hide ghost with dissolve

    else:
        gh "[playerName], я чувствую, что мое время подходит к концу…"
        gg "Постой, мы же еще не разобрались со всем до конца, я все еще не знаю, что произошло со мной!"
        gh "К сожалению, я ничем не могу помочь. Остатки моей жизни утекают сквозь пальцы. Спасибо тебе за помощь… и прощай."
        hide ghost with dissolve

        if not important1 and not important2:
            gg "И что мне теперь делать? Куда идти?"
            gg "И есть ли вообще во всем этом смысл…"
            #КОНЦОВКА: смерть

    $ persistent.Naomi_disappear = True

    jump act5_start
    return
