import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
screen = turtle.Screen()
screen.setup(750, 500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

all_states = []

while len(all_states) < 50:
    answer = screen.textinput(title=f"{len(all_states)}/50 Guess a State", prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_state = [state for state in states if state not in all_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        set_data = data[data.state == answer]
        t.goto(int(set_data.x), int(set_data.y))
        t.write(answer, align=ALIGNMENT, font=FONT)
        all_states.append(answer)
