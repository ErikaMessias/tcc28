<template>
  <div>
    <div class="line"></div>
    <header class="menu">
      <section class="imagem_logo"></section>
      <section class="meio_header"></section>
      <section class="list">
        <div class="links">
          <NuxtLink to="/transacoes" class="link" id="home">
            <span>Home</span>
            <img src="homee.png" />
          </NuxtLink>
          <NuxtLink to="/config" class="link" id="config">
            <span>Configurações</span>
            <img src="teste.png" />
          </NuxtLink>
          <NuxtLink to="/perfil" class="link" id="hist">
            <span>Perfil</span>
            <img src="perfil.png" />
          </NuxtLink>
          <button class="logout" @click="logout">
            <img src="logout.png" />
          </button>
        </div>
      </section>
    </header>
  </div>
</template>

<script>
export default {
  methods: {
    logout: function () {
      this.$auth.logout()
    },
  },
}
</script> 

<style lang="scss" scoped>
@import '@/layouts/variaveis.scss';
$image: '@/static/logo.png';

.perfil {
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.logout {
  width: 24px;
  height: 24px;
  border: none;
  cursor: pointer;
  background: #fff;
}

.menu {
  height: calc($alturaHeader - $alturaLine);
  width: 100%;
  display: flex;
  flex-direction: row;
}

.meio_header {
  height: 100%;
  width: 90%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: white;
}

.list {
  width: calc(100% - 70%);
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  background-color: white;
  font-weight: 600;
  padding-inline-start: 30px;
}

.links {
  display: flex;
}

.link {
  width: initial;
  position: relative;
  padding-bottom: 8px;
  cursor: pointer;
  color: black;
  padding: 0 2px;
  margin: 0 15px;
  text-decoration: none;

  display: flex;
  flex-direction: row;
  align-items: center;

  span {
    width: auto;
  }

  img {
    height:24px;
    width: 24px;
    display: none;
  }
}

.link::after {
  position: absolute;
  margin-bottom: -10px;
  bottom: 0;
  left: 0;
  content: '';
  width: 0%;
  height: 3px;
  background-color: red;
  transition: width 0.4s ease-out;
}

.link:hover.link::after {
  width: 100%;
}

.line {
  margin-top: 0;
  height: $alturaLine;
  background-image: url('/linha.jfif');
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  justify-content: center;
}

.imagem_logo {
  height: 100%;
  width: 15%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: white;
  background-image: url($image);
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

@media (max-width: 1600px) {
  #home {
    content: 'teste';
  }
}

@media screen and (max-width: 500px) {
  .imagem_logo {
    height: 100%;
    width: 25%;
    margin-left: 4px;
  }

  .meio_header {
    display: none;
  }

  .list {
    width: calc(100% - 10%);
  }

  .links {
    font-size: 12px;
    justify-content: center;
    padding-left: 0;
    margin-left: 0;
    
    .link {
      span {
        display: none;
      }
      img {
        display: block;
      }
    }
  }
  .perfil {
    width: 15px;
    height: 15px;
  }
}
</style>
