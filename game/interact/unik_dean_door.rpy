label unik_dean_door:
    if dean_door_click == 0:
        jump unik_dean_door1

    gg "Здесь больше ничего нет."

    jump act3_dean

label unik_dean_door1:
    show bg dean
    hide screen unikDean with dissolve

    show bg dean with pixellate
    show f_dean at right2 with dissolve
    f_dean "Николай Петрович, я понимаю ваше желание взять эту работу на конкурс, но мы {b}{color=#5f2626}не можем{/color}{/b} поощрять ее желание рисовать в импрессионизме."
    show f_np normal at left2 with dissolve
    f_np "Но это абсурд! Она талантлива, мы не можем все загубить! Если заставлять ее рисовать в том стиле, который ей не нравится, сами понимаете, это будет уже не то."
    f_dean "Вспомните, о чем нас {b}{color=#5f2626}попросили…{/color}{/b}"
    show f_np upset at left2
    f_np "Хорошо, я вас понял. Я сообщу ей об отказе в ближайшее время."
    
    hide f_dean with dissolve
    hide f_np with dissolve
    gg "Мне не нравится как это все звучит…"
    gh "Мне тоже."
    $ dean_door_click += 1
    $ friendshp_gh_temp += 2

    if count_canteen_interact == 1 and dean_door_click > 0:
        gg "Получается, ты рисовала в стиле импрессионизма и какой-то преподаватель хотел поддержать твое стремление и взять работу на конкурс."
        gh "Да, но кто-то {b}{color=#5f2626}попросил{/color}{/b} пресечь это…"
        gg "Мда, зреет что-то нехорошее"
        gh "И не говори"

    jump act3_dean