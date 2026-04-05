from rules import Rules
#Import the matplotlib library 
import matplotlib.pyplot as plt
import numpy as np
import random

#this class inherits the rules class
class Simulation(Rules):
    def __init__(self, bet=1, rounds=0, sample_runs=[]):
        super().__init__()
        self.bet = bet
        self.rounds = rounds
        self.sample_runs = sample_runs
    
    #the game itself
    #checks if a random number between 0.0-1.0 is either greater than or less than the probability (currently set to 0.5)
    #increases or decreases money based off that
    def simBets(self, money):
        if random.random() < self.probability:
            return money + self.bet
        else:
            return money - self.bet

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


    def runOneGame(self):
        money = self.money   # starting money from Rules
        rounds = 0
        run_arr = []

        while money != self.goal and money != self.lose_condition:
            money = self.simBets(money)
            run_arr.append(money)
            rounds += 1

        return money, rounds, run_arr

    def runManyGames(self, num_games=1):
        ruin_count = 0
        goal_count = 0
        total_rounds = 0
        sample_count = 0
        for i in range(num_games):
            final_money, rounds, run_arr = self.runOneGame()
            total_rounds += rounds

            if final_money == self.lose_condition:
                ruin_count += 1
            elif final_money == self.goal:
                goal_count += 1
            #getting sample rounds for graph
            if sample_count < 10 and (i % 1000) == 0:
                self.sample_runs.append(run_arr)
                sample_count += 1
        
        
        prob_ruin = ruin_count / num_games
        prob_goal = goal_count / num_games
        avg_rounds = total_rounds / num_games
        
        print(f"Games played: {num_games}")
        print(f"Probability of ruin: {prob_ruin}")
        print(f"Probability of reaching ${self.goal}: {prob_goal}")
        print(f"Average number of rounds played: {avg_rounds}")
        
    def graphGames(self):
        plt.title("Sample Rounds (10)")
        plt.ylabel("Money")
        plt.xlabel("Rounds")
        x = []
        y = []            
        for _, run in enumerate(self.sample_runs):
            x = range(len(run))
            plt.plot(x, run, alpha = .7, linewidth=1)
        plt.show()
    

player = Simulation();
player.runManyGames();
player.graphGames();
        