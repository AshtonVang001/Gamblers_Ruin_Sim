from rules import Rules
import random

#this class inherits the rules class
class Simulation(Rules):
    def __init__(self, bet=1, rounds=0):
        super().__init__()
        self.bet = bet
        self.rounds = rounds
    
    #the game itself
    #checks if a random number between 0.0-1.0 is either greater than or less than the probability (currently set to 0.5)
    #increases or decreases money based off that
    def simBets(self):
        if random.random() < self.probability:
            self.money += self.bet
        else:
            self.money -= self.bet

    #player can either choose to play or bet here
    #player either types in y or n
    #rn if player types anything besides "y" it just exits (maybe fix this later)
    def play(self):
        willPlay = input("Would you like to play y/n?")
        if(willPlay == "y"):
            while(self.money != self.goal and self.money != self.lose_condition): 
                willBet = input("Would you like to bet y/n?")
                if willBet == "y":
                    self.rounds += 1
                    self.simBets()
                    print("You have $", self.money, "left")
                else:
                    print("Ok")
                    break;
        #print the record of money left and how many rounds played
        print("Money left: ", self.money)
        print("Rounds played: ", self.rounds)

    def playLoop(self):
        for _ in range(10000):
            if self.money == self.goal or self.money == self.lose_condition:
                break
            self.rounds += 1
            self.simBets()
        print("Money left: ", self.money)
        print("Rounds played: ", self.rounds)

player = Simulation();
player.playLoop();
        


