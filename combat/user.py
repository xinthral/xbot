class Player(object):
    def __init__(self, title="Recruit", name="Unnamed", armor=0, damage=1, health=1, mana=0):

        # Current Stats
        self.armor = armor
        self.damage = damage
        self.health = health
        self.mana = mana
        self.name = name
        self.title = title

        # Base Stats
        self._base = {'name': name, 'title': title,
                      'armor': armor, 'damage': damage,
                      'health': health, 'mana': mana}

        # Max Stats
        self._max = {'armor': armor, 'damage': damage,
                     'health': health, 'mana': mana}

    def decrementHealth(self, damage=1):
        # Death check
        if (self.health <= damage):
            #FIXME: Needs to call death sequence
            print("Dead-ed")
        self.health -= damage

    def incrementHealth(self, regen=1):
        # Max HP check
        if ((self.health + regen) > self._max['health']):
            self.health = self._max['health']
        else:
            self.health += regen

    def revealIdentity(self):
        # Meant to be overloaded
        print("My name is {}.".format(self.name))

    def displayStats(self, original=False):
        if (original):
            print("Original Stats:\nName:\t{}\nHealth:\t{}\nMagic:\t{}\nArmor:\t{}"
                  .format(self.name, self.health, self.mana, self.armor))
        else:
            print("|| {} - [ HP: {} ] [ MP: {} ] [ AR: {} ] ||"
                  .format(self.name, self.health, self.mana, self.armor))

    def returnStats(self):
        return(self._base)

class SuperHero(Player):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def revealIdentity(self):
        super(SuperHero, self).reveal_identity()
        print("..And I am {}!".format(self.hero_name))

def testUser(name='McTester'):
    rank, armor, damage, health, mana = 'Tester', 5, 1, 10, 10
    return(Player(rank, name, armor, damage, health, mana))

if __name__ == "__main__":
    kodo = testUser('Kodo')
    podo = testUser('Podo')
