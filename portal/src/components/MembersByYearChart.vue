<template>
  <div>
    <canvas id="membersByYearChart"></canvas>
  </div>
</template>

<script>
  import Chart from 'chart.js/auto';
  import axios from "axios";
  import { toRaw } from 'vue';
  import {apiService} from "@/api";

  export default {
    name: "MembersByYearChart",
    data(){
      return{
        labels: [],
        data: []
      }
    },

    async mounted() {
      try{
        const response = await apiService.get("/api/club/charts/members/year/genre_alternative");
        const res_years = await apiService("/api/club/charts/members/years_in_range")
        if(response.data && res_years.data){
          response.data.map((item) =>{
            this.data.push(item)
          })
          res_years.data.map((item) => {
            this.labels.push(item)
          })
        }
      }
      catch(err){
        console.log(err.stack)
      }

      const ctx = document.getElementById('membersByYearChart')
      const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.labels,
          datasets: [{
            label: 'Hombres',
            data: toRaw(this.data[0]),
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(255, 99, 132, 0.2)',
              'rgba(255, 99, 132, 0.2)',
              'rgba(255, 99, 132, 0.2)',
              'rgba(255, 99, 132, 0.2)',
              'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(255, 99, 132, 1)',
              'rgba(255, 99, 132, 1)',
              'rgba(255, 99, 132, 1)',
              'rgba(255, 99, 132, 1)',
              'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1
          },
            {
              label: 'Mujeres',
              data: toRaw(this.data[1]),
              backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(75, 192, 192, 0.2)',
              ],
              borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(75, 192, 192, 1)',
              ],
              borderWidth: 1
            },
            {
              label: 'Otrxs',
              data: toRaw(this.data[2]),
              backgroundColor: [
                'rgba(153, 102, 255, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(153, 102, 255, 0.2)',
              ],
              borderColor: [
                'rgba(153, 102, 255, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(153, 102, 255, 1)',
              ],
              borderWidth: 1
            }]
        },
        options:{
          responsive: true,
          interaction:{
            intersect: false,
          },
          scales: {
            x: {
              stacked:true,
            },
            y: {
              stacked: true,
              beginAtZero: true,
            }
          }
        }
      });
      myChart;
    }
  }
</script>

<style scoped>

</style>