// Sucata
<template>
  <div class="cont">
    <headers />
    <toast position="bottom-right" />
    <div class="principal">
      <form class="base" method="POST">
        <h1>Descarte Sucata</h1>
        <input
          type="text"
          name="txtBreve"
          class="inputs"
          id="txtBreve"
          ref="den"
          placeholder="Nome da Sucata"
          v-model="sucata.txtBreve"
          readonly
        />
        <input
          type="number"
          name="trab"
          class="inputs"
          id="trab"
          ref="quant"
          placeholder="Quantidade (Kg)"
          v-model="sucata.trab"
          required
        />
        <input
          type="text"
          name="desc"
          class="inputs"
          id="desc"
          ref="desc"
          placeholder="Descricao"
          v-model="sucata.desc"
          required
        />
        <button type="submit" @click.prevent="fetchSucata">Enviar</button>
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
  middleware: 'auth',

  data() {
    return {
      prod: null,
      selected: [],
      sucata: {
        desc: '',
        idCenTrabFK: '',
        trab: '',
        user:'',
        id_user:'',
        txtBreve: '',
        idtipoOrdemFK: 1,
        idLocalFK: 1,
        idtipoavtFK: 1,
        iddivisaoFK: 1,
        idCentroCustoFK: 1,
      },
    }
  },
  methods: {
    fetchSucata: async function () {
      let obj = this.sucata
      let send = true

      console.log(1)

      for (const [key, value] of Object.entries(this.sucata)) {
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
            'http://127.0.0.1:8000/TransacaoSucata/',
            JSON.stringify([this.sucata]),
            {
              headers: {
                'Content-Type': 'application/json',
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
              this.$router.push('/cod_sucata')
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
  },
  created() {
    this.selected = this.$store.state.cod_sucata
    this.sucata.txtBreve = this.selected.nomeCentralTrab
    this.sucata.idCenTrabFK = this.selected.id
    this.sucata.user = this.$auth.user.username
    this.sucata.id_user = this.$auth.user.id
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/sucata/sucata.scss';
</style>
