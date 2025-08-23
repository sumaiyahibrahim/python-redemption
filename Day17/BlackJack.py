import random

# ---------- GLOBAL CONSTANTS ----------
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
    'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11
}

# ---------- CLASSES ----------

# A single card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# A deck of 52 cards
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


# A hand for player or dealer
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0  # Sum of card values
        self.aces = 0   # Count of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces += 1

        self.adjust_for_ace()

    def adjust_for_ace(self):
        # If total > 21 and there's an Ace, treat Ace as 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Chips & Betting System
class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# ---------- GAME FUNCTIONS ----------

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much would you like to bet? "))
        except ValueError:
            print("⚠️ Please enter a number.")
        else:
            if chips.bet > chips.total:
                print(f"⚠️ You don't have enough chips! You have: {chips.total}")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    global playing

    while True:
        choice = input("Hit or Stand? (h/s): ").lower()
        if choice == 'h':
            hit(deck, hand)
        elif choice == 's':
            print("Player stands. Dealer's turn.")
            playing = False
        else:
            print("⚠️ Enter 'h' or 's' only.")
            continue
        break
 

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <hidden card>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand Value:", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand Value:", player.value)


# WIN/LOSE FUNCTIONS
def player_busts(chips):
    print("❌ Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("✅ Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("✅ Dealer busts, player wins!")
    chips.win_bet()

def dealer_wins(chips):
    print("❌ Dealer wins!")
    chips.lose_bet()

def push():
    print("🤝 It's a tie! PUSH.")


# ---------- GAME LOGIC ----------
playing = True

while True:
    print("=== Welcome to Blackjack! 🃏 Try to get as close to 21 as you can ===")

    # Create & shuffle deck
    deck = Deck()
    deck.shuffle()

    # Deal cards
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Setup chips
    player_chips = Chips()

    # Bet
    take_bet(player_chips)

    # Show cards
    show_some(player_hand, dealer_hand)

    while playing:
        # Ask to hit or stand
        hit_or_stand(deck, player_hand)

        # Show cards (1 hidden from dealer)
        show_some(player_hand, dealer_hand)

        # If player busts
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # Dealer's turn
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        # Compare hands
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    # Show total chips
    print(f"\n💰 Player's chips total: {player_chips.total}")

    # Replay?
    new_game = input("Play another round? (y/n): ")
    if new_game.lower() != 'y':
        print("Thanks for playing! 🎉")
        break
    else:
        playing = True
