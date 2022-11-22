<script setup>
  import AppHeader from "@/components/AppHeader.vue";
  import MembersByYearChart from "@/components/MembersByYearChart.vue";
</script>

<template>
  <AppHeader component-called="statistics" />
  <div class="container-fluid" style="background-color: #fff5e5; min-height: 100vh">
    <div class="container pt-4">
      <h1 class="solidHeading text-center">Estadisticas</h1>
      <div class="row mt-4 pb-5">
        <div class="col-12 col-lg-6">
          <h1 class="outlineHeading text-center">Cantidad de personas inscriptas en una disciplina</h1>
          <div class="ms-3">
            <h2 class="fw-bold h3"> Chau </h2>
          </div>
        </div>

        <div class="col-12 col-lg-6">
          <h1 class="outlineHeading text-center">Participacion en disciplinas ( Por genero )</h1>
          <div class="ms-3">
            <h2 class="fw-bold h3"> Chau </h2>
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