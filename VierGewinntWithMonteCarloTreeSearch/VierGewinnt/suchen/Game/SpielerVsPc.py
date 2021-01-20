from suchen.Game.vierGewinnt import VierGewinnt as vg
import platform
import os
import suchen.Game.mcts as m

COMPUTER_TWO = "O"

if platform.system() == 'Linux':
    CLEAR = 'clear'
else:
    CLEAR = 'cls'


class PvE:
    def __init__(self, skip_welcome=False):
        self.game = vg()
        if not skip_welcome:
            self.welcome()

        self.game_controller()

    def welcome(self):
        os.system(CLEAR)

        print("\n\nVIER GEWINNT - can you beat me?\n")
        print("\nThe current number of iterations the algorithm will performe before decide for a turn is : " + str(
            m.MAX_ITERATIONS) + "\n\n")
        input("are you ready? (press enter or some other key) ")

    def game_controller(self):
        while not self.game.istSpielZuEnde():
            os.system(CLEAR)

            print("\n")
            self.game.printSpielfeld()
            possible_turns = self.game.getMoeglicheSpalten()

            self.game_info()
            i_int, is_valid = self.is_valid_input(input("\n\nyour move! choose a position > "), possible_turns)
            self.game_info()
            # funny bug, while loop behavior 0 and 1-6 as boolean
            while not is_valid:
                os.system(CLEAR)
                print("\n")
                self.game.printSpielfeld()
                self.game_info()
                print("input was not valid, try again")
                i_int, is_valid = self.is_valid_input(input("\nyour move! choose a position > "), possible_turns)

            self.game.setSpielzug(i_int)

            # i'm out
            if self.game.istSpielZuEnde():
                break

            mcts = m.MCTS(self.game, player_perspectiv=COMPUTER_TWO)
            mcts.start()
            self.game = mcts.getBestZug()

        os.system(CLEAR)
        print("\n")
        self.game.printSpielfeld()
        print("\ngame finished!")
        print("player won : " + str(self.game.getGewinner()))

    def is_valid_input(self, user_input, possible_turns):
        try:
            user_input_int = int(user_input)
        except ValueError:
            return (None, False)

        if user_input_int >= 7 or user_input_int <= -1 or not user_input_int in possible_turns:
            return (None, False)
        else:
            return (user_input_int, True)

    def game_info(self):
        print("\n                       [[human    :  p1]]")
        print("                       [[computer :  p2]]")


PvE()