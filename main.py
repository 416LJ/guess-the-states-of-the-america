import turtle as t
import pandas as pd

states_data = pd.read_csv("50_states.csv")
states = list(states_data.state)
states_known = []
screen = t.Screen()
image = "blank_states_img.gif"
screen.title("GUESS THE STATES OF THE U.S.A")
screen.addshape(image)
t.penup()
t.shape(image)
correct_guesses = 0
game_is_on = True
wrong_answer = t.Turtle()
wrong_answer.penup()
wrong_answer.hideturtle()
wrong_ans = 10
def check_ans():
    wrong_answer.clear()
    wrong_answer.goto(x=0, y=-300)
    wrong_answer.write(arg=f"The State '{answer}' is not in the USA.", font=('Ariel', 24, 'bold'),
                       align="center", move=False)
    wrong_answer.goto(x=0, y=-350)

    wrong_answer.write(arg=f"Guess Again", font=('Ariel', 24, 'bold'),
                       align="center", move=False)

while game_is_on:
    answer = screen.textinput(prompt=f"GUESS ANOTHER STATE", title=f"GUESS A STATE : {correct_guesses}/{len(states)} : Turns left : {wrong_ans}").title()
    if answer == "Exit":
        exit()
    if answer in states:
        states_known.append(answer)
        wrong_answer.clear()
        location_x = float(states_data[states_data.state == answer].x)
        location_y = float(states_data[states_data.state == answer].y)
        locater_turtle = t.Turtle()
        locater_turtle.penup()
        locater_turtle.hideturtle()
        locater_turtle.goto(location_x,location_y)
        locater_turtle.write(arg=f"{answer}", font=('Ariel', 12, 'bold'),
                   align="center", move=False)
        wrong_answer.goto(x=0,y=-350)
        wrong_answer.write(arg=f"Correct, The State '{answer}' is in the USA.", font=('Ariel', 24, 'bold'),
                           align="center", move=False)
        correct_guesses += 1
    else:
        wrong_ans -= 1
        check_ans()

    if correct_guesses == len(states) or wrong_ans == 0:
        game_is_on = False

screen.clear()
final_msg = t.Turtle()
final_msg.penup()
final_msg.hideturtle()

if correct_guesses == len(states):
    final_msg.write(arg=f"You Guessed All the States. Great Job.", font=('Ariel', 30, 'bold'),
                     align="center", move=False)
if wrong_ans == 0:
    final_msg.write(arg=f"You ran out of tries.", font=('Ariel', 30, 'bold'),
                    align="center", move=False)
    unknown_states = list(set(states) - set(states_known))
    new_data = pd.DataFrame(unknown_states)
    new_data.to_csv("states_to_learn.csv")
t.mainloop()


