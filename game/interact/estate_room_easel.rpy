label estate_room_easel:
    if k < 2:
        menu:
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                hide screen estateRoom
                jump act4_continue
            "Им меня не сломить!":
                play sound "sounds/create_character.mp3"
                jump act4_estate_room
    if k == 2:
        menu:
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                hide screen estateRoom
                jump act4_continue
            "Им меня не сломить...":
                play sound "sounds/create_character.mp3"
                jump act4_estate_room
    if k >= 3:
        menu:
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                hide screen estateRoom
                jump act4_continue
            "Приступить к рисованию":
                play sound "sounds/create_character.mp3"
                hide screen estateRoom
                jump act4_continue

    return

