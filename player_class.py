class Player:

    def __init__(self, name: str, score: int = 0) -> None:
        self.name = name
        self.score = score

    def increase_score(self) -> None:
        self.score += 1
