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
    deposit = bottle.request.query['deposit']
    game = model.nova_igra(float(deposit))
    while True:
        










bottle.run(debug=True, reloader=True)
