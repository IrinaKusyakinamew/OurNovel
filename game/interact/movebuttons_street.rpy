screen movebuttons_street():
    if current_loc == "street_front" or current_loc == "street_down":
        imagebutton:
            xalign 0.055
            yalign 0.76
            idle "images/buttons_interact/up_idle.png"
            hover "images/buttons_interact/up_hover.png"
            action Function(renpy.call, "move_street_up")

    if current_loc == "street_right" or current_loc == "street_front":
        imagebutton:
            xalign 0.006
            yalign 0.87
            idle "images/buttons_interact/left_idle.png"
            hover "images/buttons_interact/left_hover.png"
            action Function(renpy.call, "move_street_left")

    if current_loc == "street_left" or current_loc == "street_front":
        imagebutton:
            xalign 0.108
            yalign 0.87
            idle "images/buttons_interact/right_idle.png"
            hover "images/buttons_interact/right_hover.png"
            action Function(renpy.call, "move_street_right")

    if current_loc == "street_up" or current_loc == "street_front":
        imagebutton:
            xalign 0.055
            yalign 0.98
            idle "images/buttons_interact/down_idle.png"
            hover "images/buttons_interact/down_hover.png"
            action Function(renpy.call, "move_street_down")