# Блок с описанием интерактивности в центральной части улицы
label ghost:
    # ВСТАВИТЬ НУЖНЫЙ ТЕКСТ

    if count_act2_front_pred <= 1:
        menu:
            "Подойти к призраку":
                play sound "sounds/create_character.mp3"
                "Я пока ничего не нашла, подойди попозже."

                # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ
                window hide
                jump act2_front
            "Не отвлекать призрака":
                play sound "sounds/create_character.mp3"
                # ВСТАВИТЬ НУЖНЫЕ РЕПЛИКИ
                window hide
                jump act2_front

    else:
        menu:
            "Внимание, если вы подойдете к призраку, то покинете локацию"
            "Подойти к призраку":
                play sound "sounds/create_character.mp3"
                hide screen streetFront
                gh "[playerName], cмотри, тут лежит чья-то сумка."
                gg "Хм, стоит осмотреть."


                jump act2_bag
            "Не отвлекать призрака":
                play sound "sounds/create_character.mp3"
                window hide
                jump act2_front
