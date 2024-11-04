screen movebuttons():
    imagebutton:
        xalign 0.055
        yalign 0.76
        idle "up_idle.png"
        hover "up_hover.png"
        action Function(renpy.call, "move_bar_up")

    imagebutton:
        xalign 0.006
        yalign 0.87
        idle "left_idle.png"
        hover "left_hover.png"
        action Function(renpy.call, "move_bar_left")

    imagebutton:
        xalign 0.108
        yalign 0.87
        idle "right_idle.png"
        hover "right_hover.png"
        action Function(renpy.call, "move_bar_right")

    imagebutton:
        xalign 0.055
        yalign 0.98
        idle "down_idle.png"
        hover "down_hover.png"
        action Function(renpy.call, "move_bar_down")

