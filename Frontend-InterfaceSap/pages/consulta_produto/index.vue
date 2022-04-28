// Consulta Produto

<template>
  <div class="cont">
    <headers />
    <div class="principal">
      <div class="base">
        <h1>Consulta de Disponibilidade</h1>
        <div class="centro">
          <input
            type="text"
            name="search"
            v-model="produto.searchs"
            class="inputs"
            id="input1"
            placeholder="Nome do Produto"
            v-on:focus="produto.search_num = ''"
          />
          <input
            type="text"
            name="search_num"
            v-model="produto.search_num"
            class="inputs"
            id="input1"
            placeholder="Número"
            v-on:focus="produto.searchs = ''"
          />
         <button v-if="produto.searchs.length> 2 || produto.search_num.length > 4" type="submit" @click="produtoConsulta"> 
            <i
              v-if="load"
              class="pi pi-spin pi-spinner"
              style="font-size: 1rem"
            ></i>
            <span v-else> Buscar </span>
          </button>

          <button v-if="btn_solicita" @click="checkDetails()">Selecionar</button>
          <button @click="checkDetails()" v-else class="btn" to="#">
            Selecionar
          </button>
        </div>
        <tr v-if="titulo" class="tabela_titulo">
          <td class="tit1">Codigo</td>
          <td class="tit2">Nome Produto</td>
          <td class="tit3">Disponibilidade</td>
        </tr>

        <tr v-else></tr>

        <table class="tabela" style="width: 100%">
          <tr
            @click="select_lin(index, $event)"
            :class="colorRow"
            v-for="(linha, index) in produtos"
            :key="index"
            :id="'tr-' + index"
          >
            <td class="lin1">{{ linha[0] }}</td>
            <td class="lin2">{{ linha[2] }}</td>
            <td class="lin3">{{ linha[1] }}</td>
          </tr>
        </table>
      </div>
    </div>
    <footers />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  middleware: 'auth',
  data() {
    return {
      produtos: [],
      produto: {
        searchs: '',
        search_num: '',
      },
      currentSelected: {},
      load: false,
      btn_solicita: false,
      titulo: false,
      rowSelected: false,
      rowEvent: null,
    }
  },

  methods: {
    produtoConsulta: async function () {
      this.load = true
      this.titulo = true
      let pesquisa = ''
      if (this.produto.searchs !== '')
        pesquisa = 'produto_name=' + this.produto.searchs
      else pesquisa = 'produto_num=' + this.produto.search_num

      await axios
        .get('http://127.0.0.1:8000/Pesquisa/?' + pesquisa)
        .then((response) => {
          let data = response
          this.produtos = data.data.produtos
          this.load = false
        })
        .catch((err) => {
          console.log(err)
          this.load = false
        })
    },
    checkDetails: function () {
      this.$router.push({
        name: 'solicitacao_produto',
        params: { data: this.currentSelected },
      })
    },
    select_lin: function (index, event) {
      if (this.rowEvent === null) this.rowEvent = event
      else {
        if (
          this.rowEvent.path[1].attributes.id.value !==
          event.path[1].attributes.id.value
        ) {
          this.rowEvent.path[1].attributes.class.value = 'prod_tab'
          this.rowEvent = event
        }
      }
      event.path[1].attributes.class.value += ' selected'
      this.btn_solicita = true
      this.currentSelected = this.produtos[index]
      this.$store.dispatch('setProd_seletc', this.produtos[index])
    },
  },
  computed: {
    colorRow: function () {
      if (this.rowSelected) return 'prod_tab selected'
      else return 'prod_tab'
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/consulta_produto/consulta_produto.scss';
</style>
