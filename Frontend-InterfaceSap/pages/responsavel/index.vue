<template>
  <div class="cont">
    <headers />
    <div class="principal">
    <toast position="bottom-right" />
      <div class="base">
        <h1>Responsaveis</h1>
          <details class="collapse">
            <summary class="title">Cadastrar Responsavel</summary>
              <form class="form" method="POST">
                <input
                  type="text"
                  name="nomeResponsavel"
                  class="inputs"
                  id="nomeResponsavel"
                  v-model="responsavel.nomeResponsavel"
                  placeholder="Nome"
                  required
                />
                <input
                  type="email"
                  name="email_resp"
                  class="inputs"
                  id="email_resp"
                  v-model="responsavel.email_resp"
                  placeholder="email"
                />
                <button @click="SalvaResp" type="submit">Enviar</button>
        </form>
        </details>
        <hr>
        <table
          v-for="resp in respList.data"
          class="tabela"
          :key="resp.id"
          style="width: 100%"
        >
          <tr>
            <td class="linha">{{ resp.nomeResponsavel }}</td>
            <td class="linha">{{ resp.email_resp }}</td>
            <Button @click="Apagar(resp.id)"
              icon="pi pi-trash"
              class="p-button-danger"
            />
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
  name: 'home',
  middleware: 'auth',

  data() {
    return {
      respList: [],
      dataReady: false,
      responsavel: {
        nomeResponsavel: '',
        email_resp: '',
      },
    }
  },
  methods: {
    Apagar: async function(id){
      await this.$axios
        .$delete(
          'http://127.0.0.1:8000/Responsavel/'+id,
        )
      window.location.reload(true)

    },
    
    SalvaResp: async function () {
      let send = true

      for (const [key, value] of Object.entries(this.responsavel)) {
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
            'http://127.0.0.1:8000/Responsavel/',
            JSON.stringify([this.responsavel]),
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

    getResponsavel: async function () {
      await axios
        .get('http://127.0.0.1:8000/Responsavel')
        .then((response) => {
          let data = response
          this.respList = data.data
          this.dataReady = true
          console.log(this.respList)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  
  mounted: async function () {
    this.getResponsavel()
  },

}
</script>

<style lang="scss" scoped>
@import '@/pages/responsavel/responsavel.scss';
</style>
