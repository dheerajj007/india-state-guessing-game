from turtle import Turtle
FONT = ("Courier", 9, "normal")

class State(Turtle):

    def __init__(self, x, y, text):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x, y)
        self.write(text, align="center", font=FONT)
