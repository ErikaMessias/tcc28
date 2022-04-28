// Cadastro Usuario
<template>
  <div class="cont">
    <headers />
    <toast position="bottom-right" />
    <div class="principal">
      <form class="base">
        <h1>Cadastro Usuario</h1>
        <input
          type="text"
          name="idUserFK"
          class="inputs"
          id="idUserFK"
          placeholder="Nome"
          v-model="cadastro.nomes"
          required
        />
        <input
          type="email"
          name="email"
          class="inputs"
          id="input3"
          placeholder="email"
          v-model="cadastro.email"
          required
        />
        <input
          type="number"
          name="edv"
          class="inputs"
          id="input4"
          placeholder="EDV"
          v-model="cadastro.edv"
          required
        />

        <!--  -->

        <AutoComplete
          :multiple="false"
          v-model="selectedResponsavel"
          @complete="searchResponsavel($event)"
          :suggestions="filteredResponsavel"
          field="nomeResponsavel"
          id="Responsavel"
          placeholder="Preencha..."
        />

        <select v-model="idNivel" name="nivelAcesso" class="inputs">
          <option value="">Select</option>
          <option :value="nivel.id" v-for="nivel in nivelList" :key="nivel.id">
            {{ nivel.nomeAcesso }}
          </option>
        </select>

        <input
          type="password"
          name="senha"
          class="inputs"
          id="input5"
          placeholder="Senha"
          v-model="cadastro.senha"
          required
        />
        <button @click.prevent="Register" type="submit">Enviar</button>
      </form>
    </div>
    <footers />
  </div>
</template>

<script>
import headers from '../../components/headers.vue'
export default {
  components: { headers },
  name: 'home',
  data() {
    return {
      selectedResponsavel: [],
      filteredResponsavel: [],
      dataReady: false,
      nivelList: [],
      idNivel: '',
      allResponsaveis: [],
      cadastro: {
        nomes: '',
        email: '',
        edv: '',
        nivelAcesso: '',
        senha: '',
        nivelAcesso: '',
      },
    }
  },
  methods: {
    searchResponsavel(event) {
      setTimeout(() => {
        if (!event.query.trim().length) {
          this.filteredResponsavel = [...this.allResponsaveis]
        } else {
          this.filteredResponsavel = this.allResponsaveis.filter(
            (nomeResponsavel) => {
              return nomeResponsavel.nomeResponsavel
                .toLowerCase()
                .startsWith(event.query.toLowerCase())
            }
          )
        }
      }, 250)
    },

    getNivel: async function () {
      await this.$axios
        .get('http://127.0.0.1:8000/nivelAcesso')
        .then((response) => {
          console.log(response.data)
          this.nivelList = response.data.data
          console.log(this.nivelList)

          
        })
        .catch((err) => {
          console.log(err)
        })
    },

    RegisterUsuario: async function (response) {
      if (response.email === this.cadastro.email) {
        await this.$axios.$post('http://localhost:8000/Usuario/', [
          {
            edv: this.cadastro.edv,
            nomes: this.cadastro.nome,
            senha: this.cadastro.senha,
            email: this.cadastro.email,
            idUserFK: response.id,
            idRespFK: this.selectedResponsavel.id,
            idNivelAcessFK: this.idNivel,
          },

          this.$toast.add({
            severity: 'success',
            summary: 'Solicitação enviada com sucesso!',
            life: 3000,
          })
        ])
      }
    },

    Register: async function () {
      await this.$axios
        .$post('http://localhost:8000/api/v1/users/', {
          username: this.cadastro.edv,
          password: this.cadastro.senha,
          email: this.cadastro.email,
        })
        .then((response) => {
          console.log(response)
          this.RegisterUsuario(response)
        })
        .catch((error) => {
          console.log(error)
        })
    },

    getResponsaveis: async function () {
      await this.$axios
        .$get('http://localhost:8000/Responsavel/')
        .then((response) => {
          this.allResponsaveis = response.data
          console.log(this.allResponsaveis)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created() {
    this.getResponsaveis()
    this.getNivel()
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/cadastro_usuario/cadastro_usuario.scss';
</style>
