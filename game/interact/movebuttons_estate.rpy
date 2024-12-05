screen movebuttons_estate():
    # if current_loc == "estate_balkon":
    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.76
    #         idle "images/buttons_interact/up_idle.png"
    #         hover "images/buttons_interact/up_hover.png"
    #         action Function(renpy.call, "move_estate_up")

    if current_loc == "estate_room" or current_loc == "estate_hall":
        imagebutton:
            xalign 0.006
            yalign 0.87
            idle "images/buttons_interact/left_idle.png"
            hover "images/buttons_interact/left_hover.png"
            action Function(renpy.call, "move_estate_left")

    if current_loc == "estate_kitchen" or current_loc == "estate_hall":
        imagebutton:
            xalign 0.108
            yalign 0.87
            idle "images/buttons_interact/right_idle.png"
            hover "images/buttons_interact/right_hover.png"
            action Function(renpy.call, "move_estate_right")

    if current_loc == "estate_hall" or current_loc == "estate_balkon":
        imagebutton:
            xalign 0.055
            yalign 0.98
            idle "images/buttons_interact/down_idle.png"
            hover "images/buttons_interact/down_hover.png"
            action Function(renpy.call, "move_estate_down")