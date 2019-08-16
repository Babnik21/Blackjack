%rebase('osnova.tpl')

<style>
#tabela {
  border-spacing: 30px 0;
  margin: 0 auto;
  border-collapse: separate;
}
</style>

    <h1 class="title has-text-white">Pred vami je {{ balance }}€.</h1>

 <table id="tabela">
  <tr>
    <th>
      <form action='/wager/'>
        <input type='submit' class="button is-success is-inverted" value = 'Odigraj hand!'>
      </form>
    </th>
    <th>    
      <form action='/end/'>
        <input type='submit' class="button is-success is-inverted" value = 'Cash out!'>
      </form>
    </th>
  </tr>
</table> 
