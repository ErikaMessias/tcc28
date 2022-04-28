<template>
  <div class="cont">
    <headers />
    <div class="page">
      <div class="base">
        <div class="titulo">
          <h1>Transações</h1>
          <hr />
        </div>
        <div class="cards">
          <div class="card-one c">
            <h1>Descarte de Sucata</h1>
            <img src="/sucata.png" />
            <NuxtLink class="btn-ir" to="/cod_sucata">Selecionar</NuxtLink>
          </div>

          <div class="card-two c">
            <h1>Solicitar Produtos</h1>
            <img src="/produto.png" />
            <NuxtLink class="btn-ir" to="/consulta_produto">Selecionar</NuxtLink>
          </div>
        </div>
      </div>
    </div>
    <footers />
  </div>
</template>

<script>
export default {
  name: 'trancoes',
  middleware: 'auth',
}
</script>

<style lang="scss" scoped>
@import '@/pages/transacoes/transacoes.scss';


@media (max-width: 500px) {
  .base{
    margin-top: 3%;
    width: 80%;
  }
}
</style>

