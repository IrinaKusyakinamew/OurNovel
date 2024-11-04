label myScreens:

screen mapScreen:

    imagebutton:
        xpos 390
        ypos 390
        idle "obj1_idle.png"
        hover "obj1_hover.png"
        action [SetVariable("time", time + 1), Jump("chair")]

    imagebutton:
        xpos 310
        ypos 290
        idle "obj2_idle.png"
        hover "obj2_hover.png"
        action [SetVariable("time", time + 1), Jump("laptop")]

    imagebutton:
        xpos 984
        ypos 346
        idle "obj3_idle.png"
        hover "obj3_hover.png"
        action [SetVariable("time", time + 1), Jump("bed")]

    imagebutton:
        xpos 700
        ypos 500
        idle "obj4_idle.png"
        hover "obj4_hover.png"
        action [SetVariable("time", time + 1), Jump("trash")]

    # Добавляем голубую кнопку в этот же экран
    imagebutton:
        xalign 0.25
        yalign 0.95
        idle "blue_idle"
        hover "blue_hover"
        action [Hide('mapScreen'), SetVariable("time", time + 1), Jump("go_to_hall")]

screen barScreen:

    imagebutton:
        xpos 766
        ypos 289
        idle "bg bar_idle.jpg"
        hover "bg bar_hover.jpg"
        action [Hide('barScreen'), Jump("bar_inside")]