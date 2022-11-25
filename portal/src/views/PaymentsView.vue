<script setup>
  import AppHeader from "@/components/AppHeader.vue";
  import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <AppHeader component-called="statistics"/>
  <div class="container-fluid" style="background-color: #fff5e5; min-height: 100vh">
    <div class="container pt-4">
      <h1 class="text-center solidHeading mb-4">Mis pagos</h1>
      <div>
        <h1 class="outlineHeading">Pagos realizados</h1>
      </div>

      <div class="table-responsive" v-if="fees_paid.length > 0">
        <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Socio</th>
            <th scope="col">Año</th>
            <th scope="col">Mes</th>
            <th scope="col">Monto total</th>
            <th scope="col">Fecha de pago realizado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="fee_paid in fees_paid">
            <td>{{fee_paid.member_fullname}}</td>
            <td>{{fee_paid.year}}</td>
            <td>{{fee_paid.month_str}}</td>
            <td>{{fee_paid.amount}}</td>
            <td>{{ new Date(fee_paid.date_paid).toLocaleDateString('es-AR') }}</td>
          </tr>
        </tbody>
      </table>
      </div>
      <div v-else>
        <h2 class="solidSubheading ms-4">- No hay pagos registrados -</h2>
      </div>

      <div class="mt-5">
        <h1 class="outlineHeading">Pagos pendientes</h1>
      </div>

      <div class="table-responsive" v-if="fees_not_paid.length > 0">
        <table class="table table-hover align-middle">
        <thead>
        <tr>
          <th scope="col">Socio</th>
          <th scope="col">Año</th>
          <th scope="col">Mes</th>
          <th scope="col">Monto total</th>
          <th></th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="fee_not_paid in fees_not_paid">
          <td>{{fee_not_paid.member_fullname}}</td>
          <td>{{fee_not_paid.year}}</td>
          <td>{{fee_not_paid.month_str}}</td>
          <td>{{fee_not_paid.amount}}</td>
          <td><button class="btn btn-sm btn-dark px-3">Pagar</button></td>
        </tr>
        </tbody>
      </table>
      </div>
      <div v-else>
        <h2 class="solidSubheading ms-4">- No hay pagos pendientes -</h2>
      </div>
    </div>
  </div>
  <AppFooter/>
</template>

<script>
import axios from "axios";

export default {
  name: "PaymentsView",

  data() {
    return {
      fees_paid: [],
      fees_not_paid: []
    }
  },

  async mounted() {
    try {
      const response = await axios.get('http://localhost:5000/api/me/payments/complete' ,
          {withCredentials: true, xsrfCookieName: 'csrf_access_token'})
      if(response.data){
        console.log(response.data)
        this.fees_paid = response.data.fees_paid
        this.fees_not_paid = response.data.fees_not_paid
      }
      // console.log(new Date('Fri, 28 Oct 2022 00:00:00 GMT').toLocaleDateString('es-AR'))
    }
    catch (err){
      console.log(err)
    }
  }
}
</script>

<style scoped>
  .solidHeading{
    font-family: 'Londrina Solid', cursive;
    font-size:100px;
  }

  .solidSubheading{
    font-family: 'Londrina Solid', cursive;
    font-size:30px;
  }

  .outlineHeading{
    font-size: 60px;
    font-family: 'Londrina Shadow', cursive;
  }
</style>