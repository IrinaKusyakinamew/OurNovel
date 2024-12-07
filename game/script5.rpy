label act5_start:
    # гг просыпается в больнице 
    stop music fadeout 2
    play music1 "music/Not Giving Up.ogg" fadein 2
    scene bg hospital with dissolve
    gg "Где я? Больница? Неужели все, что произошло это просто сон?"
    show nurse with dissolve
    nu "Здравствуйте, [playerName]. Рада, что вы очнулись."
    gg "Что со мной случилось?"
    nu "Насколько мне известно, вы отдыхали в баре с другом и вам стало плохо. У вас случилась передозировка наркотическими веществами и вы впали в кому на несколько дней."
    gg "Что?! Но я ничего не принимал[verb_end]!"
    nu "Я сужу по вашим анализам крови. Вам нужно отдыхать."
    hide nurse with dissolve
    gg "Черт… Неужели это все было просто игрой моего воображения…"
    gg "Нет! Я не хочу в это верить."
    gg "Точно, я же делал[verb_end] заметки в телефон. Надо проверить его."
    "[playerName] достает телефон, смотрит"
    gg "Все заметки на месте. Значит… все-таки это был не сон. Фух."
    
    show expression fr_normal with dissolve
    fr "[playerName]! Я так рад[verb_end], что ты в порядке! Столько всего произошло…"
    gg "Медсестра сказала, что у меня случился передоз. Не хочешь объясниться?"
    show expression fr_uncomprehending
    hide fr_normal
    fr "Ну… Я попросил[verb_end] бармена немного «разбавить» твой напиток. Я просто хотел[verb_end], чтобы разговор шел легче, я не думал[verb_end], что этот дебил переборщит и тебе станет плохо!"

    if important2:
        gg "Что ты сделал[verb_end]?! Убирайся! Видеть тебя больше не хочу!"
        fr "Но…"
        gg "ИДИ ОТСЮДА!"
        hide fr_uncomprehending with dissolve
        "Прошло несколько месяцев с этих событий."

        if not important1:
            jump ending_third
        elif friendshp_gh >= 8:
            jump ending_second
        else:
            jump ending_fifth

    else:
        gg "Я… мне сложно это принять. Мне нужно время."
        fr "Прости пожалуйста, я правда не хотел[verb_end]."
        gg "Я хочу отдохнуть, давай поговорим позже."
        fr "Хорошо."
        hide fr_uncomprehending with dissolve
        "Прошло несколько месяцев с этих событий."

        if not important1:
            jump ending_sixth
        else:
            jump ending_fourth


label ending_second:
    scene bg painter_1 with dissolve
    gg ```
    Я подтянул[verb_end] свои навыки рисования.
    
    Я исполнил[verb_end] желание Наоми и продолжил[verb_end] ее дело.

    У меня появились друзья и фанаты, люди, которым я дорог[verb_end].
    
    Вскоре у меня получилось снять квартиру, мне больше не нужно жить в грязной общаге.
    ```
    if jos:
        scene ending2jos with dissolve
        $ persistent.ending2jos = True
        if persistent.jos_notify == 0:
            $ renpy.notify("Открыто новое достижение!")
            $ persistent.jos_notify += 1
        pause
        gg "На днях ко мне на улице прибился черный кот. Не знаю, что с ним делать, но пока что он живет у меня. Я решил[verb_end] назвать его Йосей."
    
    if gender_symbol == "♂":
        $ persistent.ending2b = True
        scene ending2b with fade
    else:
        $ persistent.ending2g = True
        scene ending2g with fade
    pause

    "Чувствую, что все теперь будет хорошо."
    "Спасибо, Наоми…"

    show the_end with fade
    pause

    return


label ending_third:
    scene bg detective with dissolve
    gg ```
    У меня получилось найти работу и съехать с общаги.

    Я продолжаю свое расследование.

    Все оказалось куда сложнее, чем ожидалось.

    В городе орудует крупная преступная организация, в которую входят и Айзек и моя бывшая компания друзей. Хорошо, что я больше не доверяю им.
    ```
    if jos:
        scene ending2jos with dissolve
        $ persistent.ending2jos = True
        if persistent.jos_notify == 0:
            $ renpy.notify("Открыто новое достижение!")
            $ persistent.jos_notify += 1
        pause
        gg "На днях ко мне на улице прибился черный кот. Не знаю, что с ним делать, но пока что он живет у меня. Я решил[verb_end] назвать его Йосей."

    if gender_symbol == "♂":
        $ persistent.ending3b = True
        scene ending3b with fade
    else:
        $ persistent.ending3g = True
        scene ending3g with fade
    pause

    "Наоми… Твоя смерть не останется безнаказанной."
    "Спи спокойно…"

    show the_end with fade
    pause

    return

label ending_fourth:

    if gender_symbol == "♂":
        $ persistent.ending4b = True
        scene ending4b with fade
    else:
        $ persistent.ending4g = True
        scene ending4g with fade
    pause

    gg ```
    Я решил[verb_end] продолжить дело Наоми.

    Я рассказал[verb_end] о таинственном художнике другу, избегая околомистических подробностей.

    Мне кажется, [friendPronoun] эта новость обрадовала.

    Он[verb_end] предложил[verb_end] использовать полученный тг канал для некоторой рекламы. 

    Я поддержал[verb_end] [friendPronoun] решение. Теперь помимо новых граффити и постов с рассуждениями о жизни периодически «таинственный художник» дает подписчикам советы о том, как и где можно «расслабиться».

    Эти действия повлияют на многие жизни. Но волнует ли это меня…?
    ```

    show the_end with fade
    pause

    return

label ending_fifth:
    scene bg painter_2 with dissolve

    gg ```
    Прошло несколько месяцев с этих событий.

    Я подтянул[verb_end] свои навыки рисования и смог[past_verb_end] найти работу по душе.

    Я съехал[verb_end] с общаги в неплохую квартиру.
    ```
    if jos:
        scene ending2jos with dissolve
        $ persistent.ending2jos = True
        if persistent.jos_notify == 0:
            $ renpy.notify("Открыто новое достижение!")
            $ persistent.jos_notify += 1
        pause
        gg "На днях ко мне на улице прибился черный кот. Не знаю, что с ним делать, но пока что он живет у меня. Я решил[verb_end] назвать его Йосей."

    if gender_symbol == "♂":
        $ persistent.ending5b = True
        scene ending5b with fade
    else:
        $ persistent.ending5g = True
        scene ending5g with fade
    pause

    "Все не так уж и плохо, впереди целая жизнь…"

    show the_end with fade
    pause

    return

label ending_sixth:
    scene bg detective with dissolve

    gg ```
    Наоми просила меня не оставлять свою смерть безнаказанной. Но все оказалось куда сложнее, чем предполагалось.

    Я рассказал о Наоми другу, избегая околомистических подробностей.

    Оказалось, в городе орудует крупная преступная организация, в которую входят и Айзек и моя компания друзей. 

    Им очень не понравилось, что я решил[verb_end] под них копать.

    Однажды [friendName] позвал[verb_end] меня выпить в баре.
    ```
    if gender_symbol == "♂":
        $ persistent.ending6b = True
        scene ending6b with fade
    else:
        $ persistent.ending6g = True
        scene ending6g with fade
    pause

    "Домой я не верну[past_end]…"

    show the_end with fade
    pause

    return

    
    # 1)	ЕСЛИ ГГ НЕ ПОДДЕРЖИВАЛ КОМПАНИЮ:
    # ЕСЛИ ГГ ВЫБРАЛ РИСОВАТЬ ПРИ ХОРОШИХ ОТНОШЕНИЯХ С НАОМИ:
    #     КОНЦОВКА: таинственный художник (есть) 2 + йос
    # ЕСЛИ ГГ ВЫБРАЛ НЕ РИСОВАТЬ ПРИ ХОРОШИХ ОТНОШЕНИЯХ С НАОМИ:
    #     КОНЦОВКА: юный детектив (есть) 3 + йос
    # ЕСЛИ ГГ ВЫБРАЛ РИСОВАТЬ ПРИ ПЛОХИХ ОТНОШЕНИЯХ С НАОМИ:
    #     КОНЦОВКА: все не так плохо 5 + йос
    # 2)	ЕСЛИ ГГ ПОДДЕРЖИВАЛ КОМПАНИЮ:
    #         ЕСЛИ ГГ ВЫБРАЛ РИСОВАТЬ ПРИ ХОРОШИХ ОТНОШЕНИЯХ С НАОМИ:
    #             КОНЦОВКА: криминальный терпила (есть) 4
    #         ЕСЛИ ГГ ВЫБРАЛ НЕ РИСОВАТЬ ПРИ ХОРОШИХ ОТНОШЕНИЯХ С НАОМИ:
    #             КОНЦОВКА: мертвый детектив 6