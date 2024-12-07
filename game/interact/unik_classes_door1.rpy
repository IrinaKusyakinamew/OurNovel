label unik_classes_door1:
    if friendshp_gh_temp == 5:
        menu:
            "Вы нашли все возможное на это локации. Зайдя в кабинет, вы больше не сможете ходить по локациям университета"
            "Зайти в кабинет искусства":
                $ friendshp_gh += friendshp_gh_temp
                $ renpy.notify(f"Отношения с персонажем Призрак значительно улучшились")

                gh "Я рада, что мы столько осмотрели"

                $ persistent.history = True
                if persistent.history_notify == 0:
                    $ renpy.notify("Открыто новое достижение!")
                    $ persistent.history_notify += 1
                    gg "Полный обход занял довольно много времени"

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
                    gh "Жаль, что мы почти ничего не нашли"
                else:
                    $ renpy.notify(f"Отношения с персонажем Призрак улучшились")
                    gh "Хорошо, что мы смогли что-то найти"

                hide screen unikClasses
                jump act3_flashback_start
            "Пока не заходить":
                jump act3_classes 

