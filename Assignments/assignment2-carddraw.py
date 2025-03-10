import requests

# Shuffle a new deck of cards
shuffle_response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
deck_id = shuffle_response.json()['deck_id']

# Draw 5 cards from the shuffled deck change count dependig on how many cards you want to draw
draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")
cards = draw_response.json()['cards']

# Print the value and suit of each card
for card in cards:
    print(f"{card['value']} of {card['suit']}")

# Check for pairs, triples, straights, or same suit
values = [card['value'] for card in cards]
suits = [card['suit'] for card in cards]

# Check for pairs or triples
value_counts = {value: values.count(value) for value in set(values)}
pairs = sum(1 for count in value_counts.values() if count == 2)
triples = sum(1 for count in value_counts.values() if count == 3)
quads = sum(1 for count in value_counts.values() if count == 4)


# Check for all same suit
same_suit = len(set(suits)) == 1

# Check for straight
value_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JOKER', 'QUEEN', 'KING', 'ACE']
sorted_values = sorted(values, key=lambda x: value_order.index(x))
is_straight = all(value_order.index(sorted_values[i]) + 1 == value_order.index(sorted_values[i + 1]) for i in range(len(sorted_values) - 1))

# Congratulate the user based on the results
if pairs > 0:
    print(f"Congratulations! You have {pairs} pair(s).")
if triples > 0:
    print(f"Congratulations! You have {triples} triple(s).")
if quads > 0:
    print(f"Congratulations! You have {quads} quad(s).")
if same_suit:
    print("Congratulations! All your cards are of the same suit.")
if is_straight:
    print("Congratulations! You have a straight.")