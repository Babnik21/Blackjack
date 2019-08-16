%rebase('osnova.tpl') 

<style>
#tabela {
  border-spacing: 30px 0;
  margin: 0 auto;
  border-collapse: separate;
}
</style>

    <h2 class="subtitle has-text-white>"Neveljavna izbira!</h2>
    <h1 class="title has-text-white">Koliko denarja želite staviti naslednji hand?</h1>

    <form action='/hand/', method="push">
      <div class="control">
        <h2 class="subtitle has-text-white">Stava:<input class="input" type="text" placeholder="vpišite število" name='wager'></h2> 
      </div>
    </form>
