<template>
  <div class="cont">
    <div class="page">
      <div class="base">
        <div class="titulo">
          <h1>Historico de Sucata</h1>
          <hr />
        </div>
        <div class="cards">
          <div v-for="his in HisList.data" :key="his.id" class="card-one c">
            <h1>{{ his.txtBreve }}</h1>
            <h4>{{ his.desc }}</h4>
            <h4>{{ his.trab}}</h4>
            <h4>{{ his.dataInser }}</h4>
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
      HisList: [],
      dataReady: false,
    }
  },
  methods: {
    getHisSucata: async function () {
      await axios
        .get('http://localhost:8000/TransacaoSucata/?id=' + this.$auth.user.id)
        .then((response) => {
          let data = response
          this.HisList = data.data
          this.dataReady = true
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },

  mounted: async function () {
    this.getHisSucata()
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/hist_produto/hist_produto.scss';
</style>



