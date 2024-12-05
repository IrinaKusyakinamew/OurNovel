label estate_interact_door:
    "Дверь, за которой свобода"
    menu:
        "Хотите попробовать сбежать?"
        "Сбежать":
            play sound "sounds/create_character.mp3"
            $ k += 1
            hide screen estateHall
            jump act4_estate_room
        "Нет, это не в моих силах":
            play sound "sounds/create_character.mp3"
            jump act4_estate_hall
    return