__author__ = 'anna'
#One card war game
#From 1 to 4 players

import cards2, games

class W_Card(cards2.Card):
    """A war game playing card"""

    @property
    def value(self):
        v = W_Card.RANKS.index(self.rank) + 2
        return v
class W_Deck(cards2.Deck):
    """A war game deck"""
    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank, suit))
class W_Hand(cards2.Hand):
    """A war game hand"""
    def __init__(self, name):
        super(W_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(W_Hand, self).__str__() + "(" + str(self.total) + ")"
        return rep
    @property
    def total(self):
        t = 0
        for card in self.cards:
            t += card.value
            return t

class W_Player(W_Hand):
    """A war game player"""

    def win(self):
        print(self.name, "wins.")

    def lose(self):
        print(self.name, "loses.")

    def push(self):
        print(self.name, "pushes.")

class W_Game(object):
    """A war game"""
    def __init__(self, names):
        self.players = [W_Player(name) for name in names]
        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()


    def play(self):
        #deal 1 card to everyone
        self.deck.deal(self.players, per_hand=1)

        records = dict()
        for player in self.players:
            records[player.name] = player.total
        print("Records", records)

        sort = sorted(records, key=records.get, reverse=True)
        print("Sorted keys", sort)
        #winner rating using set
        st = sorted(set(sorted(records.values())), reverse=True)
        print("Set: ", st)
        win_rating = st[0]

        #announce winner(s)

        #this code is much easear and good but it may announce winners/users in a wrong order
        # for player in self.players:
        #     if player.total == win_rating:
        #         player.win()
        #     else:
        #         player.lose()

        for item in sorted(records.items()):
            if item[1] == win_rating:
                print(item[0], "wins.")

        #keys of winners to delete from records in order to left only losers
        to_del = [item[0] for item in records.items() if item[1] == win_rating]

        #deleting winners, only losers left
        for i in to_del:
            del records[i]

        #announce losers
        for loser in sorted(records):
            print(loser, "loses.")

        #remove everyone cards
        for player in self.players:
            player.clear()

def main():
    print("\t\tWelcome to War Game!\n")

    number = games.ask_number("How many players? (1-4): ", low=1, high=5)
    names = [input("Enter player name: ") for i in range(number)]
    print(names)
    print()

    game = W_Game(names)
    count = 0
    again = None
    while again != "n":
        count +=1
        if count > 1:
            game.deck.populate()
            game.deck.shuffle()
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")

main()
input("\nPress the enter key to exit.")



