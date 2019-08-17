%rebase('osnova.tpl')

<style>
#tabela {
  border-spacing: 30px 0;
  margin: 0 auto;
  border-collapse: separate;
}
</style>

 <table id='karte'>
  <tr>
    <th>
% for el in player:
    <img src="https://deckofcardsapi.com/static/img/{{el}}.png">
% end
    </th>
    <th>
% for el in dealer:
    <img src="https://deckofcardsapi.com/static/img/{{el}}.png">
% end

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

