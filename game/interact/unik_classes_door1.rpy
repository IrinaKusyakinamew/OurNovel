label unik_classes_door1:
    if friendshp_gh_temp == 5:
        menu:
            "Вы нашли все возможное на это локации. Зайдя в кабинет, вы больше не сможете ходить по локациям университета"
            "Зайти в кабинет искусства":
                $ friendshp_gh += friendshp_gh_temp
                $ renpy.notify(f"Отношения с персонажем Призрак значительно улучшились")

                $ persistent.history = True
                if persistent.history_notify == 0:
                    $ renpy.notify("Открыто новое достижение!")
                    $ persistent.history_notify += 1

                hide screen unikClasses
                jump act3_flashback_start
            "Пока не заходить":
                jump act3_classes 

    else:
        menu:
            "Внимание! Вы не полностью исследовали локацию. Если вы зайдете внутрь, то больше не сможете исследовать локации университета. Вы уверены, что хотите зайти?"
            "Зайти в кабинет искусства":
                $ friendshp_gh += friendshp_gh_temp
                if friendshp_gh_temp == 0:
                    $ friendshp_gh -= 3
                    $ renpy.notify(f"Отношения с персонажем Призрак ухудшились")
                else:
                    $ renpy.notify(f"Отношения с персонажем Призрак улучшились")

                hide screen unikClasses
                jump act3_flashback_start
            "Пока не заходить":
                jump act3_classes 