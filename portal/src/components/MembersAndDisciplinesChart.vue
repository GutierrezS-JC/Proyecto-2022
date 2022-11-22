<template>
  <div>
    <canvas id="membersAndDisciplinesChart"></canvas>
  </div>
</template>

<script>
  import Chart from 'chart.js/auto';
  import axios from "axios";

  export default {
    name: "MembersAndDisciplinesChart",

    data() {
      return {
        labels: ['Hombres', 'Mujeres', 'Otrxs'],
        data: []
      }
    },

    async mounted() {
      try {
        const response = await axios.get("http://127.0.0.1:5000/api/club/charts/members/disciplines_by_genre");
        if (response.data) {
          this.data.push(response.data.cant_hombres, response.data.cant_mujeres, response.data.cant_others)
        }
      } catch (err) {
        console.log(err)
      }

      const ctx = document.getElementById('membersAndDisciplinesChart')
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
        options:{
          responsive: true,
        }
      });
      myChart
    }
  }
</script>

<style scoped>

</style>