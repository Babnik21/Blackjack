import time, sys
from model import Igra, Hand
import model


#popravi da piše v evrih ne '100 denarja'

def igralec_izbira_prva(game, roka):
    #Vpraša igralca, kaj želi s trenutno roko storiti in vrne, rabi popravek
    print(roka)
    print('Kaj želite narediti?')
    print('1) Hit')
    print('2) Stand')
    print('3) Double')
    odgovor = input('> ')
    if len(odgovor) != 1 or odgovor not in '123':
        print('Neveljavna izbira!')
        return igralec_izbira_prva(game, roka)
    else:
        return model.igralec_poteza(roka, odgovor)

def igralec_izbira(game, roka):
    print(roka)
    print('Kaj želite narediti?')
    print('1) Hit')
    print('2) Stand')
    odgovor = input('> ')
    if len(odgovor) != 1 or odgovor not in '12':
        print('Neveljavna izbira!')
        return igralec_izbira(game, roka)
    else:
        return model.igralec_poteza(roka, odgovor)


def vprašaj_po_depositu():
    #Vpraša igralca, koliko denarja želi vložiti za igralno mizo in vrne število
    print('Koliko denarja želite imeti za mizo?')
    odgovor = input('> ')
    if len(odgovor) == 0 or odgovor.count('.') > 1:
        print('Neveljaven vnos')
        return vprašaj_po_depositu()
    for el in odgovor:
        if el not in '1234567890.':
            print('Neveljavna izbira!')
            return vprašaj_po_depositu()
    return float(odgovor)

def pridobi_wager(igra):
    #Vpraša igralca, koliko denarja želi staviti prihodnji hand
    print('Koliko denarja želite staviti naslednjo roko?')
    odgovor = input('> ')
    if len(odgovor) == 0 or odgovor.count('.') > 1:
        print('Neveljavna izbira')
        return pridobi_wager(igra)
    for el in odgovor:
        if el not in '1234567890.':
            print('Neveljavna izbira.')
            return pridobi_wager(igra)
    odgovor = float(odgovor)
    if odgovor > igra.balance:
        print('Neveljavna izbira! Na voljo imate le še {} evrov.'.format(igra.balance))
        return pridobi_wager(igra)
    else:
        return odgovor

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

def nova_igra(cifra):
    #Vrne novo igro
    return Igra(cifra)

def razplet(roka, game):
    #Obvesti igralca o razpletu roke in osveži stanje na računu igralca
    if model.player_blackjack(roka):
        print('Čestitke! Blackjack!')
        game.balance += 1.5 * roka.wager
    elif model.player_won(roka):
        print('Čestitke! Zmagali ste trenutno roko!')
        game.balance += roka.wager
    elif model.dealer_won(roka):
        print('Dealer je zmagal to roko.')
        game.balance -= roka.wager
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

def new_hand(game):
    roka = Hand(pridobi_wager(game))
    roka.update_counts()
    return roka

def odigraj_roko(game):
    #Sestavek kjer igralec odigra roko
    roka = new_hand(game)
    while roka.player_count < 21 and not roka.stand:
        if len(roka.player_cards) == 2:
            roka = igralec_izbira_prva(game, roka)
        else:
            roka = igralec_izbira(game, roka)
        roka.update_counts()
    if roka.player_count <= 21:
        while roka.dealer_count < 17:
            roka.dealer_hit()
            roka.update_counts()
            print(roka)
    razplet(roka, game)

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
    intro()
    while True:
        igra()
        if not play_again():
            break
    print('Hvala za igro!')

program()