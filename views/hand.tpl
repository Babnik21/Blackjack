% import model
% end
<html>
  <head>
    <title>Blackjack</title>
  </head>
  <body>
  {{karte}}
    <form action='/hit/'>
      <input type='submit' value = 'Hit'>
    </form>
    <form action='/dealer_turn/'>
      <input type='submit' value = 'Stand'>
    </form>
  </body>
</html>
