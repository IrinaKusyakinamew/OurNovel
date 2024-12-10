class Stats():
    """отслеживание статистики текущей игры"""

    def __init__(self):
        """инициализация статистики"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """статистика, меняющаяся во время игры"""
        self.guns_left = 3
        self.score = 0

