class BattleField(object):
    """
    The one to rule them all....or manage all the players atleast
    """
    def __init__(self):
        self.combatants = {
            'meta': dict(),
            'all': set(),
            'duels': set(),
            }

    # Mutators
    def addCombatant(self, fighter):
        # Prevents duplicates, but I should really use a set
        if fighter not in self.combatants['all']:
            self.combatants['all'].add(fighter)

    def remCombatant(self, fighter):
        try:
            self.combatants['all'].remove(fighter)
        except KeyError:
            print('Person is already a non-combatant')

    def addDuel(self, fighter1, fighter2):
        self.combatants['duels'].add((fighter1, fighter2))

    def remDuel(self, fighter1, fighter2):
        try:
            self.combatants['duels'].remove((fighter1, fighter2))
        except KeyError:
            print('Currently, there is no duel between these two.')
