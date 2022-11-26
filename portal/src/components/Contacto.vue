<template>
  <div class="container-fluid" style="background-color: #fff5e5">
    <div class="container pt-2 pt-md-5">
      <h1 class="solidHeading">Contacto</h1>
      <div class="row pb-5">
        <div class="col-12 col-lg-6 mt-2">
          <h2 class="fw-semibold mb-4">{{info.contact_info}}</h2>
          <h2 class="outlineHeading">Telefono: </h2>
          <ul>
            <li class="defaultSub ms-md-3">
              {{info.phone}}
            </li>
          </ul>
          <h2 class="outlineHeading">Email: </h2>
          <ul>
            <li class="defaultSub ms-md-3">
              {{info.email}}
            </li>
          </ul>
        </div>
        <div class="col-12 col-lg-6">
          <iframe
              src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13096.656971618655!2d-58.0855378!3d-34.8521002!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc036ac4c09e2e382!2sClub%20Deportivo%20Villa%20Elisa!5e0!3m2!1ses-419!2sar!4v1669469242420!5m2!1ses-419!2sar"
              style="border:0;" allowfullscreen="" loading="lazy"
              referrerpolicy="no-referrer-when-downgrade">
          </iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Contacto",

  data(){
    return{
      info: {}
    }
  },

  async created() {
    try{
      // const response = await axios.get("http://127.0.0.1:5000/api/club/info")
      const response = await axios.get("https://admin-grupo26.proyecto2022.linti.unlp.edu.ar/api/club/info")
      this.info = response.data
    }
    catch(err){
      console.log(err)
    }
  }
}
</script>

<style scoped>
  .solidHeading{
    font-family: 'Londrina Solid', cursive;
    font-size:80px;
  }

  .solidSubheading{
    font-family: 'Londrina Solid', cursive;
    font-size:40px;
  }

  .defaultSub{
    font-family: Roboto, Arial, sans-serif;
    font-weight: bold;
    font-size: 1.2em;
  }
  .outlineHeading{
    font-size: 60px;
    font-family: 'Londrina Shadow', cursive;
  }
  iframe {
    width: 100%;
    height: 400px;
  }

  @media (min-width: 576px){
    .solidHeading{
      font-family: 'Londrina Solid', cursive;
      font-size:120px;
    }

    .defaultSub{
      font-family: Roboto, Arial, sans-serif;
      font-weight: bold;
      font-size: 1.8em;
    }
  }
</style>
