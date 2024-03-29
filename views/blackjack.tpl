%rebase('osnova.tpl')

<style>
#tabela {
  border-spacing: 30px 0;
  margin: 0 auto;
  border-collapse: separate;
}
#karte {
  border-spacing: 80px 0;
  margin: 0 auto;
  border-collapse: separate;
}

.ocka {
  position: relative;
  min-height: 500px;
}

.ocka img {
  position: absolute;
  width: 200px;
}
</style>


<table id='karte'>
  <tr>
    <th>
    <div class="ocka" style="width: {{120 + len(player)*80}}px; height: {{197.883 + max(len(player), len(dealer)) * 80}}px">
% for i, el in enumerate(player):
    <img src="https://deckofcardsapi.com/static/img/{{el}}.png" style="left: {{i*80}}px; top: {{i*80}}px">
% end
  </div>
    </th>
    <th>
    <div class="ocka" style="width: {{120 + len(dealer)*80}}px">
% for i, el in enumerate(dealer):
    <img src="https://deckofcardsapi.com/static/img/{{el}}.png" style="left: {{i*80}}px; top: {{i*80}}px">
% end
  </div>

    </th>
  </tr>
</table>  

    <h1 class="has-text-white title">Čestitke! Blackjack! Vaše novo stanje je {{stanje}}.</h1>

    <h1 class="has-text-white title">Želite igrati ponovno?</h1>
     <table id="tabela">
  <tr>
    <th>    
      <form action='/igra/'>
        <input type='submit' class="button is-success is-inverted" value ='Da'>
      </form>
    </th>
    <th>
          <form action='/end/'>
      <input type='submit' class="button is-success is-inverted" value ='Ne'>
    </form>
    </th>
  </tr>
</table> 

