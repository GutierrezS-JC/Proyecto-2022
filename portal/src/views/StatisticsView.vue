<script setup>
  import AppHeader from "@/components/AppHeader.vue";
  import MembersByYearChart from "@/components/MembersByYearChart.vue";
  import MembersAndDisciplinesChart from "@/components/MembersAndDisciplinesChart.vue";
  import MembersWithDisciplinesChart from "@/components/MembersWithDisciplinesChart.vue";
  import MembersWithDebtChart from "@/components/MembersWithDebtChart.vue";
</script>

<template>
  <AppHeader component-called="statistics" />
  <div class="container-fluid" style="background-color: #fff5e5; min-height: 100vh">
    <div class="container pt-4">
      <h1 class="solidHeading text-center">Estadisticas</h1>
      <div class="row mt-4 pb-3">
        <div class="col-12 col-lg-6 text-center">
          <h1 class="outlineHeading mb-3">Cantidad de asociados del club ( Total - Por genero )</h1>
          <div>
            <MembersAndDisciplinesChart  />
          </div>
        </div>

        <div class="col-12 col-lg-6 text-center">
          <h1 class="outlineHeading mb-3">Asociados con disciplinas registradas ( {{current_year}} )</h1>
          <div>
            <MembersWithDisciplinesChart />
          </div>
        </div>
      </div>

      <div class="row mt-4 pb-3">
        <div class="col-12 text-center">
          <h1 class="outlineHeading mb-3">Cuotas segun el vencimiento</h1>
          <div>
            <MembersWithDebtChart />
          </div>
        </div>
      </div>

      <div class="row mt-5">
        <div class="col-12">
          <h1 class="outlineHeading text-center">Cantidad de asociados registrados por año</h1>
          <div class="ms-3">
            <MembersByYearChart class="mb-5" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "StatisticsView",

  data(){
    return {
      current_year : new Date().getFullYear()
    }
  }

}
</script>

<style scoped>
  .solidHeading{
    font-family: 'Londrina Solid', cursive;
    font-size:100px;
  }

  .outlineHeading{
    font-size: 60px;
    font-family: 'Londrina Shadow', cursive;
  }
</style>