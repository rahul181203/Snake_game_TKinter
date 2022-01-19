import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('DAY-20 & DAY - 21\data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Arial",24,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('DAY-20 & DAY - 21\data.txt',mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",align="center",font=("Arial",24,"normal"))
    #     self.goto(0,100)
    #     self.write(f"Your final Score is : {self.score}",align="center",font=("Arial",24,"normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()