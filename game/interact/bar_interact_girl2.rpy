# Блок с описанием интерактивности в главном зале бара
label bar_interact_girl2:
    if girl_click == 0:
        "Красноволосая девушка" "Твоя идея - полный отстой!"
        "Рыжеволосая девушка" "Правда? А ты можешь предложить что-то получше? У нас нет денег."
        "Красноволосая девушка" "Я не стану разводить парней на коктейли."
        $ persistent.listen = True
        if persistent.listen_notify == 0:
            $ renpy.notify("Открыто новое достижение!")
            $ persistent.listen_notify += 1

        $ girl_click += 1
    "Девушки шепчутся."
    gg "Думаю, их лучше не тревожить"
    window hide
    jump bar_interact