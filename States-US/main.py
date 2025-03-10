import turtle
import pandas
from score import Score
game_score= Score()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")

guessed_states = []

while True:
    answer_state = screen.textinput(title="Guess the State",
                                    prompt="What is the name of the state (or type 'Exit' to quit)").capitalize()

    if answer_state == "Exit":
        break  # Exit loop if user types Exit

    if (states["state"] == answer_state).any() and answer_state not in guessed_states:
        guessed_states.append(answer_state)  # Add to guessed list
        state_info = states[states.state == answer_state]
        x = state_info.x.item()
        y = state_info.y.item()

        # Create a new turtle for writing each state
        state_writer = turtle.Turtle()
        state_writer.hideturtle()  # Hide the turtle icon
        state_writer.penup()
        state_writer.goto(y, x)  # Coordinates are (y, x) as per your file
        state_writer.write(state_info.state.item(), align="center", font=("Arial", 8, "normal"))
        game_score.increase_score()
    else:
        print("wrong or already guessed")

screen.exitonclick()
