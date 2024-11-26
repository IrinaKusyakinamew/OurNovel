screen movebuttons_gallery():
    if current_loc == "gallery_front" or current_loc == "gallery_down":
        imagebutton:
            xalign 0.055
            yalign 0.76
            idle "images/buttons_interact/up_idle.png"
            hover "images/buttons_interact/up_hover.png"
            action Function(renpy.call, "move_gallery_up")

    if current_loc == "gallery_right" or current_loc == "gallery_front":
        imagebutton:
            xalign 0.006
            yalign 0.87
            idle "images/buttons_interact/left_idle.png"
            hover "images/buttons_interact/left_hover.png"
            action Function(renpy.call, "move_gallery_left")

    if current_loc == "gallery_left" or current_loc == "gallery_front":
        imagebutton:
            xalign 0.108
            yalign 0.87
            idle "images/buttons_interact/right_idle.png"
            hover "images/buttons_interact/right_hover.png"
            action Function(renpy.call, "move_gallery_right")

    if current_loc == "gallery_up" or current_loc == "gallery_front":
        imagebutton:
            xalign 0.055
            yalign 0.98
            idle "images/buttons_interact/down_idle.png"
            hover "images/buttons_interact/down_hover.png"
            action Function(renpy.call, "move_gallery_down")
    # if current_loc == "gallery_front":
    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.76
    #         idle "images/buttons_interact/up_idle.png"
    #         hover "images/buttons_interact/up_hover.png"
    #         action Function(renpy.call, "move_gallery_up")

    #     imagebutton:
    #         xalign 0.006
    #         yalign 0.87
    #         idle "images/buttons_interact/left_idle.png"
    #         hover "images/buttons_interact/left_hover.png"
    #         action Function(renpy.call, "move_gallery_left")

    #     imagebutton:
    #         xalign 0.108
    #         yalign 0.87
    #         idle "images/buttons_interact/right_idle.png"
    #         hover "images/buttons_interact/right_hover.png"
    #         action Function(renpy.call, "move_gallery_right")

    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.98
    #         idle "images/buttons_interact/down_idle.png"
    #         hover "images/buttons_interact/down_hover.png"
    #         action Function(renpy.call, "move_gallery_down")
    
    # elif current_loc == "gallery_up":
    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.76
    #         idle "images/buttons_interact/up_idle.png"
    #         hover "images/buttons_interact/up_idle.png"
    #         action Function(renpy.call, "move_gallery_up")

    #     imagebutton:
    #         xalign 0.006
    #         yalign 0.87
    #         idle "images/buttons_interact/left_idle.png"
    #         hover "images/buttons_interact/left_idle.png"
    #         action Function(renpy.call, "move_gallery_left")

    #     imagebutton:
    #         xalign 0.108
    #         yalign 0.87
    #         idle "images/buttons_interact/right_idle.png"
    #         hover "images/buttons_interact/right_idle.png"
    #         action Function(renpy.call, "move_gallery_right")

    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.98
    #         idle "images/buttons_interact/down_idle.png"
    #         hover "images/buttons_interact/down_hover.png"
    #         action Function(renpy.call, "move_gallery_down")

    # elif current_loc == "gallery_right":
    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.76
    #         idle "images/buttons_interact/up_idle.png"
    #         hover "images/buttons_interact/up_idle.png"
    #         action Function(renpy.call, "move_gallery_up")

    #     imagebutton:
    #         xalign 0.006
    #         yalign 0.87
    #         idle "images/buttons_interact/left_idle.png"
    #         hover "images/buttons_interact/left_hover.png"
    #         action Function(renpy.call, "move_gallery_left")

    #     imagebutton:
    #         xalign 0.108
    #         yalign 0.87
    #         idle "images/buttons_interact/right_idle.png"
    #         hover "images/buttons_interact/right_idle.png"
    #         action Function(renpy.call, "move_gallery_right")

    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.98
    #         idle "images/buttons_interact/down_idle.png"
    #         hover "images/buttons_interact/down_idle.png"
    #         action Function(renpy.call, "move_gallery_down")

    # elif current_loc == "gallery_left":
    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.76
    #         idle "images/buttons_interact/up_idle.png"
    #         hover "images/buttons_interact/up_idle.png"
    #         action Function(renpy.call, "move_gallery_up")

    #     imagebutton:
    #         xalign 0.006
    #         yalign 0.87
    #         idle "images/buttons_interact/left_idle.png"
    #         hover "images/buttons_interact/left_idle.png"
    #         action Function(renpy.call, "move_gallery_left")

    #     imagebutton:
    #         xalign 0.108
    #         yalign 0.87
    #         idle "images/buttons_interact/right_idle.png"
    #         hover "images/buttons_interact/right_hover.png"
    #         action Function(renpy.call, "move_gallery_right")

    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.98
    #         idle "images/buttons_interact/down_idle.png"
    #         hover "images/buttons_interact/down_idle.png"
    #         action Function(renpy.call, "move_gallery_down")

    # else:
    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.76
    #         idle "images/buttons_interact/up_idle.png"
    #         hover "images/buttons_interact/up_hover.png"
    #         action Function(renpy.call, "move_gallery_up")

    #     imagebutton:
    #         xalign 0.006
    #         yalign 0.87
    #         idle "images/buttons_interact/left_idle.png"
    #         hover "images/buttons_interact/left_idle.png"
    #         action Function(renpy.call, "move_gallery_left")

    #     imagebutton:
    #         xalign 0.108
    #         yalign 0.87
    #         idle "images/buttons_interact/right_idle.png"
    #         hover "images/buttons_interact/right_idle.png"
    #         action Function(renpy.call, "move_gallery_right")

    #     imagebutton:
    #         xalign 0.055
    #         yalign 0.98
    #         idle "images/buttons_interact/down_idle.png"
    #         hover "images/buttons_interact/down_idle.png"
    #         action Function(renpy.call, "move_gallery_down")