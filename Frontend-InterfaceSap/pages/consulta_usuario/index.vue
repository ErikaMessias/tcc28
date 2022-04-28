// Consulta Usuario

<template>
  <div class="cont">
    <headers />
    <div class="principal">
      <div class="base">
        <h1>Consulta de Usuario</h1>
        <div class="centro">
          <input
            type="text"
            name="search"
            class="inputs"
            id="input1"
            placeholder="Pesquisar"
          />
          <button>Buscar</button>
        </div>
        <div class="cards">
          <div
            v-for="usuarios in UserList.data"
            :key="usuarios.id"
            class="card-one c"
          >
            <h1>{{ usuarios.edv }}</h1>
            <h1>{{ usuarios.email }}</h1>
            <Button @click="Apagar(usuarios.id)" icon="pi pi-trash" class="p-button-danger" />
          </div>
        </div>
      </div>
    </div>
    <footers />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'hist_produto',
  middleware: 'auth',

  data() {
    return {
      UserList: [],
      dataReady: false,
    }
  },
  methods: {

    deletar: async function(id){
      await this.$axios
        .$delete(
          'http://localhost:8000/api/v1/users/'+id,
          console.log(111)
        )
      window.location.reload(true)
    },

    Apagar: async function(id){
      await this.$axios
        .$delete(
          'http://localhost:8000/Usuario/'+id,
        )
      this.deletar(id)
      console.log(1)
      window.location.reload(true)
    },

    getUsuario: async function () {
      await axios
        .get('http://localhost:8000/Usuario/')
        .then((response) => {
          let data = response
          this.UserList = data.data
          this.dataReady = true
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },

  mounted: async function () {
    this.getUsuario()
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/consulta_usuario/consulta_usuario.scss';
</style>
