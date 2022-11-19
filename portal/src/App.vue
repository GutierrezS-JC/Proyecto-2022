<script setup>
import { RouterLink, RouterView } from "vue-router";
import AppHeader from "@/components/AppHeader.vue";
import InformationMain from "@/components/InformationMain.vue";
</script>

<template>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <AppHeader />
  <InformationMain />
</template>

<style scoped>
  *{
    background-color: #fff5e5
  }
</style>