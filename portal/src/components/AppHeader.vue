<template>
  <nav class="navbar navbar-dark navbar-expand-lg bg-dark">
    <div class="container">
      <router-link to="/" class="navbar-brand">
      <img
          alt="Vue logo"
          class="logo"
          src="@/assets/Escudo.png"
          width="50"
          height="50"
      />
      </router-link>
<!--      <a class="navbar-brand" href="#">Club Deportivo Villa Elisa</a>-->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" aria-current="page" href="#nuestroClub">Sobre nosotros</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#actividades">Actividades</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pagos</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Estadisticas</a>
          </li>
        </ul>
<!--        <span class="navbar-text">-->
        <nav>
          <router-link to="/login" class="btn btn-outline-light">Iniciar Sesion</router-link>
<!--          <RouterLink to="/login">Iniciar Sesion</RouterLink>-->
        </nav>
<!--        </span>-->
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: "AppHeader"
  }
</script>