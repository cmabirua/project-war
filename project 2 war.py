#Card
#suit,rank,value
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#here we will create the dic for values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit


#deck class

class Deck:
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []

        for suit in suits:
            for rank in ranks :
                #create the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

new_deck = Deck()   
new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard)
bottom_card = new_deck.all_cards[-1]
print(bottom_card)
new_deck.shuffle()

for card_object in new_deck.all_cards:
    print(card_object)
print(new_deck.all_cards[0])
print(len(new_deck.all_cards))

#player Class
class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []#this have empty list..we need to add and remove the card 
    
    def remove_one(self):
        return self.all_cards.pop(0)#it will pop from the top of the card deck
    
    def add_cards(self,new_cards):#new card can either be single card obj or a list of card obj
        if type(new_cards) == type([]):#newcard is empty then add multiple card
            self.all_cards.extend(new_cards)#we have multiple card object
        
        else:#we have single card object
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f'Player {self.name} : has {len(self.all_cards)} cards.'

new_player = Player ("JOSE")
print(new_player)
new_player.add_cards(mycard)#adding single card
print(mycard)
print(new_player)
print(new_player.all_cards[0])
new_player.add_cards([mycard,mycard,mycard])#adding multiple card
print(new_player)
new_player.remove_one()#it removed one card from mycard
print(new_player)#here we get 3 card

#game logic
#game setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()#shuffle the deck

#split the deck
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
#while game_on
round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    #check if a player is out of card
    if len(player_one.all_cards) == 0:
        print('Player One,Out of cards! Player Two Wins !!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two,Out of cards! Player One Wins !!')
        game_on = False
        break
# Otherwise, the game is still on!
    #start a new Round #continue
    player_one_card = []
    player_one_card.append(player_one.remove_one())
    player_two_card = []
    player_two_card.append(player_two.remove_one())


#while at_war #still game is continue by adding each other card
at_war = True

while at_war:

    if player_one_card[-1].values > player_two_card[-1].values:
        #player one get the card
        player_one.add_cards(player_one_card)
        player_one.add_cards(player_two_card)

#no longer at war,time for next round
        at_war = False
     #player two has hidher card   
    elif player_one_card[-1].values < player_two_card[-1].values:
       #player two has hidher card
        player_two.add_cards(player_one_card)
        player_two.add_cards(player_two_card)
       #no longer at two ,time for next round
        at_war = False 

    else:
       print('WAR!') 
       #this occue when the card are equal
       #we will grab another card each and continue the current war.

         #if player has 5 card then it looses
       if len(player_one.all_cards) < 5:
           print("Player One unable to declae war")
           print("Player Two WINS!!")
           game_on = False#game end
           break#break will end overall while loop
       
       elif len(player_two.all_cards) < 5:
           print("Player Two unable to declae war")
           print("Player One WINS!!")
           game_on = False#game end
           break#break will end overall while loop
       #otherwise were still at war,so we will add the next card
       else:
           for num in range(5):
               player_one_card.append(player_one.remove_one())
               player_two_card.append(player_two.remove_one())
               
    
      
       