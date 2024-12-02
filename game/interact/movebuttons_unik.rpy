screen movebuttons_unik():
    if current_loc == "hall" or current_loc == "classes" or current_loc == "ladder":
        imagebutton:
            xalign 0.055
            yalign 0.76
            idle "images/buttons_interact/up_idle.png"
            hover "images/buttons_interact/up_hover.png"
            action Function(renpy.call, "move_unik_up")

    if current_loc == "hall" or current_loc == "ladder" or current_loc == "classes" or current_loc == "dean":
        imagebutton:
            xalign 0.006
            yalign 0.87
            idle "images/buttons_interact/left_idle.png"
            hover "images/buttons_interact/left_hover.png"
            action Function(renpy.call, "move_unik_left")

    if current_loc == "hall" or current_loc == "ladder" or current_loc == "canteen" or current_loc == "lecture":
        imagebutton:
            xalign 0.108
            yalign 0.87
            idle "images/buttons_interact/right_idle.png"
            hover "images/buttons_interact/right_hover.png"
            action Function(renpy.call, "move_unik_right")

    if current_loc == "ladder" or current_loc == "awards" or current_loc == "frescoes":
        imagebutton:
            xalign 0.055
            yalign 0.98
            idle "images/buttons_interact/down_idle.png"
            hover "images/buttons_interact/down_hover.png"
            action Function(renpy.call, "move_unik_down")