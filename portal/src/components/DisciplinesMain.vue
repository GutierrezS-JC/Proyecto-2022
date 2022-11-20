<template>
  <div class="container-fluid" style="background-color: #fff5e5">
    <div class="container pt-4">
      <h1 class="solidHeading">Actividades / Disciplinas</h1>
      <div class="row" id="actividades">
        <div class="col-12 col-lg-6">
          <h1>FUTBOL</h1>
          <ul class="ms-3">
            <li>Categoria 2022</li>
            <li>Categoria 2023</li>
            <li>Categoria 2025</li>
          </ul>
        </div>

        <div class="col-12 col-lg-6">
          <h1>Basquet</h1>
          <ul class="ms-3">
            <li>Categoria Adultos</li>
          </ul>
        </div>

        <div class="col-12 col-lg-6">
          <h1>Basquet</h1>
          <ul class="ms-3">
            <li>Categoria Adultos</li>
          </ul>
        </div>

        <div class="col-12 col-lg-6">
          <h1>FUTBOL</h1>
          <ul class="ms-3">
            <li>Categoria 2022</li>
            <li>Categoria 2023</li>
            <li>Categoria 2025</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "DisciplinesMain",

  async created() {
    // axios.get(`https://admin-grupo26.proyecto2022.linti.unlp.edu.ar/api/club/disciplines`)
    axios.get(`http://127.0.0.1:5000/api/club/disciplines`)
        .then((response) =>
          console.log(response.data))
  },
}
</script>

<style scoped>
  .solidHeading{
    font-family: 'Londrina Solid', cursive;
    font-size:100px;
  }
</style>