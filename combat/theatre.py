class BattleField(object):
    """
    The one to rule them all....or manage all the players atleast
    """
    def __init__(self):
        self.combatants = {
            'meta': {},
            'all': [],
            'duels': [],
            }

    # Mutators
    def addCombatant(self, fighter):
        # Prevents duplicates, but I should really use a set
        if fighter not in self.combatants['all']:
            self.combatants['all'].append(fighter)

    def remCombatant(self, fighter):
        self.combatants['all'].remove(fighter)

    def addDuel(self, fighter1, fighter2):
        self.combatants['duels'].append((fighter1, fighter2))

    def remDuel(self, fighter1, fighter2):
        try:
            self.combatants['duels'].remove((fighter1, fighter2))
        except ValueError:
            print('This pair is not fighting.')
