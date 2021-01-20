import copy as c
import math as m
from anytree import *
from anytree.exporter import DotExporter as d
from graphviz import Source
from suchen.Game.vierGewinnt import VierGewinnt as vg

MAX_ITERATIONS = 400


X_SPIELER = "X"
O_SPIELER = "O"

class MCTS:
    def __init__(self, vg=vg(), player1=X_SPIELER, player2=O_SPIELER, player_perspectiv=X_SPIELER,
                 iterations=MAX_ITERATIONS):
        self.player1 = player1
        self.player2 = player2
        self.root = self.initNode(vg)
        self.aktuellerKnoten = self.root
        self.player_perspectiv = player_perspectiv
        self.iterations = iterations
        self.i = 0

    def edgeattrfunc(node, child):
        return 'label="w=%sn=%s:w=%s,n=%s"' % (
            node.__getattribute__("w"), node.__getattribute__("n"), child.__getattribute__("w"),
            child.__getattribute__("n"))

    def initNode(self, game, parent=None):
        node = Node(game.__str__(), parent)
        node.__setattr__("game", game)
        node.__setattr__("n", 0)
        node.__setattr__("w", 0)
        node.__setattr__("ucb", None)
        return node

    def start(self):
        for x in range(1, self.iterations):
            self.selection()
            # if x == 20:
            # d(self.root).to_dotfile("Test.dot")
            self.aktuellerKnoten = self.root

    def getSpiel(self):
        return self.aktuellerKnoten.__getattribute__("game")

    def setSpiel(self, game):
        self.aktuellerKnoten.__setattr__("game", game)

    def getN(self):
        return self.aktuellerKnoten.__getattribute__("n")

    def setChild(self, game):
        self.initNode(game, parent=self.aktuellerKnoten)

    def selection(self):
        if self.aktuellerKnoten.is_leaf:
            if self.getN() == 0:
                self.simulation()
            else:
                # if self.i % 6 == 0:
                #     str = ""
                #     # d(self.root).to_dotfile("Graphen/Test" + self.i.__str__() + ".dot")
                #     # render('dot', 'png', 'Datei/Test0')
                #     for line in d(self.root):
                #         str += line
                #     src = Source(str)
                #     src.render("Graphen/Test" + self.i.__str__(), format="png", view=False)
                # self.i += 1
                for k in self.getSpiel().getMoeglicheSpalten():
                    boardcopy = c.deepcopy(self.getSpiel())
                    boardcopy.setSpielzug(k)
                    self.setChild(boardcopy)
                self.aktuellerKnoten = self.aktuellerKnoten.children[0]
                self.simulation()
        else:
            max_node = None
            for k in self.aktuellerKnoten.children:
                if k.__getattribute__("n") == 0:
                    max_node = k
            if max_node is None:
                for k in self.aktuellerKnoten.children:
                    self.calcUCB(k)
                    if max_node is None:
                        max_node = k
                    elif k.__getattribute__("ucb") > max_node.__getattribute__("ucb"):
                        max_node = k
            self.aktuellerKnoten = max_node
            self.selection()

    def simulation(self):
        boardcopy = c.deepcopy(self.getSpiel())
        while not boardcopy.istSpielZuEnde():
            boardcopy.setSpielzug(boardcopy.getMoeglicheSpalten()[0])
        if boardcopy.getGewinner() == None:
            self.backpropagation(0)
        if boardcopy.getGewinner().__eq__(self.player_perspectiv):
            self.backpropagation(1)
        else:
            self.backpropagation(-1)

    def backpropagation(self, result):
        self.aktuellerKnoten.__setattr__("w", self.aktuellerKnoten.__getattribute__("w") + result)
        self.aktuellerKnoten.__setattr__("n", self.aktuellerKnoten.__getattribute__("n") + 1)
        if self.aktuellerKnoten.parent is None:
            return True
        else:
            self.aktuellerKnoten = self.aktuellerKnoten.parent
        return self.backpropagation(result)

    def getBestZug(self):
        max = self.root.children[0]
        for k in self.root.children:
            if k.__getattribute__("w") > max.__getattribute__("w"):
                max = k

        return max.__getattribute__("game")

    def calcUCB(self, node):
        ucb = node.__getattribute__("w") / node.__getattribute__("n") + m.sqrt(
            (2 * m.log2(node.parent.__getattribute__("n")) / node.__getattribute__("n")))
        node.__setattr__("ucb", ucb)
