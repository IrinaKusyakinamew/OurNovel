screen movebuttons():
    if current_state == "bar_interact":
        imagebutton:
            xalign 0.055
            yalign 0.76
            idle "images/buttons_interact/up_idle.png"
            hover "images/buttons_interact/up_hover.png"
            action Function(renpy.call, "move_bar_up")

    if current_state == "bar_right" or current_state == "bar_interact":
        imagebutton:
            xalign 0.006
            yalign 0.87
            idle "images/buttons_interact/left_idle.png"
            hover "images/buttons_interact/left_hover.png"
            action Function(renpy.call, "move_bar_left")

    if current_state == "bar_left" or current_state == "bar_interact":
        imagebutton:
            xalign 0.108
            yalign 0.87
            idle "images/buttons_interact/right_idle.png"
            hover "images/buttons_interact/right_hover.png"
            action Function(renpy.call, "move_bar_right")

    if current_state == "bar_up":
        imagebutton:
            xalign 0.055
            yalign 0.98
            idle "images/buttons_interact/down_idle.png"
            hover "images/buttons_interact/down_hover.png"
            action Function(renpy.call, "move_bar_down")

