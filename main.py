import turtle
import pandas as pd
from state import State

screen = turtle.Screen()
screen.title("India State Guessing Game")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

state_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

data = pd.read_csv("28_states.csv")
states = data["state"].to_list()
x_s = data["x"].to_list()
y_s = data["y"].to_list()

guess_state = 0
guessed_states = []

while guess_state != 28:
    
    if state_answer == "Exit":
        missing_states= []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if state_answer in states and state_answer not in guessed_states:
        position = states.index(state_answer)
        guess_state += 1
        state = State(x_s[position], y_s[position], state_answer)
        guessed_states.append(state_answer)
    
    state_answer = screen.textinput(title=f"{guess_state}/28 States Correct", prompt="What's another state's name?").title()

