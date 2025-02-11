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

    