import bottle
bottle.TEMPLATE_PATH.insert(0, 'views')
from model import Igra, Hand
import model
import time

game = Igra(0)

@bottle.get('/')
def osnovna():
    game.balance = 0
    return bottle.template('osnovna_stran.tpl')

@bottle.get('/deposit/')
def deposit():
    return bottle.template('deposit.tpl')

@bottle.get('/igra/')
def igra():
    if game.balance == 0:
        deposit = bottle.request.query['deposit']
        if not model.je_stevilka(deposit):
            return bottle.template('deposit_1.tpl')
        elif float(deposit) <= 0:
            return bottle.template('deposit_1.tpl')
        game.balance = float(deposit)
    return bottle.template('igra.tpl', balance=game.balance)

@bottle.get('/wager/')
def wager():
    return bottle.template('wager.tpl')

@bottle.get('/hand/')
def hand():
    wager = bottle.request.query['wager']
    if not model.veljaven_odgovor(wager, game):
        return bottle.template('wager_1.tpl')
    game.new_hand(float(wager))
    dealer = model.spremeni_format_handa(game.roka.dealer_cards, game.roka.dealer_suits)
    player = model.spremeni_format_handa(game.roka.player_cards, game.roka.player_suits)
    if game.roka.player_count == 21:
        bottle.redirect('/razplet/')
    if model.can_double(game):
        return bottle.template('hand_double.tpl', player = player, dealer = dealer)
    else:
        return bottle.template('hand.tpl', player = player, dealer = dealer)

@bottle.post('/hit/')
def hit():
    game.roka.player_hit()
    game.roka.update_counts()
    dealer = model.spremeni_format_handa(game.roka.dealer_cards, game.roka.dealer_suits)
    player = model.spremeni_format_handa(game.roka.player_cards, game.roka.player_suits)
    if game.roka.player_count > 21:
        return bottle.redirect('/razplet/')
    else:
        return bottle.template('hand.tpl', player = player, dealer = dealer)

@bottle.post('/double/')
def double():
    game.roka.player_hit()
    game.roka.update_counts()
    game.roka.wager *= 2
    if game.roka.player_count >= 22:
        bottle.redirect('/razplet/')
    bottle.redirect('/dealer_turn/')


@bottle.get('/dealer_turn/')
def dealer_turn():
    game.roka.dealer_hit()
    game.roka.update_counts()
    dealer = model.spremeni_format_handa(game.roka.dealer_cards, game.roka.dealer_suits)
    player = model.spremeni_format_handa(game.roka.player_cards, game.roka.player_suits)
    if game.roka.dealer_count >= 17:
        bottle.redirect('/razplet/')
    else:
        return bottle.template('dealer_turn.tpl', player = player, dealer = dealer)

@bottle.get('/razplet/')
def razplet():
    dealer = model.spremeni_format_handa(game.roka.dealer_cards, game.roka.dealer_suits)
    player = model.spremeni_format_handa(game.roka.player_cards, game.roka.player_suits)
    if game.player_blackjack() and (game.roka.dealer_count != 21 or len(game.roka.dealer_cards) > 2):
        game.balance += 1.5*game.roka.wager
        return bottle.template('blackjack.tpl', player = player, dealer = dealer, stanje = game.balance)
    elif game.player_won():
        game.balance += game.roka.wager
        return bottle.template('player_won.tpl', player = player, dealer = dealer, stanje = game.balance)
    elif game.dealer_won():
        game.balance -= game.roka.wager
        return bottle.template('dealer_won.tpl', player = player, dealer = dealer, stanje = game.balance)
    else:
        return bottle.template('tie.tpl', player = player, dealer = dealer, stanje = game.balance)

@bottle.get('/end/')
def end():
    return bottle.template('end.tpl', stanje = game.balance)


bottle.run(debug=True, reloader=True)
