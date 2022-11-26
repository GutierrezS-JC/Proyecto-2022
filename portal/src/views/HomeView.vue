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

</script>