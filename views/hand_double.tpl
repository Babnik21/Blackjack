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
    <form action='/stand/'>
      <input type='submit' value = 'Stand'>
    </form>
    <form action='/double/'>
      <input type='submit' value = 'Double'>
    </form>
  </body>
</html>
