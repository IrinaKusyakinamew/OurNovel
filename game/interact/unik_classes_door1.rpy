label unik_classes_door1:
    # ВСТАВИТЬ НУЖНЫЙ ТЕКСТ
    menu:
        "Внимание! Если вы зайдете внутрь, то больше не сможете исследовать локации университета"
        "Зайти в кабинет искусства":
            hide screen unikClasses
            jump act3_flashback_start
        "Пока не заходить":
            jump act3_classes 