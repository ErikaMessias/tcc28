<template>
  <div class="cont">
    <headerLogin />
    <toast position="bottom-right" />
    <div class="principal">
      <div class="base">
        <h1>Login</h1>
        <form
          action=""
          method="POST"
          class="loginForm"
          v-on:submit.prevent="sendlogin()"
        >
          <input
            type="text"
            id="input1"
            class="inputs"
            v-model="login.username"
            required
            placeholder="EDV"
          />
          <input
            type="password"
            name="senha"
            v-model="login.password"
            class="inputs"
            id="input2"
            required
            placeholder="Senha"
          />
          <button type="submit">Enviar</button>
        </form>
      </div>
    </div>
    <footers />
  </div>
</template>

<script>
export default {
  name: 'login',
  data() {
    return {
      login: {
        username: null,
        password: null,
      },
    }
  },
  methods: {
    sendlogin() {
      console.log('tentando autenticar....')
      console.log(this.login)
      this.$auth
        .loginWith('local', { data: this.login })
        .then(() => {
          console.log('DEU CERTO O LOGIN')
        })
        .catch((erro) => {
          this.login.username = null
          this.login.password = null
          console.log('erro')
          console.log(erro)
          this.$toast.add({
            severity: 'error',
            summary: 'Login invalido!',
            detail: 'Edv ou senha errados. Tente outra vez.',
            life: 3000,
          })
        })
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/pages/login.scss';
</style>
