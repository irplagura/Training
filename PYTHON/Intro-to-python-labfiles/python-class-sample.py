
class Greeter(object):
    def hello(self):
	    print("Hello")
		
	#note self always defined when defining function in a class
    def goodbye(self):
        print("Goodbye")
		


class Greeter2(object):
    # provide an argument to init
    def __init__(self, name):
        self.name = name
		
    def hello(self):
        print("Hello " + self.name)
		
    def goodbye(self) :
        print("Goodbye " + self.name)
		
		
# Create an instance of the class
g = Greeter()
g.hello()
g.goodbye()

g2 = Greeter2("Ray")
g2.hello()
g2.goodbye()

################################################
import random

# Simulate a 6 side die
class Die(object):
    def roll(self):
        return random.randint(1, 6)

# Create an instance of the die
d = Die()
print("Dies roll: " + str(d.roll()))
print("Dies roll: " + str(d.roll()))
print("Dies roll: " + str(d.roll()))

##########################

# Defined number of sides in a die
class Die2(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

print("Another die with defined sides")
d2 = Die2(128)
print("Dies roll: " + str(d2.roll()))
print("Dies roll: " + str(d2.roll()))
print("Dies roll: " + str(d2.roll()))

d3 = Die2(512)
print("Dies roll: " + str(d3.roll()))
print("Dies roll: " + str(d3.roll()))
print("Dies roll: " + str(d3.roll()))


##############################
# Simulate a shuffled deck of card
# and deal (remove from a deck)
class Deck(object):
    def shuffle(self):
        suites = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks  = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]      

        # self.variable will be used only for this class
        self.cards = []
        # Fill in the cards list
        for suit in suites:
            for rank in ranks:
                self.cards.append(rank + " of " + suit)

        # use shuffle function to shuffle a list
        random.shuffle(self.cards)

    def deal(self):
        # Using pop function to remove entry on top of list
        return self.cards.pop()

c = Deck()
c.shuffle()
# max of only 56 cards, otherwise it's going to be an empty list
for I in range(1,58):
  print("Here is a random deck of card: "+str(I))
  print(c.deal())




##############
# All of these can be turned into as a module
# and import it from your program
