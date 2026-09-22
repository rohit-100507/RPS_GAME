import random

while True :

   
    pc = ["ROCK" , "PAPER" , "SCISSOR"]
    random_throw= random.choice(pc)


    user = input("Enter ROCK / PAPER / SCISSOR : ").upper()

    if user not in pc:
        print(" ERROR: Please enter only ROCK, PAPER, or SCISSOR")
        continue
    
    print("COMPUTER CHOSSE : " , random_throw)

 
    if  user == "ROCK" and random_throw == "PAPER":
        print("YOU LOSS , TRY AGAIN")

    elif user == "ROCK" and random_throw == "SCISSOR":
        print("YOU WON ")    

    elif user == "PAPER" and random_throw == "SCISSOR" :
        print("YOU LOSS , TRY AGAIN") 

    elif user == "PAPER" and random_throw == "ROCK" :
        print("YOU WIN")     
 
    elif user == "SCISSOR" and random_throw == "ROCK" :
        print("YOU LOSS , TRY AGAIN")

    elif user == "SCISSOR" and random_throw == "PAPER" :
        print("YOU WIN")    

    else :
        print("Its tie")    


    while True:
        next_play = input("Want To Play Another Round ? (yes / no): ").lower()

        if next_play == "yes":
            break
          

        elif next_play == "no":
            print("Thank you for playing")
            exit()

        else:
            print("ERROR: Please enter only yes or no")

   