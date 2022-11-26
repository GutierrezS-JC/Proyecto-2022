<template>
  <div class="container-fluid bg-dark">
    <div class="row p-4">
      <div class="col-12 col-lg-4">
        <div class="text-center">
          <h1 class="outlineHeading">ATENCION</h1>
        </div>
      </div>
      <div class="col-12 col-lg-8 pt-lg-3 text-white px-5">
        <p>Los valores mencionados anteriormente son los únicos valores permitidos y autorizados por el club,
          todo otro cobro deberá tener previa aprobación de la Comisión Directiva, la que lo informará con la
          antelación necesaria.</p>
        <p>El único lugar habilitado para el pago es la secretaría del club. Está prohibido el pago a los profesores.</p>
        <p>
          Los pagos se efectúan del 1 al 10 de cada mes. Todos aquellos que necesiten otra fecha de pago,
          deberán consensuar la misma con el club. Así como también cualquier situación personal,
          la que será resuelta de común acuerdo.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PricesAlert"
}
</script>

<style scoped>
  .solidHeading{
    font-family: 'Londrina Solid', cursive;
    color: white;
    font-size:80px;
  }

  .outlineHeading{
    font-size: 85px;
    color: white;
    font-family: 'Londrina Shadow', cursive;
  }
</style>