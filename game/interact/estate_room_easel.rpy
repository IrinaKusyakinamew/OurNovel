label estate_room_easel:
    if k == 1:
        menu:
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                jump act4_continue
            "Нет, я буду сопротивляться до конца!":
                play sound "sounds/create_character.mp3"
                jump act4_estate_room
    if k == 2:
        menu:
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                jump act4_continue
            "Им меня не сломить!":
                play sound "sounds/create_character.mp3"
                jump act4_estate_room
    if k == 3:
        menu:
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                jump act4_continue
            "Им меня не сломить...":
                play sound "sounds/create_character.mp3"
                jump act4_estate_room
    if k == 4:
        menu:
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                jump act4_continue
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                jump act4_continue

    return

