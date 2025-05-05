import random
# ASCII ATR Graphic
logo = '''
█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█

▄▖▄▖▖  ▖▄▖
▌ ▌▌▛▖▞▌▙▖
▙▌▛▌▌▝ ▌▙▖
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

win = '''
▗▖  ▗▖▗▄▖ ▗▖ ▗▖    ▗▖ ▗▖▗▄▄▄▖▗▖  ▗▖
 ▝▚▞▘▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌  █  ▐▛▚▖▐▌
  ▐▌ ▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌  █  ▐▌ ▝▜▌
  ▐▌ ▝▚▄▞▘▝▚▄▞▘    ▐▙█▟▌▗▄█▄▖▐▌  ▐▌                       
'''
lose = '''
▗▖  ▗▖▗▄▖ ▗▖ ▗▖    ▗▖    ▗▄▖  ▗▄▄▖▗▄▄▄▖
 ▝▚▞▘▐▌ ▐▌▐▌ ▐▌    ▐▌   ▐▌ ▐▌▐▌   ▐▌   
  ▐▌ ▐▌ ▐▌▐▌ ▐▌    ▐▌   ▐▌ ▐▌ ▝▀▚▖▐▛▀▀▘
  ▐▌ ▝▚▄▞▘▝▚▄▞▘    ▐▙▄▄▖▝▚▄▞▘▗▄▄▞▘▐▙▄▄▖
'''

draw = '''                                                                                                 
▗▄▄▄ ▗▄▄▖  ▗▄▖ ▗▖ ▗▖
▐▌  █▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌
▐▌  █▐▛▀▚▖▐▛▀▜▌▐▌ ▐▌
▐▙▄▄▀▐▌ ▐▌▐▌ ▐▌▐▙█▟▌                                                                                             
'''

invalid = '''
▗▄▄▄▖▗▖  ▗▖▗▖  ▗▖ ▗▄▖ ▗▖   ▗▄▄▄▖▗▄▄▄ 
  █  ▐▛▚▖▐▌▐▌  ▐▌▐▌ ▐▌▐▌     █  ▐▌  █
  █  ▐▌ ▝▜▌▐▌  ▐▌▐▛▀▜▌▐▌     █  ▐▌  █
▗▄█▄▖▐▌  ▐▌ ▝▚▞▘ ▐▌ ▐▌▐▙▄▄▖▗▄█▄▖▐▙▄▄▀                            
'''

goodbuy = '''
 ▗▄▄▖ ▗▄▖  ▗▄▖ ▗▄▄▄  ▗▄▄▖ ▗▖ ▗▖▗▖  ▗▖
▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌  █ ▐▌ ▐▌▐▌ ▐▌ ▝▚▞▘ 
▐▌▝▜▌▐▌ ▐▌▐▌ ▐▌▐▌  █ ▐▛▀▚▖▐▌ ▐▌  ▐▌  
▝▚▄▞▘▝▚▄▞▘▝▚▄▞▘▐▙▄▄▀ ▐▙▄▞▘▝▚▄▞▘  ▐▌                                
'''
# greeting
print(f"{logo}\n->Make your choice:"
       "\nType:\n0 for - ROCK\n1 for - PAPER\n2 for - SCISSORS\n->Type End to quit.")

# win/lose counters
game = 0
wins = 0
losses = 0
draws = 0

while True:
    player = input("Make your choice: ")

    if player == 'End'.lower():
        print(f"{goodbuy}\nFinal Score: Wins: {wins} | Losses: {losses} | Draw:{draws}  \nTotal games: {game}")
        break

    if player not in ['0', '1', '2', 'end']:
        print(f"{invalid}\n\nPLEASE ENTER 0, 1, 2 to PLAY OR End TO QUIT".lower())
        continue  # star over

    player = int(player)
    computer = random.randint(0, 2)

    # computer chosing
    if computer == 0:
        print(f'Computer chose: "ROCK"\n{rock}')
    elif computer == 1:
        print(f'Computer chose: "PAPER"\n{paper}')
    elif computer == 2:
        print(f'Computer chose: "SCISSORS"\n{scissors}')
    print("_________________________\n")

    # player chosing
    if player == 0:
        print(f'Player chose: "ROCK"\n{rock}')
    elif player == 1:
        print(f'Player chose: "PAPER"\n{paper}')
    elif player == 2:
        print(f'Player chose: "SCISSORS"\n{scissors}')

    # wind & lose game logic
    if player == computer:
        draws += 1
        game += 1
        print(f"{draw}\n\nPLAY AGAIN!")

    elif (player == 0 and computer == 2) or \
            (player == 1 and computer == 0) or \
            (player == 2 and computer == 1):
        print(win)
        wins += 1  # add win score
        game += 1
    else:
        print(lose)
        losses += 1  # add lose score
        game += 1
    # Current Score:
    print(f"Game # {game} | Wins: {wins} | Losses: {losses} | Draw:{draws} ")
