label estate_interact_door:
    "Дверь, за которой свобода"
    menu:
        "Что делать?"
        "Сбежать":
            play sound "sounds/create_character.mp3"
            $ k += 1
            hide screen estateHall
            jump freedom
        "Нет, это не в моих силах":
            play sound "sounds/create_character.mp3"
            jump act4_estate_hall
    return

label freedom:
    scene bg estate_hall with dissolve
    show guard with dissolve
    if k < 3:
        "Охранник" "Наоми, ваш отец запретил вам выходить. Давайте я отведу вас в комнату."
    else:
        "Охранник" "Наоми, это бесполезно. Пожалуйста прекратите."
    jump act4_estate_room