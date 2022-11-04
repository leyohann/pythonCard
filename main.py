from models import PresidentGame
from random import randrange


def print_ln():
    print('\n')


def game_loop(g: PresidentGame):
    """
    The main game loop.
    Loops in circle until the user wants to quit the application.
    Args:
        g: The President Game instance.
    """
    wanna_continue = True
    gameover = False
    empty = 0
    print(f"premier joueur : {g.first_player.name}")
    for ai in g.ai_players:
        print(f"Adversaire:{ai.name} ,nombre de cartes:{len(ai.hand)}, main:{ai.hand}")
    while wanna_continue:
        while len(g.main_player.hand) != 0 and gameover is False:
            print('Your current deck is : ')
            print(g.main_player.hand, )
            print_ln()
            if g.first_player == g.main_player :
                choice = ""
                plays = g.first_player.play(choice)
                print(f"{plays}")
            choice = input('What value do you wish to play ? ')
            plays = g.main_player.play(choice)
            print(f"You play {plays}")
            nb_cards = len(plays)
            for ai in g.ai_players:
                plays = ai.play(choice, nb_cards)
                print(f"{ai.name} plays \t {plays}")
                # print(f"{ai.name} : {ai.hand}")
            wanna_continue = input('Do you want to continue playing (y/N)? ')
            wanna_continue = (wanna_continue == 'Y' or wanna_continue == 'y')
            for ai in g.ai_players:
                if ai.hand is []:
                    empty = empty + 1
                    print(empty)
                    if empty == 2:
                        gameover = True
                        print("gameover is true")
            empty = 0

        print('BRAVO! Champs, you win!!!')
        wanna_continue = False


print("end of game")

if __name__ == '__main__':
    print_ln()
    print(
        """        *********************************************
        *** President : The cards game (TM) v.0.1 ***
        ********************************************* """)
    g = PresidentGame()
    g.distribute_cards()
    game_loop(g)
    print('Thank you for playing. I hope you enjoyed !')
