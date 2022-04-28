// Solicitação de Produtos

<template>
  <div class="cont">
    <headers />
    <toast position="bottom-right" />
    <div class="principal">
      <form class="base" method="POST">
        <h1>Solicitação de Produtos</h1>
        <div class="centro">
          <section class="img">
            <img src="/fita.png" />
          </section>
          <section class="campos">
            <input
              type="text"
              name="material"
              class="inputs"
              id="material"
              placeholder="Nome Material"
              v-model="solicitacao.material"
              readonly
            />
            <input
              type="text"
              name="codigo"
              class="inputs"
              id="codigo"
              placeholder="Codigo"
              v-model="solicitacao.codigo"
              readonly
            />
            <input
              type="number"
              min="0"
              :max="maxsteel"
              name="quantidade"
              class="inputs"
              id="quantidade"
              placeholder="Quantidade(UN)"
              v-model="solicitacao.quantidade"
              required
            />
            <input
              type="text"
              name="recebedor"
              class="inputs"
              id="recebedor"
              placeholder="Recebedor"
              v-model="solicitacao.recebedor"
              required
            />
          </section>
        </div>
        <!-- <button type="submit" @click="fetchSolicitacao">Enviar</button> -->
        <button type="submit" @click.prevent="fetchSolicitacao">Enviar</button>
      </form>
    </div>
    <footers />
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'home',
  middleware: 'auth',
  data() {
    return {
      selectedItem: [],
      maxsteel: null,
      fotolist: [],
      dataReady: false,
      solicitacao: {
        codigo: '',
        material: '',
        quantidade: '',
        recebedor: '',
        user_Salva: '',
        id_user_Salva: '',
        umr: 7463,
        dep: 555,
        idCentroCFK: 1,
        idTipoMovimentoFK: 1,
        idContaRazaoFK: 1,
      },
    }
  },
  methods: {
    fetchSolicitacao: async function () {
      let send = true

      for (const [key, value] of Object.entries(this.solicitacao)) {
        if (document.getElementById(key)) {
          if (value == '') {
            send = false
            document.getElementById(key).style.borderColor = ''
          } else {
            document.getElementById(key).style.borderColor = '#E5E5E5'
          }
        }
      }

      if (send) {
        await this.$axios
          .$post(
            'http://127.0.0.1:8000/TransacaoProduto/',
            JSON.stringify([this.solicitacao]),
            {
              headers: {
                'Content-type': 'application/json',
              },
            }
          )
          .then((response) => {
            console.log(response)
            this.$toast.add({
              severity: 'success',
              summary: 'Solicitação enviada com sucesso!',
              life: 3000,
            })

            setTimeout(() => {
              this.$router.push('/consulta_produto')
            }, 2500)
          })
          .catch((error) => {
            console.log(error)
            this.$toast.add({
              severity: 'error',
              summary: 'Solicitação não enviada!',
              detail: 'Preencher novamente!',
              life: 4000,
            })
          })
      }
    },
    getFoto: async function () {
      await axios
        .get('http://localhost:8000/Produto')
        .then((response) => {
          let data = response
          this.fotolist = data.data
          this.dataReady = true
          console.log(this.fotolist)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.selectedItem = this.$route.params.data
    this.solicitacao.material = this.selectedItem[2]
    this.solicitacao.codigo = this.selectedItem[0]
    this.maxsteel = this.selectedItem[1]
    this.solicitacao.user_Salva = this.$auth.user.username
    this.solicitacao.id_user_Salva = this.$auth.user.id
  },

   mounted: async function () {
    this.getFoto()
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/solicitacao_produto/solicitacao_produto.scss';
</style>
