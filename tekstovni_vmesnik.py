import time
from model import Igra, Hand
import model




def igralec_izbira_prva(game):
    #Vpraša igralca, kaj želi s trenutno roko storiti in to izvede
    #Uporabljena le za prvič, ko je igralec na potezi, saj kasneje 'double' ni mogoč
    print(game.roka)
    print('Kaj želite narediti?')
    print('1) Hit')
    print('2) Stand')
    print('3) Double')
    odgovor = input('> ')
    if len(odgovor) != 1 or odgovor not in '123':
        print('Neveljavna izbira!')
        return igralec_izbira_prva(game)
    else:
        return model.igralec_poteza(game, odgovor)

def igralec_izbira(game):
    #Podobno kot igralec_izbira_prva, le da brez možnosti 'double'
    print(game.roka)
    print('Kaj želite narediti?')
    print('1) Hit')
    print('2) Stand')
    odgovor = input('> ')
    if len(odgovor) != 1 or odgovor not in '12':
        print('Neveljavna izbira!')
        return igralec_izbira(game)
    else:
        return model.igralec_poteza(game, odgovor)


def vprašaj_po_depositu():
    #Vpraša igralca, koliko denarja želi vložiti za igralno mizo in vrne to število
    print('Koliko evrov želite imeti za mizo?')
    odgovor = input('> ')
    if len(odgovor) == 0 or odgovor.count('.') > 1:
        print('Neveljaven vnos.')
        return vprašaj_po_depositu()
    for el in odgovor:
        if el not in '1234567890.':
            print('Neveljaven vnos.')
            return vprašaj_po_depositu()
    return float(odgovor)

def pridobi_wager(game):
    #Vpraša igralca, koliko denarja želi staviti prihodnji hand, in vrne to število
    print('Koliko želite staviti naslednjo roko?')
    odgovor = input('> ')
    if not model.veljaven_odgovor(odgovor, game):
        print('Neveljavna izbira.')
        return pridobi_wager(game)
    else:
        return float(odgovor)

def play_again():
    #Vpraša igralca, če želi igrati ponovno, vrne True/False
    print('Ali želite igrati ponovno?')
    print('1) Da')
    print('2) Ne')
    odgovor = input('> ')
    if len(odgovor) != 1 or odgovor not in '12':
        print('Neveljaven odgovor.')
        return play_again()
    elif odgovor == '1':
        return True
    else:
        return False

def razplet(game):
    #Obvesti igralca o razpletu roke in osveži stanje na računu igralca
    if game.player_blackjack():
        print('Čestitke! Blackjack!')
        game.balance += 1.5 * game.roka.wager
    elif game.player_won():
        print('Čestitke! Zmagali ste trenutno roko!')
        game.balance += game.roka.wager
    elif game.dealer_won():
        print('Dealer je zmagal to roko.')
        game.balance -= game.roka.wager
    else:
        print('Izenačenje!')

def cash_out(game):
    #Igralca vpraša ali želi nadaljevati z igro ali ne, vrne True/False
    print('Ali želite nadaljevati z igro? Trenutno imate {} evrov.'.format(game.balance))
    print('1) Da')
    print('2) Ne')
    izbira = input('> ')
    if izbira == '1':
        return False
    elif izbira == '2':
        return True
    else:
        print('Neveljavna izbira!')
        return cash_out(game)

def odigraj_roko(game):
    #Sestavek kjer igralec odigra roko
    game.new_hand(pridobi_wager(game))
    while game.roka.player_count < 21 and not game.roka.stand:
        if model.can_double(game):
            game.roka = igralec_izbira_prva(game)
        else:
            game.roka = igralec_izbira(game)
        game.roka.update_counts()
    if game.roka.player_count <= 21:
        while game.roka.dealer_count < 17:
            game.roka.dealer_hit()
            game.roka.update_counts()
            print(game.roka)
    razplet(game)

def igra():
    #Celotna igra
    game = model.nova_igra(vprašaj_po_depositu())
    while True:
        odigraj_roko(game)
        if game.balance == 0:
            print('Imate 0 evrov.')
            break
        elif cash_out(game):
            break
    print('Vaše končno stanje je {} evrov.'.format(game.balance))
    time.sleep(2)

def intro():
    print('Pozdravljeni v igri blackjack!')
    print('Igrajte le s toliko denarja, kot ga lahko izgubite.')
    print('Če nimate vsaj 18 let, zapustite igro na tej točki.')
    time.sleep(3)

def program():
    #Main
    intro()
    while True:
        igra()
        if not play_again():
            break
    print('Hvala za igro!')

program()