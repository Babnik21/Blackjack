class Igra:
    def __init__(self, deposit):
        self.balance = deposit

    def __str__(self):
        print('Na voljo imate še {} evrov.'.format(self.balance))


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
        
    def update_counts(self):
        player_count = 0
        dealer_count = 0
        for el in self.dealer_cards:
            if el in '23456789':
                dealer_count += int(el)
            elif el in 'TQJK':
                dealer_count += 10
            else:
                dealer_count += 11
        for el in self.dealer_cards:
            if dealer_count > 21 and el == 'A':
                dealer_count -= 10
        for el in self.player_cards:
            if el in '23456789':
                player_count += int(el)
            elif el in 'TQJK':
                player_count += 10
            else:
                player_count += 11
        for el in self.player_cards:
            if player_count > 21 and el == 'A':
                player_count -= 10
        self.player_count = player_count
        self.dealer_count = dealer_count
        
    def player_hit(self):
        self.player_cards.append(choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']))

    def dealer_hit(self):
        self.dealer_cards.append(choice(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']))      

    def __str__(self):
        return 'Vaša roka je {}, dealer ima {}'.format(self.player_cards, self.dealer_cards)

def igralec_poteza(roka, odgovor):
    if odgovor == '1':
        roka.player_hit()
    elif odgovor == '2':
        roka.stand = True
    else:
        roka.player_hit()
        roka.stand = True
        roka.wager *= 2
    return roka
        
def player_won(roka):
    if roka.player_count > 21:
        return False
    elif roka.dealer_count > 21:
        return True
    else:
        return roka.player_count > roka.dealer_count

def dealer_won(roka):
    if roka.player_count > 21:
        return True
    elif roka.dealer_count > 21:
        return False
    else:
        return roka.player_count < roka.dealer_count

