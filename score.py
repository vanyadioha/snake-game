from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("hs.txt") as hs_file:
            hs = hs_file.read()
            self.high_score = int(hs)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Courier", 16, "normal"),
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            with open("hs.txt", mode="w") as hsfile:
                hsfile.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
