import bottle
bottle.TEMPLATE_PATH.insert(0, 'views')
from model import Igra, Hand
import model
import time


@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.tpl')

 
@bottle.get('/deposit/')
def deposit():
    return bottle.template('deposit.tpl')

@bottle.get('/igra/')
def igra():
    deposit = float(bottle.request.query['deposit'])
    game = model.nova_igra(float(deposit))
    return bottle.template('igra.tpl', deposit = deposit)

@bottle.get('/cash_out/')
def cash_out():
    return bottle.template('cash_out.tpl')

@bottle.get('/odigraj_hand/')
def odigraj_hand():
    return bottle.template('odigraj_hand')










bottle.run(debug=True, reloader=True)
