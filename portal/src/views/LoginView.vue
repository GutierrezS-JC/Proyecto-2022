<script setup>
  import AppHeader from "@/components/AppHeader.vue";
</script>
<template>
  <section class="vh-100" style="background-color: #f6e0bc;">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col col-xl-9">
          <div class="card" style="border-radius: 1rem;">
            <div class="row g-0">
              <div class="col-md-6 col-lg-5 d-none d-md-block">
                <div class="text-center mt-5 ms-5">
                  <img
                      alt="Vue logo"
                      class="logo"
                      src="@/assets/casual_basket.png"
                  />
                </div>
              </div>

              <div class="col-md-6 col-lg-7 d-flex align-items-center">
                <div class="card-body p-4 p-lg-5 text-black">
                  <form action @submit.prevent="login">
                    <div class="d-flex align-items-center mb-3 pb-1">
                      <img
                          alt="Vue logo"
                          class="logo"
                          src="@/assets/Escudo.png"
                          width="100"
                          height="100"
                      />
                    </div>

                    <h1 class="pb-2 display-6" style="letter-spacing: 1px;">Inicio de sesión</h1>
                    <div class="mb-4">
                      <label class="form-label" for="#formDocNum">Numero de documento</label>
                      <input v-model="user.email" id="formDocNum" class="form-control form-control-lg" />
                    </div>

                    <div class="mb-4">
                      <label class="form-label" for="formPassword">Contraseña</label>
                      <input v-model="user.password" type="password" id="formPassword" class="form-control form-control-lg" />
                    </div>

                    <div class="pt-2 mb-4">
                      <input class="btn btn-dark btn-block px-4" type="submit" value="Iniciar Sesion">
                    </div>
                    <router-link to="/" style="color: black">Volver al inicio</router-link>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapActions, mapGetters} from 'vuex'
export default {
  name: "LoginView",
  data: () => ({
    error: false,
    user: {
      email: null,
      password: null
    }
  }),
  computed: {
    ...mapGetters({
      authUser: 'auth/user',
      isLoggedIn: 'auth/isLoggedIn'
    })
  },
  methods: {
    ...mapActions('auth', ['loginUser', 'logoutUser']),

    async login() {
      await this.loginUser(this.user)
          .catch(() => {
            this.error = true
          });
      this.user = {
        email: null,
        password: null
      }

      if (this.isLoggedIn) {
        this.$router.push('/')
      }
    },

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
    }
  }
}
</script>

<style scoped>
  @media (min-width: 992px) {
    section{
      background-position: 130% 120%;
      background-size: 50em;
      background-repeat: no-repeat;
      background-image: url("@/assets/sports.png");
    }
  }

</style>