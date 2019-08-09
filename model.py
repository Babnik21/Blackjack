from random import choice

class Hand:
    def __init__(self, wager):
        self.wager = wager
        self.stand = False
        self.dealer_cards = [choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])]
        self.player_cards = [choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']), 
        choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])]
        self.player_count = 0
        self.dealer_count = 0
        self.dealer_ace_count = 0
        self.player_ace_count = 0
        
    def update_counts(self):
        #Na novo prešteje vrednost dealerjeve in igralčeve roke
        player_count = self.player_ace_count * -10
        dealer_count = self.dealer_ace_count * -10
        player_aces = self.player_cards.count('A')
        dealer_aces = self.dealer_cards.count('A')
        for el in self.dealer_cards:
            if el in '23456789':
                dealer_count += int(el)
            elif el in 'TQJK':
                dealer_count += 10
            else:
                dealer_count += 11
        if dealer_count > 21 and dealer_aces > self.dealer_ace_count:
            dealer_count -= 10
            self.dealer_ace_count += 1
        for el in self.player_cards:
            if el in '23456789':
                player_count += int(el)
            elif el in 'TQJK':
                player_count += 10
            else:
                player_count += 11
        if player_count > 21 and player_aces > self.player_ace_count:
            player_count -= 10
            self.player_ace_count += 1
        self.player_count = player_count
        self.dealer_count = dealer_count
        
    def player_hit(self):
        #Igralcu doda karto
        self.player_cards.append(choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']))

    def dealer_hit(self):
        #Dealerju doda karto
        self.dealer_cards.append(choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']))      

    def __str__(self):
        moje = ', '.join(self.player_cards)
        dealerjeve = ', '.join(self.dealer_cards)
        prvi_del = 'Vaša roka je ' + moje + ' ({})'.format(self.player_count)
        drugi_del = ', dealer ima ' + dealerjeve + ' ({}).'.format(self.dealer_count)
        return prvi_del + drugi_del

    def konec(self):
        self.stand = True

    def double(self):
        self.player_hit()
        self.wager *= 2
        self.konec()

class Igra:
    def __init__(self, deposit = 5):
        self.balance = deposit
        self.roka = Hand(-1)

    def __str__(self):
        print('Na voljo imate še {} evrov.'.format(self.balance))

    def new_hand(self, wager):
        #Naredi novo roko in jo vrne
        roka = Hand(wager)
        roka.update_counts()
        self.roka = roka

    def update_balance(self, amount):
        self.balance = amount
    
    def dealer_won(self):
        #Preveri, ali je dealer zmagal, vrne True/False
        if self.roka.player_count > 21:
            return True
        elif self.roka.dealer_count > 21:
            return False
        else:
            return self.roka.player_count < self.roka.dealer_count

    def player_won(self):
        #Preveri, ali je igralec zmagal, vrne True/False
        if self.roka.player_count > 21:
            return False
        elif self.roka.dealer_count > 21:
            return True
        else:
            return self.roka.player_count > self.roka.dealer_count

    def player_blackjack(self):
        #Preveri, ali ima igralec Blackjack ali ne
        if self.roka.player_count != 21 or len(self.roka.player_cards) != 2:
            return False
        else:
            return self.roka.dealer_count != 21 or len(self.roka.dealer_cards) != 2

def nova_igra(cifra):
    #Vrne novo igro
    return Igra(cifra)

def igralec_poteza(game, odgovor):
    #Sprejme odgovor uporabnika in opravi potezo (hit/stand...)
    if odgovor == '1':
        game.roka.player_hit()
    elif odgovor == '2':
        game.roka.konec()
    else:
        game.roka.player_hit()
        game.roka.stand = True
        game.roka.wager *= 2
    return game.roka
    



def can_double(game):
    return len(game.roka.player_cards) == 2 and game.balance >= 2*game.roka.wager