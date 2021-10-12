from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
         super().__init__()
         self.score = 0
         with open("data.txt") as data:
             self.hight_score = int(data.read())
         self.penup()
         self.color("white")
         self.goto(0, 270)
         self.hideturtle()
         self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} Hight Score:{self.hight_score}", align=ALIGMENT, font=FONT)



    def reset(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.hight_score}")

        self.score = 0


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGMENT, font=FONT)

    def insrease_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


