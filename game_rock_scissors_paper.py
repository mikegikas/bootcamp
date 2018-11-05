import random

def game():
    L = ["rock", "scissors", "paper"]
    print("----------------------")
    print("|The Game is starting|")
    print("|     Good Luck!     |")
    print("----------------------")
    totalPlayer = 0
    totalComputer = 0
    tries = True
    while(tries):
        word = input("Give a choice: ")
        if word in L:
            computerChoice = random.choice(L)
            print("Computer choice was:",computerChoice)
            if(word == computerChoice):
                print("Tie!")
            elif(word == "rock"):
                if(computerChoice == "paper"):
                    print("You lose")
                    totalComputer +=1
                else:
                    print("You win")
                    totalPlayer +=1
            elif(word == "scissors"):
                if(computerChoice == "rock"):
                    print("You lose")
                    totalComputer +=1
                else:
                    print("You win")
                    totalPlayer +=1  
            elif(word == "paper"):
                if(computerChoice == "scissors"):
                    print("You lose")
                    totalComputer +=1
                else:
                    print("You win")
                    totalPlayer +=1
        
            if(totalPlayer == 3):
                print("------------")
                print("|Player win|")
                print("------------")
                tries = False
            elif(totalComputer == 3):
                print("--------------")
                print("|Computer win|")
                print("--------------")
                tries = False
        else:
            print("Wrong input. Try Again") 

game()
  