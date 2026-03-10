from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_Score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}       High Score: {self.high_Score}", move=False, align="center" , font=("Arial", 18, "normal"))

    def score_increase(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_Score:
            self.high_Score = self.score
        self.score = 0
        self.update_score()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("Game Over", move=False, align="center", font=("Arial", 32, "normal"))
        

