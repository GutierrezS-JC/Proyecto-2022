<template>
  <div class="chart-container text-center">
    <canvas id="membersWithDebtChart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from "axios";

export default {
  name: "MembersWithDebtChart",

  data(){
    return {
      labels: ['No Vencidas', 'Vencidas'],
      data: []
    }
  },

  async mounted() {
    try {
      const response = await axios.get("http://127.0.0.1:5000/api/club/charts/members/with_debt_cant");
      if (response.data) {
        this.data.push(response.data.cant_no_vencidas, response.data.cant_vencidas)
      }
    } catch (err) {
      console.log(err)
    }

    const ctx = document.getElementById('membersWithDebtChart')
    const myChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: this.labels,
        datasets: [{
          label: 'Cantidad',
          data: this.data,
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(75, 192, 192)',
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