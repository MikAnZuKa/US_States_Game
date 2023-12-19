import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

#checking if answer state is among states in csv file
guessed_state = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 guessed states", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #pulling out right row in order to get coords
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
