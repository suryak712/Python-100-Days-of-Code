import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)
df = pd.read_csv("50_states.csv")
states = df['state'].tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # states_missed = []
        # for state in states:
        #     if state not in guessed_states:
        #         states_missed.append(state)
        states_missed = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(states_missed)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df['state'] == answer_state]
        t.goto(state_data['x'].item(), state_data['y'].item())
        t.write(state_data['state'].item(), font=("Arial", 10, "bold"))


turtle.mainloop()