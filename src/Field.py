from client.client import send_to_server
class Field:
    def __init__(self):
        self.turns = 0
        self.boxes = [[0,0,0],[0,0,0],[0,0,0]]
        self.game_over = False
        self.id = self.get_id()

    def get_id(self):
        send_to_server(b'get_id')

    def get_turns(self):
        return self.turns

    def turn(self,player,x,y):
        if(self.is_box_checked(x,y)==False):
            self.turns += 1
            self.boxes[x][y] = player
            return True
        else:
            return False

    def is_box_checked(self,x,y):
        if self.boxes[x][y] == 0:
            return False
        else:
            return True

    #TODO maybe obsolte
    def box_is_checked_by(self,x,y):
        return self.boxes[x][y]

    def has_player_won_horizontal(self,player):
        win = False
        i = 0
        while(i < len(self.boxes[0]) and not win):
            if(self.boxes[i][0] == player and
                    self.boxes[i][1] == player and
                    self.boxes[i][2] == player):
                win = True
                self.game_over = True
            else:
                i += 1

        return win

    def has_player_won_vertical(self,player):
        win = False
        i = 0
        while(i < len(self.boxes[0]) and not win):
            if(self.boxes[0][i] == player and
                    self.boxes[1][i] == player and
                    self.boxes[2][i] == player):
                win = True
                self.game_over = True
            else:
                i += 1

        return win


    def has_player_won_across(self, player):
        win = False

        if(self.boxes[0][0] == player and
            self.boxes[1][1] == player and
            self.boxes[2][2] == player):
            win = True
            self.game_over = True

        if (self.boxes[0][2] == player and
                self.boxes[1][1] == player and
                self.boxes[2][0] == player):
            win = True
            self.game_over = True

        return win

    def reached_max_turns(self):
        if (self.get_turns() == 9):
            self.game_over = True
            return True
        else:
            return False

    def is_game_over(self):
        self.print()
        return self.game_over

    def print(self):
        send_to_server(self)
        print(str(self.boxes[0][0])+""+str(self.boxes[0][1])+""+str(self.boxes[0][2]))
        print(str(self.boxes[1][0]) + "" + str(self.boxes[1][1]) + "" + str(self.boxes[1][2]))
        print(str(self.boxes[2][0]) + "" + str(self.boxes[2][1]) + "" + str(self.boxes[2][2]))