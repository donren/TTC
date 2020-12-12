import PySimpleGUI as sg
from src import Field
import random


box_row_1 = [sg.B(' ', size=(8, 4), key=(0, i)) for i in range(3)]
box_row_2 = [sg.B(' ', size=(8, 4), key=(1, i)) for i in range(3)]
box_row_3 = [sg.B(' ', size=(8, 4), key=(2, i)) for i in range(3)]
layout = [[sg.Text('                    ',key='-playername-'),sg.Text(' ',key='-marker-')],
        box_row_1,
        box_row_2,
        box_row_3]


window = sg.Window('Tic Tac Toe', layout,finalize=True)
open_window = True
def reset_gui(window):
    for i in range(3):
        for j in range(3):
            window[(i,j)].update('')

def update_player_text(window,player):
    window['-playername-'].update(get_player_name(player))
    window['-marker-'].update(get_marker(player))

def get_player_name(player):
    if player == 1:
        return 'Maus'
    if player == 2:
        return 'Klaus'

def get_marker(player):
    if player == 1:
        return 'X'
    if player == 2:
        return '0'

def switch_player(player):
    if player == 1:
        return  2
    elif player == 2:
        return  1

while open_window:
    ttt = Field.Field()
    player = random.randint(1,2)
    sg.Popup('{} ({}) starts'.format(get_player_name(player),get_marker(player)), title='Poup')
    while ttt.is_game_over() == False:             # Event Loop
        choice=""
        update_player_text(window, player)
        event, values = window.read()
        print(event, values)
        successful = ttt.turn(player,event[0],event[1])

        if successful:
            #update checkbox
            window[event].update(get_marker(player))

            #check for victotry
            if(ttt.has_player_won_across(player) or
            ttt.has_player_won_horizontal(player) or
            ttt.has_player_won_vertical(player) ):
                choice = sg.popup_yes_no("victory:{} ({})".format(get_player_name(player), get_marker(player)),
                                       title='Poup')
            #check for max turns
            if ttt.reached_max_turns():
                choice == sg.popup_yes_no("draw", get_marker(player),
                                       title='Poup')


            if(choice=="No"):
                open_window = False

            #switch player
            player = switch_player(player)

        if event in (None, 'Exit'):
            open_window = False

    reset_gui(window)

window.close()