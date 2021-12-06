import random as rnd
import turtle as t

def instructions():
    ''' Print the instructions for the game Pig '''
    print("Please open the .txt file named 'Instructions.txt' if you are unsure of how to play")
    file = open("Instructions.txt", 'w')
    file.write("Instructions for Pig:\n")
    file.write("1) Input the number of players\n")
    file.write("2) Input the winning score (score players need to reach to win)\n")
    file.write("3) When instructed, the player whose turn it is can do the following:\n\n")
    file.write("\t\t'R' = Roll\t 'H' = Hold\n\n")
    file.write("The player's turn score is the sum of all rolls that turn\n\n")
    file.write("Once the player chooses to hold, the turn score is added to their total score\n")
    file.write("If a player rolls a 1 in their turn, the turn ends without adding anything to their total score\n\n")
    file.write("The first player to reach the goal score wins!")

    file.write("\n\n\nMake sure you have playsound installed to your python pathway, google it if you don't know how to install a pip3 to a command shell")
    
def random():
    return rnd.randint(1, 6)

def settings():
    players = int(input("Please enter the number of players: "))
    goal = int(input("Please enter the goal score: "))
    return players, goal

def playerlist(players):
    ''' Create a player list, backwards, based on the argument '''
    playerlist = []

    for i in range(1, players + 1):
      playerlist.append(i)

    return playerlist
    
def game():
    turnscore = 0
    flag = False
    while flag == False:
        cmd = input("What would you like to do? R for roll, H for hold: ")
        try:
            if cmd == 'R':
                roll = random()
                print("\nYou rolled a {}".format(roll))
                if roll != 1:
                    turnscore += roll
                    print("Your turn score is {}".format(turnscore))
                else:
                    print("Turn over")
                    return 0
            if cmd == 'H':
                print("Your final turnscore is {}".format(turnscore))
                return turnscore
        except:
            print("Invalid input, try again")
        
def main():
    ''' The main body of the game, calls all other functions and arguments in it'''
    instructions()
    
    plrind = 0
    scorelist = []
    
    setting = settings()
    playerlist1 = playerlist(setting[0])
    players = len(playerlist1)
    goalscore = setting[1]
    for i in range(players):
        scorelist.append(0)
    
    while max(scorelist) < goalscore:
        print("\n\n\nPlayer {}".format(plrind + 1))
        score = game()
        scorelist[plrind] += score
        print("Your total score is {}".format(scorelist[plrind]))
        plrind += 1
        plrind %= players
    
    winner = scorelist.index(max(scorelist))
    print("Player {} is the winner!".format(winner + 1))  
    print("Enjoy this Turtle having some fun")  
    
repeat = True
while repeat != False:
    
    if __name__ == '__main__':
        main()
    
    rep = input("Play again?(Y/N): ")
    if rep == 'Y' or rep == 'y':
        repeat = True
    else:
        repeat = False
