<template>
  <div class="chart-container text-center">
    <canvas id="membersWithDisciplinesChart"></canvas>
  </div>
</template>

<script>
  import Chart from 'chart.js/auto';
  import axios from "axios";

  export default {
    name: "MembersWithDisciplinesChart",

    data(){
      return {
        labels: ['Hombres', 'Mujeres', 'Otrxs'],
        data: []
      }
    },

    async mounted() {
      try {
        // const response = await axios.get("http://127.0.0.1:5000/api/club/charts/members/disciplines/current_year");
        const response = await axios.get("https://admin-grupo26.proyecto2022.linti.unlp.edu.ar/api/club/charts/members/disciplines/current_year");
        if (response.data) {
          this.data.push(response.data.cant_male, response.data.cant_female, response.data.cant_others)
        }
      } catch (err) {
        console.log(err)
      }

      const ctx = document.getElementById('membersWithDisciplinesChart')
      const myChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: this.labels,
          datasets: [{
            label: 'Cantidad',
            data: this.data,
            backgroundColor: [
              'rgb(255, 99, 132)',
              'rgb(75, 192, 192)',
              'rgb(153, 102, 255)'
            ],
            hoverOffset: 4
          }]
        },
        options: {
          maintainAspectRatio: false,
          responsive: true,
        }
      });
      myChart
    }
  }
</script>

<style scoped>
  @media (min-width: 767.98px){
    .chart-container{
      height:75vh !important;
    }
  }
</style>