<template>
  <div>
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
        const response = await axios.get("http://127.0.0.1:5000/api/club/charts/members/disciplines/current_year");
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
          responsive: true,
        }
      });
      myChart
    }
  }
</script>

<style scoped>

</style>