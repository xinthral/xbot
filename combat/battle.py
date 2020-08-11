from theatre import BattleField
from random import seed, choice
from time import perf_counter

class Battle(object):
    """
    Many to Many
    """
    def __init__(self, bot):
        self.battlefield = Battlefield()
        self.players = []
        self.referee = bot
        self.rumble()

    def duel(self):
        """
        Allows players to target another player to battle
        """
        pass

    def pairOff(self):
        """
        Randomly chooses a pair from the players list to battle
        """
        pass

class Fight(object):
    """
    One to One
    """
    def __init__(self, player1, player2, phase):
        # Instantiate fight seed
        seed(perf_counter())

        self.p1 = player1
        self.p2 = player2

        # Each fight reduces phase, FIXME: recovery on cycle?
        if (phase >= 0) and (phase <= 10):
            self.phase = int(phase)
        else:
            self.phase = 5
        #self.strike()

    def ambush(self):
        """
        The greater the phase value the greater the probability of success
        """
        probabilityMap = [ _ for _ in range(0, 12) ]
        epsilon = self.randomRoll(probabilityMap)
        return(epsilon <= self.phase)

    def randomRoll(self, inputList):
        return(choice(inputList))

    def strike(self):
        if not (self.ambush()):
            tmpUsr = self.p1
            self.p1 = self.p2
            self.p2 = tmpUsr

if __name__ == "__main__":
    from user import Player

    usr1 = Player("Tester", "Kodo", 0, 1, 5, 0)
    usr2 = Player("Tester", "Podo", 0, 1, 5, 0)

    def testFightObj():
        fightObj = Fight(usr1, usr2, -1)
        return(fightObj)

    def itrFightObj():
        count = 0
        for _ in range(1, 101):
            if testFightObj().ambush():
                count += 1
        return(count)

    # Shows a list of probabilities of ambush by %
    def ambushProb():
        ambsh = [ itrFightObj() for _ in range(0, 30) ]
        ambsh.sort()
        print("Success %:\n[{} -> {}]".format(ambsh[0], ambsh[-1]))
        #return(ambsh)

    ambushProb()
    input("Press ENTER to continue...")
