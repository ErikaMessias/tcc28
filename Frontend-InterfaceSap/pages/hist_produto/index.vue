<template>
  <div class="cont">
    <div class="page">
      <div class="base">
        <div class="titulo">
          <h1>Historico de Produtos</h1>
          <hr />
        </div>
        <div class="cards">
          <div v-for="prod in prodList.data" :key="prod.id"  class="card-one c">
            <h1>{{ prod.material }}</h1>
            <h4>{{ prod.quantidade }}</h4>
            <h4>{{ prod.recebedor }}</h4>
            <h4>{{ prod.dataIInsercao }}</h4>
            <NuxtLink class="btn-ir" to="#">Add foto</NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'hist_produto',
  layout: 'standard',
  middleware: 'auth',

  data() {
    return {
      prodList: [],
      dataReady: false,
    }
  },
  methods: {
    getHisProd: async function () {
      await axios
        .get('http://localhost:8000/TransacaoProduto/?id_user=' + this.$auth.user.id)
        .then((response) => {
          console.log(this.$auth.user.id)
          let data = response
          this.prodList = data.data
          this.dataReady = true

        })
        .catch((err) => {
          console.log(err)
        })
    },
  },

  mounted: async function () {
    this.getHisProd()
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/hist_produto/hist_produto.scss';
</style>
