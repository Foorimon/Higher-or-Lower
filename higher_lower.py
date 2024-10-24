import random

class Card:
    
    #Represents a playing card with a suit and rank.
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, rank):

        if not (suit in Card.suits and rank in Card.ranks):
            raise ValueError("Invalid card: " + str(suit) + " " + str(rank))

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def card_str(self):
        if self.rank == "10":
            return f"""
            ┌─────┐
            │10   │
            │  {self.suit}  │
            │   10│
            └─────┘
            """
        else:
            return f"""
            ┌─────┐
            │{self.rank}    │
            │  {self.suit}  │
            │    {self.rank}│
            └─────┘
            """ 

class Deck:

    #Initializes a Deck object with a full deck of 52 cards.
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def debug_print_deck(self):
        for card in self.cards:
            print(card.card_str())
    
    def deal(self, num_cards = 1):
        return self.cards.pop()

deck = Deck()
deck.shuffle()
score = 0
user_score = 0
Playing = True

while Playing:
    if len(deck.cards) < 2:
        deck.shuffle()
        print ("deck shuffled")
    print ("you draw")
    seen_card = deck.deal()
    revealed_card_rank = seen_card.rank
    revealed_card_suit = seen_card.suit
    print (seen_card.card_str())
    lose = False
    concealed_card = deck.deal()
    hidden_card_rank = concealed_card.rank
    hidden_card_suit = seen_card.suit
    
    if revealed_card_rank == "A":
        revealed_card_rank = "1"
    if revealed_card_rank == "J":
        revealed_card_rank = "11"
    if revealed_card_rank == "Q":
        revealed_card_rank = "12"
    if revealed_card_rank == "K":
        revealed_card_rank = "13"

    if hidden_card_rank == "A":
        hidden_card_rank = "1"
    if hidden_card_rank == "J":
        hidden_card_rank = "11"
    if hidden_card_rank == "Q":
       hidden_card_rank = "12"
    if hidden_card_rank == "K":
        hidden_card_rank = "13"
    
    if revealed_card_suit == "♠":
        revealed_card_suit = "1"
    if revealed_card_suit == "♦":
        revealed_card_suit = "2"
    if revealed_card_suit == "♣":
        revealed_card_suit = "3"
    if revealed_card_suit == "♥":
        revealed_card_suit = "4"

    
    if hidden_card_suit == "♠":
        hidden_card_suit = "1"
    if hidden_card_suit == "♦":
        hidden_card_suit = "2"
    if hidden_card_suit == "♣":
        hidden_card_suit = "3"
    if hidden_card_suit == "♥":
        hidden_card_suit = "4"
        
    here = True
    while here:
        answer = input("higher or lower \n")
        if answer == "h":
            if (int(revealed_card_rank) < int(hidden_card_rank)):
                score = score + 1
                print ("well done the hidden card was", concealed_card.card_str(), "\nyou have a score of", score,"\n")
                here = False
            elif (int(revealed_card_rank) > int(hidden_card_rank)):
                print ("its over, the card was", concealed_card.card_str(), "\nyou had a score of", score, "now its all gone\n")
                score = 0
                here = False
            elif (int(revealed_card_suit) < int(hidden_card_suit)):
                score = score + 1
                print ("well done the hidden card was", concealed_card.card_str(), "\nyou have a score of", score,"\n")
                here = False
            else:
                print ("its over, the card was", concealed_card.card_str(), "\nyou had a score of", score, "now its all gone\n")
                score = 0
                here = False

        elif answer == "l":
            if (int(revealed_card_rank) > int(hidden_card_rank)):
                score = score + 1
                print ("well done the hidden card was", concealed_card.card_str(), "\nyou have a score of", score,"\n")
                here = False
            elif (int(revealed_card_rank) < int(hidden_card_rank)):
                print ("its over, the card was", concealed_card.card_str(), "\nyou had a score of", score, "now its all gone\n")
                score = 0
                here = False
            elif (int(revealed_card_suit) > int(hidden_card_suit)):
                score = score + 1
                print ("well done the hidden card was", concealed_card.card_str(), "\nyou have a score of", score,"\n")
                here = False
            else:
                print ("its over, the card was", concealed_card.card_str(), "\nyou had a score of", score, "now its all gone\n")
                score = 0
                here = False
                
        else:
            print("its l or h im lazy\n")
        check = True
    here = True
    while here:
        if score == 0:
            staying = input ("wanna play again? \n")
            if staying == "y":
                print ("good luck\n")
                here = False
                check = False
            elif staying == "n":
                print ("see u\n")
                Playing = False
                here = False
                check = False
            else:
                print("its y or n im lazy\n")
        if check:      
            leave = input("do you wanna leave \n")
            if leave == "y":
                Playing = False
                print("your score is", score)
                here = False
            elif leave == "n":
                here = False
            else:
                print("its y or n im lazy\n")



