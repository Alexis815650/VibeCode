import random

# Card values and suits
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

def card_value(card):
    rank, _ = card
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11  # Initially consider Ace as 11, will adjust later if needed
    else:
        return int(rank)

def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        val = card_value(card)
        value += val
        if card[0] == 'A':
            aces += 1
    # Adjust for aces if value > 21
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(hand, hide_first=False):
    if hide_first:
        return "[Hidden], " + ", ".join(f"{rank} of {suit}" for rank, suit in hand[1:])
    else:
        return ", ".join(f"{rank} of {suit}" for rank, suit in hand)

def blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Dealer's hand:", display_hand(dealer_hand, hide_first=True))
    print("Your hand:", display_hand(player_hand))
    print("Your hand value:", hand_value(player_hand))

    # Player's turn
    while True:
        if hand_value(player_hand) == 21:
            print("Blackjack! You have 21.")
            break
        choice = input("Hit or Stand? (h/s): ").strip().lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            print("You drew:", f"{player_hand[-1][0]} of {player_hand[-1][1]}")
            print("Your hand:", display_hand(player_hand))
            print("Your hand value:", hand_value(player_hand))
            if hand_value(player_hand) > 21:
                print("You busted! Dealer wins.")
                return
        elif choice == 's':
            break
        else:
            print("Please enter 'h' to Hit or 's' to Stand.")

    # Dealer's turn
    print("\nDealer's turn:")
    print("Dealer's hand:", display_hand(dealer_hand))
    print("Dealer's hand value:", hand_value(dealer_hand))

    while hand_value(dealer_hand) <= 16:
        dealer_hand.append(deck.pop())
        print("Dealer hits and draws:", f"{dealer_hand[-1][0]} of {dealer_hand[-1][1]}")
        print("Dealer's hand:", display_hand(dealer_hand))
        print("Dealer's hand value:", hand_value(dealer_hand))

    dealer_total = hand_value(dealer_hand)
    player_total = hand_value(player_hand)

    if dealer_total > 21:
        print("Dealer busted! You win!")
    else:
        print("\nFinal hands:")
        print("Dealer's hand:", display_hand(dealer_hand), "Value:", dealer_total)
        print("Your hand:", display_hand(player_hand), "Value:", player_total)
        if dealer_total >= player_total:
            print("Dealer wins!")
        else:
            print("You win!")

if __name__ == "__main__":
    blackjack()
