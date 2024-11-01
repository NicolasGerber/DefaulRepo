import  random

def deal_card():
    """Deal a random card from the "cards" list"""
    cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
             "K": 10}
    card_symbol = random.choice(list(cards.keys()))
    card_value = cards[card_symbol]
    return card_symbol, card_value

def calculate_score(card_values):
    """Does the sum of the score of the cards and verifies if the ACE score pass 21, then turning into an 1"""
    score = sum(card_values)
    if score == 21 and len(card_values) == 2:
        return 0
        #the zero value indicates BLACKJACK
    if 11 in card_values and score > 21:
        card_values.remove(11)
        card_values.append(1)

    return sum(card_values)

def compare(p_score, d_score):
    if p_score == d_score:
        return "DRAW!"
    elif d_score == 0:
        return "Dealer has Blackjack. YOU LOSE!!"
    elif p_score == 0:
        return "BLACKJACK!! YOU WIN!!"
    elif p_score > 21:
        return "You pass over 21. YOU LOSE!!"
    elif d_score > 21:
        return "The dealer went over 21. YOU WIN!!"
    elif p_score > d_score:
        return "YOU WIN!!"
    else:
        return "YOU LOSE!!"

def play_game():
    player_hand = []
    dealer_hand = []
    player_hand_values = []
    dealer_hand_values = []
    dealer_score = -1
    player_score = -1

    for _ in range(2):
        card_symbol, card_value = deal_card()
        player_hand.append(card_symbol)
        player_hand_values.append(card_value)

        card_symbol, card_value = deal_card()
        dealer_hand.append(card_symbol)
        dealer_hand_values.append(card_value)

    is_game_over = False
    while not is_game_over:
        player_score = calculate_score(player_hand_values)
        dealer_score = calculate_score(dealer_hand_values)
        print("Player's hand:", player_hand, "Player's score:", "21" if player_score == 0 else player_score)
        print("Dealer's first card:", dealer_hand[0])
        if player_score > 21:
            is_game_over = True
            print("You went over 21. YOU LOSE!!")
            break

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            hit = input("Type 'y' get other card, type 'n' to pass: ")
            if hit == 'y':
                card_symbol, card_value = deal_card()
                player_hand.append(card_symbol)
                player_hand_values.append(card_value)
            else:
                is_game_over = True

    if not is_game_over and player_score <= 21:
        while dealer_score !=0 and dealer_score < player_score:
            card_symbol, card_value = deal_card()
            dealer_hand.append(card_symbol)
            dealer_hand_values.append(card_value)
            dealer_score = calculate_score(dealer_hand_values)
            print("Dealer's hand:", dealer_hand, "Dealer's score:", "21" if dealer_score == 0 else dealer_score)

            input("Show dealer's next card...")


    print(f"Your final hand: {player_hand}, Final score: {'BLACKJACK' if player_score == 0 else player_score}")
    print(f"Dealer's final hand: {dealer_hand}, Final score: {'BLACKJACK' if dealer_score == 0 else dealer_score}")
    print(compare(player_score, dealer_score))

while input("Wanna Play BlackJack?(y/n): ").lower() == 'y':
    play_game()
    input("Press Enter to continue...")
    print("\n" * 20)

