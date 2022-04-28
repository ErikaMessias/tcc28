<template>
  <div class="cont">
    <headers />
    <div class="principal">
      <div class="base">
        <div class="titulo">
          <h1>Codigo Sucata</h1>
          <Button
            v-if="btn_selec"
            @click="checkDetail()"
            icon="pi pi-check"
            class="p-button-danger"
          />
          <Button v-else class="btn_disable" />
          <!-- <hr /> -->
        </div>

        <tr class="tabela_titulo">
          <td class="tit1">Codigo SAP</td>
          <td class="tit2">Denominação</td>
          <td class="tit3">Descrição</td>
          <td class="tit4">Exemplos</td>
          <td class="tit5">Origem</td>
        </tr>
        <table class="tabela" style="width: 100%">
          <tr
            @click="select_linha(index, $event)"
            :class="colorRows"
            v-for="(cent, index) in centList.data"
            :key="index"
            :id="'tr-' + index"
          >
            <td class="lin1">{{ cent.nomeCentralTrab }}</td>
            <td class="lin2">{{ cent.den }}</td>
            <td class="lin3">{{ cent.des }}</td>
            <td class="lin4">{{ cent.ex }}</td>
            <td class="lin5">{{ cent.ori }}</td>
          </tr>
        </table>

        <div class="pagination">
          <a @click="getPaginationSutaca(1, -1)" href="#">&laquo;</a>
          <a
            @click="getPaginationSutaca(x, 0)"
            v-for="x in centList.pages"
            :key="x"
            href="#"
            >{{ x }}</a
          >
          <a @click="getPaginationSutaca(1, 1)" href="#">&raquo;</a>
        </div>
      </div>
    </div>
    <footers />
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data: function () {
    return {
      selected: [],
      btn_selec: false,
      currentIndex: 1,
      dataReady: false,
      centList: [],
      currentSelected: {},
      rowSelected: false,
      rowSelected: false,
      rowEvents: null,
    }
  },
  methods: {
    getPaginationSutaca: async function (page, path) {
      console.log(this.currentIndex)
      if (path > 0 && this.currentIndex < this.centList.pages) {
        this.currentIndex += page
      } else if (path < 0 && this.currentIndex > 1) {
        this.currentIndex -= page
      } else if (path === 0) {
        this.currentIndex = page
      }

      await axios
        .get('http://127.0.0.1:8000/cod_sucata/?page=' + this.currentIndex)
        .then((response) => {
          let data = response
          this.centList = data.data
          this.dataReady = true
        })
        .catch((err) => {
          console.log(err)
        })
    },

    changeIndex: function (page) {
      this.currentIndex = page
      this.getPaginationSutaca()
    },

    checkDetail: function () {
      this.$router.push('/sucata')
    },

    select_linha: function (index, event) {
      this.btn_selec = true
      if (this.rowEvents === null) this.rowEvents = event
      else {
        if (
          this.rowEvents.path[1].attributes.id.value !==
          event.path[1].attributes.id.value
        ) {
          this.rowEvents.path[1].attributes.class.value = 'prod_tab'
          this.rowEvents = event
        }
      }
      event.path[1].attributes.class.value += ' selected'
      this.currentSelected = this.centList.data[index]
      this.$store.dispatch('setCodigo_seletc', this.centList.data[index])
    },
  },
  computed: {
    colorRows: function () {
      if (this.rowSelected) return 'prod_tab selected'
      else return 'prod_tab'
    },
  },
  mounted: async function () {
    this.getPaginationSutaca(0)
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/cod_sucata/cod_sucata.scss';
</style>
