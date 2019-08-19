% import model
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



 <table id='tabela'>
  <tr>
    <th>
      <form action='/hit/' method='post'>
        <input type='submit' class="button is-success is-inverted" value = 'Hit'>
      </form>
    </th>
    <th>
      <form action='/dealer_turn/'>
        <input type='submit' class="button is-success is-inverted" value = 'Stand'>
      </form>
    </th>
    <th>
      <form action='/double/' method='post'>
        <input type='submit' class="button is-success is-inverted" value = 'Double'>
      </form>
    </th>
  </tr>
</table> 




<div id="ocka">

</div>