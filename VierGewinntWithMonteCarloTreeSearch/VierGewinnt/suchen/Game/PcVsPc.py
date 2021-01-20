from suchen.Game.vierGewinnt import VierGewinnt as vg
import platform
import os
import suchen.Game.mcts as m
import time

if platform.system() == 'Linux':
    CLEAR = 'clear'
else:
    CLEAR = 'cls'

COMPUTER_ONE = "X"
COMPUTER_TWO = "O"

COMPUTER_ONE_ITERATIONS = 200
COMPUTER_TWO_ITERATIONS = 100

# seconds to wait till next turn is displayed to the human viwer
DISPLAY_SPEED = 3


class EvE():
    def __init__(self, cmd=False):
        self.game = vg()

        self.cmd = cmd
        if not self.cmd:
            self.welcome()

        self.game_controller()

    def welcome(self):
        os.system(CLEAR)

        print("\n \nVIER GEWINNT - can we beat us?\n")
        print("\nThe current number of iterations the algorithm will performe before decide for a turn is : \n")
        print(" (computer) " + COMPUTER_ONE + " : " + str(COMPUTER_ONE_ITERATIONS) + "\n")
        print(" (computer) " + COMPUTER_TWO + " : " + str(COMPUTER_TWO_ITERATIONS) + "\n\n")
        print(" display time is set to : " + str(DISPLAY_SPEED) + "\n")
        input("are you ready? (press enter or some other key) ")

    def game_controller(self):
        while not self.game.istSpielZuEnde():
            os.system(CLEAR)
            print(" ")
            self.game.printSpielfeld()
            self.game_info()

            mcts_pc_one = m.MCTS(vg=self.game, player_perspectiv=COMPUTER_ONE,
                                 iterations=COMPUTER_ONE_ITERATIONS)

            # fire up pc_one
            mcts_pc_one.start()

            self.game = mcts_pc_one.getBestZug()

            # i'm out
            if self.game.istSpielZuEnde():
                break

            if not self.cmd:
                time.sleep(DISPLAY_SPEED)

            os.system(CLEAR)
            print(" ")
            self.game.printSpielfeld()
            self.game_info()

            mcts_pc_two = m.MCTS(vg=self.game, player_perspectiv=COMPUTER_TWO,
                                 iterations=COMPUTER_TWO_ITERATIONS)

            # fire up pc_two
            mcts_pc_two.start()
            self.game = mcts_pc_two.getBestZug()

            # SLEEP
            if not self.cmd:
                time.sleep(DISPLAY_SPEED)

        os.system(CLEAR)
        print("\n")

        self.game.printSpielfeld()
        print("\ngame finished!")
        print("player won : " + str(self.game.getGewinner()))

    def game_info(self):
        if self.game.getAktuellerSpieler() == COMPUTER_ONE:
            print("\n                     [[computer :  " + COMPUTER_ONE + "]] (Turn)")
            print("\n                     [[computer :  " + COMPUTER_TWO + "]]")
        else:
            print("\n                     [[computer :  " + COMPUTER_ONE + "]]")
            print("\n                     [[computer :  " + COMPUTER_TWO + "]] (Turn)")


EvE()
