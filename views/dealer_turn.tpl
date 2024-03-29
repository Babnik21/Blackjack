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

<h2 class="title has-text-white">{{karte}}</h2>

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


  <form action='/dealer_turn/', method = "post">
    <input type='submit' class="button is-success is-inverted" value='Next'>
  </form>

