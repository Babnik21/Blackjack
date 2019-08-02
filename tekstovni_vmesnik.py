import time, sys
from model import Igra, Hand
import model


#blablba


def igralec_izbira(game, roka):
    #Vpraša igralca, kaj želi s trenutno roko storiti in vrne, rabi popravek
    print(roka)
    print('Kaj želite narediti?')
    print('1) Hit')
    print('2) Stand')
    print('3) Double')
    odgovor = input('> ')
    if len(odgovor) != 1 or odgovor not in '123':
        print('Neveljavna izbira!')
        return igralec_izbira(game, roka)
    else:
        return model.igralec_poteza(roka, odgovor)



def vprašaj_po_depositu():
    #Vpraša igralca, koliko denarja želi vložiti za igralno mizo in vrne število
    print('Koliko denarja želite imeti za mizo?')
    odgovor = input('> ')
    for el in odgovor:
        if el not in '1234567890':
            print('Neveljavna izbira!')
            return vprašaj_po_depositu()
    return int(odgovor)

def pridobi_wager(igra):
    #Vpraša igralca, koliko denarja želi staviti prihodnji hand
    print('Koliko denarja želite staviti naslednjo roko?')
    odgovor = input('> ')
    for el in odgovor:
        if el not in '1234567890':
            print('Neveljavna izbira.')
            return pridobi_wager(igra)
    odgovor = int(odgovor)
    if odgovor > igra.balance:
        print('Neveljavna izbira! Na voljo imate le še {} evrov.'.format(igra.balance))
        return pridobi_wager(igra)
    else:
        return odgovor

def play_again():
    print('Ali želite igrati ponovno?')
    print('1) Da')
    print('2) Ne')

def nova_igra():
    #Vrne novo igro
    return Igra(vprašaj_po_depositu())

def razplet(roka, game):
    #Obvesti igralca o razpletu roke in osveži stanje na računu igralca
    if model.player_won(roka):
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

def odigraj_roko(game):
    #Sestavek kjer igralec odigra roko
    roka = Hand(pridobi_wager(game))
    while roka.player_count < 21 and not roka.stand:
        roka.update_counts()
        roka = igralec_izbira(game, roka)
    if roka.player_count <= 21:
        while roka.dealer_count < 17:
            roka.update_counts()
            roka.dealer_hit()
    razplet(roka, game)

def igra():
    #Celotna igra
    game = nova_igra()
    while game.balance >= 0:
        odigraj_roko(game)
        if cash_out(game):
            break
    print('Vaše končno stanje je {} evrov. Hvala za igro!'.format(game.balance))
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

program()