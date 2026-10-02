from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock', 0), ('paper', 1) ('scissors', 3)]

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text = "Computer Won!!!")
    computer_score_label.config(text = 'Computer Score : ' + str(computer_score))
    player_score_label.config(text = 'Player Score : ') + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score += 1
    winner_label.config(text = "Player Won!!!")
    computer_score_label.config(text = 'Computer Score: ' + str(computer_score))
    player_score_label.config(text = 'Player Score: ' + str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text = "Tie!!!")
    computer_score_label.config(text = 'Computer Score: ' + str(computer_score))
    player_score_label.config(text = 'Player Score: ' + str(player_score))

def player_choice(player_input):
    global player_score, computer_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer input)
    player_choice_label.config(text = 'Your selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer selected : ' + computer_input[0])

    if (player_input == computer_input):
        tie()
