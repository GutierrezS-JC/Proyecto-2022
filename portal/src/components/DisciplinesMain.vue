<template>
  <div class="container-fluid" style="background-color: #fff5e5">
    <div class="container pt-4">
      <div class="row pb-5" id="actividades">
        <div class="col-12">
          <h1 class="solidHeading">Disciplinas</h1>
        </div>
        <div class="col-12 col-lg-6" v-for="discipline in disciplines" >
          <h1 class="outlineHeading">{{ discipline.name }}</h1>
          <div class="ms-3" v-for="detail in discipline.details">
            <h2 class="text-decoration-underline fw-bold h3"> {{ detail.category }} </h2>
            <ul class="ms-2 fs-5">
              <li> <span class="fw-bold"> Dias y horarios: </span> {{ detail.days_hours }} </li>
              <li> <span class="fw-bold"> Precio: </span> ${{ detail.monthly_fee }} </li>
              <li> <span class="fw-bold"> Profesores: </span> {{ detail.teachers }}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from "axios";
import {apiService} from "@/api";

export default {
  name: "DisciplinesMain",

  data() {
    return {
      disciplines: []
    }
  },

  async created() {
    try{
      const response = await apiService.get("/api/club/disciplines")
      if(response.data){
        this.disciplines = response.data
      }
    }
    catch(err){
      console.log(err.stack)
    }
  },
}
</script>

<style scoped>
 .solidHeading{
    font-family: 'Londrina Solid', cursive;
    font-size:80px;
  }

  .outlineHeading{
    font-size: 85px;
    font-family: 'Londrina Shadow', cursive;
  }
  @media (min-width: 576px){
    .solidHeading{
      font-family: 'Londrina Solid', cursive;
      font-size:120px;
    }
  }
</style>