from random import randint

class Player():
    def __init__(self):
        self.dice = []
 
    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append((randint(1,6)))
    
    def get_dice(self):
        return self.dice

def main():

    p1 = Player()
    p2 = Player()

    p1.roll()
    p2.roll()

    print(f"Player 1 rolled {p1.get_dice()}")
    print(f'Player 2 rolled {p2.get_dice()}')

    if sum(p1.get_dice()) == sum(p2.get_dice()):
        print('Draw!')
    elif sum(p1.get_dice()) == sum(p2.get_dice()):
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')

if __name__ == '__main__':
    main()