% import model
% end
%rebase('osnova.tpl')

<style>
#tabela {
  border-spacing: 30px 0;
  margin: 0 auto;
  border-collapse: separate;
}
</style>

  {{karte}}

 <table id="tabela">
  <tr>
    <th>
      <form action='/hit/'>
        <input type='submit' class="button is-success is-inverted" value = 'Hit'>
      </form>
    </th>
    <th>
      <form action='/dealer_turn/'>
        <input type='submit' class="button is-success is-inverted" value = 'Stand'>
      </form>
    </th>
  </tr>
</table> 




