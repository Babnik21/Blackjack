%rebase('osnova.tpl')

<style>
#tabela {
  border-spacing: 30px 0;
  margin: 0 auto;
  border-collapse: separate;
}
</style>

    {{ karte }}
    <h1 class="has-text-white title">Izenačenje. Vaše novo stanje je {{stanje}}€.</h1>
    <h1 class="has-text-white title">Želite igrati ponovno?</h1>

 <table id='tabela'>
  <tr>
    <th>
      <form action='/igra/'>
        <input type='submit' class="button is-success is-inverted" value ='Da'>
      </form>
    </th>
    <th>    
      <form action='/end/'>
        <input type='submit' class="button is-success is-inverted" value ='Ne'>
      </form></th>
  </tr>
</table> 


