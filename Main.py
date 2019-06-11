from random import shuffle


class Shoe:
    deck = [1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3, 3,
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            8, 8, 8, 8,
            9, 9, 9, 9,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10]
    total_deck = []

    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.total_deck = self.new_shoe()

    def draw_card(self):
        return self.total_deck.pop()

    def size(self):
        return len(self.total_deck)

    def needs_shuffle(self):
        return self.size() <= self.num_decks * 52 * .18

    def new_shoe(self):
        for i in range(self.num_decks):
            self.total_deck += self.deck
        shuffle(self.total_deck)
        return self.total_deck



def main():
    s = Shoe(6)
    for i in range(2000):
        if s.needs_shuffle():
            s.new_shoe()
        print("card is : " + str(s.draw_card()))
        print("size is " + str(s.size()))


if __name__ == "__main__":
    main()