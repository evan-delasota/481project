from games import *
from random import shuffle


class Card:
    suits = ["clubs", "diamonds", "hearts", "spades"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False

        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False

        return False

class Deck:
    def __init__(self):
        self.deck = []
        for value in range(2, 15):
            for suit in Card.suits:
                self.deck.append(Card(value, suit))
        shuffle(self.deck)

    def remove_card(self, card):
        if len(self.deck) == 0:
            return
        return self.deck.remove(card)

class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        return self.hand.append(card)

    def remove_card(self, card):
        if len(self.hand) == 0:
            return
        return self.hand.remove(card)




class GameOfThirteen(Game):
    def __init__(self):
        self.num_of_players
        self.players = []
        self.deck = Deck()
        self.board = []
        self.moves = []
        # self.initial = GameState(to_move = to_move, utility = 0, board = self.board, moves = self.moves)

    def deal_cards(self):


    def result(self, state, move):
        pass

    def actions(self, state):
        pass

    def print_card_pile(self, board):
        if board == []:
            print("Pile doesn't exist\n")
            return
        else:
            return board.peek()

    def construct_moves(self, card_pile):
        moves = []
        return moves

    def terminal_test(self, state):
        return len(state.moves) == 0

    def utility(self, state, player):
        pass

if __name__ == "__main__":
    thirteen = GameOfThirteen()
    test = Deck()
    player_1 = Player()
    for card in test.deck:
        print(card.value, card.suit)
    # utility = thirteen.play_game(alpha_beta_player, query_player)


