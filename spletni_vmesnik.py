import bottle
bottle.TEMPLATE_PATH.insert(0, 'views')
from model import Igra, Hand
import model
import time

game = model.nova_igra(5)

@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.tpl')

@bottle.get('/deposit/')
def deposit():
    return bottle.template('deposit.tpl')

@bottle.get('/igra/')
def igra():
    deposit = float(bottle.request.query['deposit'])
    game.update_balance(deposit)
    return bottle.template('igra.tpl', deposit = deposit)

@bottle.get('/wager/')
def get_wager():
    return bottle.template('wager.tpl')


@bottle.get('/cash_out/')
def cash_out():
    return bottle.template('cash_out.tpl')

@bottle.get('/hand/')
def odigraj_hand():
    if game.roka.wager == -1:
        stava = float(bottle.request.query['wager'])
        game.new_hand(stava) 
    if model.can_double(game):
        return bottle.template('hand_double.tpl', karte = game.roka)
    else:
        return bottle.template('hand.tpl', karte = game.roka)

@bottle.get('/hit/')
def hit():
    game.roka.player_hit()
    game.roka.update_counts()
    return bottle.template('hand.tpl', karte = game.roka)

@bottle.get('/dealer_turn/')
def stand():
    game.roka.dealer_hit()
    game.roka.update_counts()
    return bottle.template('dealer_turn.tpl', karte = game.roka)









bottle.run(debug=True, reloader=True)
