import random
print("Hello! You are stuck in the house of a Pinterest mom, where each room is seasonally themed.\n Unfortunately, some of her decorations might be too realistic. Your goal is to make it out of all four rooms alive.")
print("You have 5 health points, 3 backpack slots, and 1 hand item.")

class spring():

    foundShed = False
    location = ''
    passed = ''
    def __init__(self):
        current_game = newGame
        self.passed = False
        self.location = 0
        print('The first door leads you into the Spring Room. You are scared and lost, but at least the weather is nice and the birds are chirping.') 
        self.Q1()
    def Q1(self):
        print('''\nChoose your selection:
              R. Explore the River
              F. Explore the Forest
              G. Explore the Garden
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = game.parseText(game,selection)
        if choice == 'r':
            self.Q2()
        elif choice == 'f':
            self.Q3()
        elif choice == 'g':
            self.Q4()
        else:
            self.Q1()


    def Q2(self):
    	print('\nYou are at the River') 
        print('''Choose your selection:
                F. Explore the Forest
                G. Explore the Garden
                B. Backpack / Check Stats
                ''')
        selection = input()
        choice = game.parseText(game,selection)
        if choice == 'f':
            self.Q3()
        elif choice == 'g':
            self.Q4()
        elif choice == 'w':
            self.Q5()
        elif choice == 'a':
            self.Q5()
        else:
            self.Q2()
    def Q3(self):
    	print('\nYou are in the Forest')
    	print('''Choose your selection:
              R. Explore the River
              G. Explore the Garden
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = game.parseText(game,selection)
        if choice == 'r':
            self.Q2()
        elif choice == 'g':
            self.Q4()
        else:
            self.Q3()
    def Q4(self,e):
        
        event = random.random()
        if event < 0.1:
            newGame.lives -= 1
            print("Oof, you've lost one life. Current life: {}".format(newGame.lives))
            e = 0
        event += e
        if event > 2 and not self.foundShed:
            newGame.getFromGround('shovel')
            newGame.getFromGround('fishing rod')
            event = 0
            print("You have found the shed, there is a shovel and a fishing rod inside, they might be useful.")
            self.Q7()
        print('''Choose your selection:
              R. Explore the River
              F. Explore the Forest
              B. Backpack / Check Stats
              ''')
        selection = input()
        choice = game.parseText(game,selection)
        if choice == 'r':
            self.Q2()
        elif choice == 'f':
            self.Q3()
        else:
            self.Q4()
    def Q5(self):
        pass
    def Q6(self):
        pass

class game():
    backpack = ['backpack']
    lives = 5
    items = 0
    hand = 'hand'
    level = 0
    places = [{'r':1, 'f':2, 'g':3},
              {'s':1, 'o':2, 'b':3},
              {'p':1, 'l':2, 'x':3},
              {'m':1, 'i':2, 'c':3}]
    location = ''
    def __init__(self):
        self.location = 'default_0'
    def start(self):
        stage1 = spring()
	def getFromBackpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)
            self.backpack.append(self.hand)
            self.hand = item
        else:
            print("Sorry, there is no such item in your backpack.")
    
    def getFromGround(self, item):
        if len(self.backpack) < 3:
            self.backpack.append(self.hand)
            self.hand = item
        else:
            print("Sorry, your backpack is full.")

    def remove(self, item):
        if item == self.hand:
            print('What do you want to replace the ' + item + ' in your hand?')
            item = input().lower()
            self.hand = item
        elif item in self.backpack:
            self.backpack.remove(item)

    def useItem(self, item):
        pass
    
    def parseText(self, text):
        text = text.lower()
        if text == "b":
            print("lives: " + str(self.lives))
            print("item in hand: " + self.hand)
            print("backpack: " + str(self.backpack)[1:-1])
        elif text in self.places[self.level] and text != self.location:
            self.location = text
            print("You have now changed locations. " + self.location)
            return self.location
        else:
            print("Sorry, we didn't get that. Please try again.")

newGame = game()
newGame.start()




