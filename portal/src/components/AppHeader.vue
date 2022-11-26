<script setup>
  defineProps({
    componentCalled: {
      type: String
    },
  });
</script>

<template>
  <nav class="navbar navbar-dark navbar-expand-lg bg-dark">
    <div class="container">
      <router-link to="/" class="navbar-brand">
      <img
          alt="Vue logo"
          class="logo"
          src="@/assets/Escudo.png"
          width="50"
          height="50"
      />
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li v-if="componentCalled !== 'statistics'" class="nav-item">
            <a class="nav-link" aria-current="page" href="#nuestroClub">Sobre nosotros</a>
          </li>
          <li v-if="componentCalled !== 'statistics'" class="nav-item">
            <a class="nav-link" href="#actividades">Actividades</a>
          </li>
          <li v-if="componentCalled === 'statistics'" class="nav-item">
            <router-link to="/" class="nav-link">Inicio</router-link>
          </li>
          <li v-if="componentCalled !== 'statistics'" class="nav-item">
            <router-link to="/statistics" class="nav-link">Estadisticas</router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item">
            <router-link to="/payments" class="nav-link">Mis Pagos</router-link>
          </li>
        </ul>
        <nav v-if="isLoggedIn">
          <span class="text-white me-4">{{authUser.full_name}}</span>
          <button @click="logout" class="btn btn-outline-light">Cerrar Sesion</button>
        </nav>
        <nav v-else>
          <router-link to="/login" class="btn btn-outline-light">Iniciar Sesion</router-link>
        </nav>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Swal from "sweetalert2";

  export default {
    name: "AppHeader",
    computed: {
      ...mapGetters({
        authUser: 'auth/user',
        isLoggedIn: 'auth/isLoggedIn'
      })
    },

    methods: {
      ...mapActions('auth', ['loginUser', 'logoutUser']),
      async logout() {
        await this.logoutUser().catch((err) => {
          console.log(err)
        });
        this.error = false;
        this.user = {
          email: null,
          password: null
        }
        this.$router.push('/')
        await Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: 'Sesion cerrada',
          showConfirmButton: false,
          timer: 1500
        })
      }
    }
  }
</script>