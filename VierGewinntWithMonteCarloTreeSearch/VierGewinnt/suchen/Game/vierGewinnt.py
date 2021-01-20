import random as r

LEER_FELD = "*"


class VierGewinnt:
    DEF_ZEILEN = 6
    DEF_SPALTEN = 7
    X_SPIELER = "X"
    O_SPIELER = "O"

    def __init__(self, spieler1=X_SPIELER, spieler2=O_SPIELER, zeilen=DEF_ZEILEN, spalten=DEF_SPALTEN):
        self.spieler1 = spieler1
        self.spieler2 = spieler2
        self.zeilen = zeilen
        self.spalten = spalten
        self.spielfeld = [[LEER_FELD] * spalten for i in range(zeilen)]
        self.aktuellerSpieler = spieler1
        # self.letzterSpieler = None
        self.gewinner = None

    def getAktuellerSpieler(self):
        return self.aktuellerSpieler

    def getGewinner(self):
        return self.gewinner

    def printSpielfeld(self):
        str = ""
        for spalte in range(self.spalten):
            str += spalte.__str__() + " "
        str += "\n"
        for zeile in range(self.zeilen):
            str += " ".join(self.spielfeld[zeile]) + "\n"
        print(str)

    def setSpielzug(self, spalte):
        if (not self.istSpalteMoeglich(spalte)) or self.istSpielZuEnde():
            return False
        zeile = self.getLetzteMoeglicheZeile(spalte)
        self.spielfeld[zeile][spalte] = self.aktuellerSpieler
        # hier muss man noch überprüfen ob einer gewonnen hat dann break
        self.checkGewinner()
        if self.istSpielZuEnde():
            return True
        if self.aktuellerSpieler == self.spieler1:
            self.aktuellerSpieler = self.spieler2
        else:
            self.aktuellerSpieler = self.spieler1

    def getLetzteMoeglicheZeile(self, spalte):
        for zeile in range(self.zeilen):
            if self.spielfeld[zeile][spalte] != LEER_FELD:
                return zeile - 1
        return -1

    def getMoeglicheSpalten(self):
        spaltenList = []
        for spalte in range(self.spalten):
            if self.istSpalteMoeglich(spalte):
                spaltenList.append(spalte)

        r.shuffle(spaltenList)
        return spaltenList

    def istSpalteMoeglich(self, spalte):
        return self.spielfeld[0][spalte] == LEER_FELD

    def setSpielfeld(self, spielfeld):
        self.spielfeld = spielfeld

    def getSpielfeld(self):
        return self.spielfeld

    def istSpielZuEnde(self):
        return self.gewinner or len(self.getMoeglicheSpalten()) == 0

    def checkGewinner(self):
        spielzuege = 0
        spieler = None
        # horizontaler check
        for zeile in range(self.zeilen):
            for spalte in range(self.spalten):
                spielzuege, spieler = self.checkFeld(spielzuege, spieler, zeile, spalte)
                if spielzuege == 4:
                    self.gewinner = spieler
                    return True
            spielzuege = 0
            spieler = None

        # vertikaler check
        for spalte in range(self.spalten):
            for zeile in range(self.zeilen):
                spielzuege, spieler = self.checkFeld(spielzuege, spieler, zeile, spalte)
                if spielzuege == 4:
                    self.gewinner = spieler
                    return True
            spielzuege = 0
            spieler = None

        # diagonal links nach rechts, unterer bereich
        for zeile in range(self.zeilen - 3):
            aktuelleZeile = zeile
            for spalte in range(self.spalten):
                spielzuege, spieler = self.checkFeld(spielzuege, spieler, aktuelleZeile, spalte)
                if spielzuege == 4:
                    self.gewinner = spieler
                    return True
                aktuelleZeile += 1
                if aktuelleZeile >= self.zeilen:
                    break
            spielzuege = 0
            spieler = None
        # diagonal links nach rechts, oberer bereich
        for spalte in range(self.spalten - 3):
            aktuellerSpalte = spalte
            for zeile in range(self.zeilen):
                spielzuege, spieler = self.checkFeld(spielzuege, spieler, zeile, aktuellerSpalte)
                if spielzuege == 4:
                    self.gewinner = spieler
                    return True
                aktuellerSpalte += 1
                if aktuellerSpalte >= self.spalten:
                    break
            spielzuege = 0
            spieler = None

        # diagonal rechts nach links, oberer bereich
        for spalte in range(self.spalten - 1, 1, -1):
            aktuellerSpalte = spalte
            for zeile in range(self.zeilen):
                if aktuellerSpalte < 0:
                    break
                spielzuege, spieler = self.checkFeld(spielzuege, spieler, zeile, aktuellerSpalte)
                if spielzuege == 4:
                    self.gewinner = spieler
                    return True
                aktuellerSpalte -= 1
            spielzuege = 0
            spieler = None

        # diagonal rechts nach links, unterer bereich
        for zeile in range(self.zeilen - 3):
            aktuelleZeile = zeile
            for spalte in range(self.spalten - 1, -1, -1):
                spielzuege, spieler = self.checkFeld(spielzuege, spieler, aktuelleZeile, spalte)
                if spielzuege == 4:
                    self.gewinner = spieler
                    return True
                aktuelleZeile += 1
                if aktuelleZeile >= self.zeilen:
                    break
            spielzuege = 0
            spieler = None
        return False

    def checkFeld(self, spielzuege, spieler, zeile, spalte):
        if self.spielfeld[zeile][spalte] != LEER_FELD:
            if self.spielfeld[zeile][spalte] == spieler:
                spielzuege += 1
            else:
                spielzuege = 1
                spieler = self.spielfeld[zeile][spalte]
        else:
            spielzuege = 0
            spieler = None
        return spielzuege, spieler

    def __str__(self):
        str = ""
        for spalte in range(self.spalten):
            str += spalte.__str__() + " "
        str += "\n"
        for zeile in range(self.zeilen):
            str += " ".join(self.spielfeld[zeile]) + "\n"
        return str

# def checkGewinner(self):


# vg = VierGewinnt()
# vg.printSpielfeld()
# vg.setSpielzug(0)
# vg.setSpielzug(1)
# vg.printSpielfeld()
# vg.setSpielzug(0)
# vg.setSpielzug(1)
# vg.setSpielzug(0)
# vg.setSpielzug(1)
# vg.setSpielzug(0)
# vg.setSpielzug(1)
# vg.printSpielfeld()
