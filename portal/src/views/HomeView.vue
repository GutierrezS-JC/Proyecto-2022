<script setup>
  import InformationMain from "@/components/InformationMain.vue";
  import AppHeader from "@/components/AppHeader.vue";
  import AppFooter from "@/components/AppFooter.vue";
  import DisciplinesMain from "@/components/DisciplinesMain.vue";
  import Contacto from "@/components/Contacto.vue";
  import PricesAlert from "@/components/PricesAlert.vue";
</script>

<template>
  <main>
    <AppHeader/>
    <InformationMain />
    <DisciplinesMain />
    <PricesAlert/>
    <Contacto/>
    <AppFooter/>
  </main>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  methods: {
    ...mapActions('auth', ['fetchUser'])
  },
  computed: {
    ...mapGetters({
      authUser: 'auth/user',
      isLoggedIn: 'auth/isLoggedIn'
    })
  },
  async mounted() {
    try{
      await this.fetchUser()
    }
    catch(err){
      if(err.response.status === 401){
        console.log("Unauthorized")
      }
    }
  },
}
</script>