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
          <th scope="col">Agregar comprobante</th>
          <th></th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="fee_not_paid in fees_not_paid">
          <td>{{fee_not_paid.member_fullname}}</td>
          <td>{{fee_not_paid.year}}</td>
          <td>{{fee_not_paid.month_str}}</td>
          <td>{{fee_not_paid.amount}}</td>
          <td><input type="file" @change="onChangeFile(fees_not_paid, $event)"
                     accept="application/pdf,application/vnd.ms-excel, image/png, image/jpeg"/></td>
          <td v-if="file">
            <button @click="submitFile" class="btn btn-sm btn-dark px-3">Registrar pago</button>
          </td>
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
import Swal from "sweetalert2";

export default {
  name: "PaymentsView",

  data() {
    return {
      fees_paid: [],
      fees_not_paid: [],
      file: null,
      month: null,
      year: null
    }
  },

  async mounted() {
    await this.fetchPayments();
  },

  methods:{
    async fetchPayments() {
      try {
        // const response = await axios.get('http://localhost:5000/api/me/payments/complete' ,
            const response = await axios.get('https://admin-grupo26.proyecto2022.linti.unlp.edu.ar/api/me/payments/complete',
            {withCredentials: true, xsrfCookieName: 'csrf_access_token'})
        if(response.data){
          this.fees_paid = response.data.fees_paid
          this.fees_not_paid = response.data.fees_not_paid
        }
      }
      catch (err){
        console.log(err)
      }
    },

    onChangeFile(feeNotPaid, event){
      this.month = feeNotPaid[0].month_num
      this.year = feeNotPaid[0].year
      this.file = event.target.files[0];
    },

    async submitFile(){
      let formData = new FormData();
      formData.append('file', this.file)
      try{
        // const response = await axios.post('http://localhost:5000/api/me/payments',
        const response = await axios.post('https://admin-grupo26.proyecto2022.linti.unlp.edu.ar/api/me/payments',
            {'month': this.month, 'year': this.year},
            {withCredentials: true, xsrfCookieName: 'csrf_access_token'})
        // const res_file = await axios.post('http://localhost:5000/api/me/payments/file', formData, {
        const res_file = await axios.post('https://admin-grupo26.proyecto2022.linti.unlp.edu.ar/api/me/payments/file', formData, {
          withCredentials: true,
              xsrfCookieName: 'csrf_access_token'
            },
        )
        if(response.data && res_file){
          await this.fetchPayments()
          await Swal.fire(
              'Todo bien!',
              'La cuota fue registrada con exito',
              'success'
          )
        }
      }
      catch(err){
        console.log(err)
        await Swal.fire(
            'Error',
            'No se pudo registrar el pago de la cuota',
            'error'
        )
      }
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