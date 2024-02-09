from random import randrange

def getInput():
    user_input = input("Hit or stay? (h or s): ")
    return user_input

def checkInput(input):
    if input != 'h' and input != 's' and input != 'q':
        print("Try again. h for Hit. s for Stay. q for quit")
        return 0
    else:
        return input

def draw(deck_size):
    i = randrange(0,deck_size)
    return i

# deal(player_hand,dealer_hand,deck):


# def hit(hand):


# def stay(dealer_hand, player_hand):


def main():
    quit = False

    deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]

    player_hand = 0
    dealer_hand = 0

    # deck = deal(player_hand, dealer_hand,deck)

    
    while quit == False:
        player_move = getInput()
        player_move = checkInput(player_move)
        if player_move:
            if player_move == 'h':
                card = draw(len(deck))
                card = deck.pop(card)
                print(deck)
                print(card)
            # elif player_move == 's':
                # stay()
            else:
                quit = True
        
        



if __name__ == "__main__":
    main()
