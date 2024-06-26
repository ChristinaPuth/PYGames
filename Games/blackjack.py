

import random
import sys  # Import sys to use sys.exit()

class Player(object):
    def __init__(self):
        self.alive = True
        self.lost = False
        self.hand = []
        self.total = 0
        self.distance_away_from_goal = None

    def show_to_self(self):
        return "%d: %s" % (self.total, str(self.hand))

    def update(self):
        temp = 0
        for card in self.hand:
            temp += card[0]
        self.total = temp

    def show(self):
        if not self.lost:
            return "%s and %d more cards" % (self.hand[0], len(self.hand) - 1)
        else:
            return "%d: %s" % (self.total, str(self.hand))

class Game(object):
    suits = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
    cards_per_suit = 13
    cards_in_deck = len(suits) * cards_per_suit
    goal = 21

    def __init__(self, number_of_players):
        self.deck = [(value, suit) for suit in self.suits for value in range(1, self.cards_per_suit + 1)]
        self.players = []
        self.possible_winners = []
        self.round = 0

        for x in range(number_of_players):
            p = Player()
            self.players.append(p)

    def deal_cards(self, number_of_cards, player):
        if player.alive:
            for card in range(number_of_cards):
                c = self.deck[0]
                player.hand.append(c)
                self.deck.remove(c)

    def response_handler(self, response, player):
        if response == 'exit':
            print("Exiting game.")
            sys.exit(0)  # Exits the game
        elif response == 's':
            player.alive = False
        elif response == 'c':
            self.deal_cards(1, player)
            print(player.hand[-1])
            player.update()
        elif response == 'l':
            print(player.show_to_self())
        else:
            print("Not a valid response")

        if player.alive:
            new_response = input("Player %d: 's' to stop, 'c' to continue, 'l' to look at your hand, or 'exit' to exit the game:" %
                                 (self.players.index(player) + 1)).strip()
            self.response_handler(new_response, player)

    def final_score_handler(self, player):
        if player.lost:
            return "**lost** %d" % player.total
        else:
            score_board = sorted(self.possible_winners, key=lambda x: x.distance_away_from_goal)
            if player is score_board[0]:
                return "**Winner** %d" % player.total
            else:
                return player.total

    def main(self):
        random.shuffle(self.deck)
        for player in self.players:
            self.deal_cards(2, player)
            player.update()

        while True:
            self.round += 1
            number_alive = len([p for p in self.players if p.alive])
            print("Round: %d" % self.round)
            for player in self.players:
                print("Player %d: %s" % (self.players.index(player) + 1, player.show()))

            for player in self.players:
                if player.alive:
                    response = input("Player %d: 's' to stop, 'c' to continue, 'l' to look at your hand, or 'exit' to exit the game:" %
                                     (self.players.index(player) + 1)).strip()
                    self.response_handler(response, player)

                    if player.total > self.goal:
                        player.alive = False
                        player.lost = True
                        print("Player %d is out of the game" % (self.players.index(player) + 1))

            if number_alive == 0:
                break

        for player in self.players:
            if not player.lost:
                player.distance_away_from_goal = self.goal - player.total
                self.possible_winners.append(player)

        for player in self.players:
            print("Player %d: %s" % (self.players.index(player) + 1, self.final_score_handler(player)))

if __name__ == '__main__':
    g = Game(5)
    g.main()
