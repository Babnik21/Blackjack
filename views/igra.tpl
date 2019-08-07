<html>
  <head>
    <title>Blackjack</title>
  </head>
  <body>
    Usedli ste se za mizo, pred vami je {{ deposit }}.

    <form action='/odigraj_hand/'>
      <input type='submit' value = 'Odigraj hand!'>
    </form>

    <form action='/cash_out/'>
      <input type='submit' value = 'Cash out!'>
    </form>
  </body>
</html>