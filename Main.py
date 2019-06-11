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
        for i in range(num_decks):
            self.total_deck += self.deck
        shuffle(self.total_deck)

    def draw_card(self):
        return self.total_deck.pop()

    def size(self):
        return len(self.total_deck)


def main():
    shoe = Shoe(6)
    for i in range(52 * 6):
        print(shoe.draw_card())
        print(shoe.size())


if __name__ == "__main__":
    main()