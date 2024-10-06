<template>
    <div>
        <nav class="barra-menu">
    <div class="logo">
      <span class="good">GOOD</span>
      <span class="burger">BURGER</span>
    </div>
    <ul class="menu">
      <li><a href="#">Inicio</a></li>
      <li><a href="#">Nosotros</a></li>
      <li><a href="#">Redes</a></li>
      <li><a href="#">Atención al Cliente</a></li>
    </ul>
    <div class="acciones">
      <a href="#" class="iniciar-sesion">Iniciar Sesión</a>
    </div>
  </nav>
    </div>
</template>
<style scoped>
.barra-menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #000; 
  padding: 10px 20px;
}

.logo {
  color: #ffad00; 
  font-size: 24px;
}

.good {
  font-weight: bold;
}

.burger {
  font-weight: normal;
}

.menu {
  list-style: none;
  display: flex;
  gap: 20px;
}

.menu li a {
  color: #fff; 
  text-decoration: none;
  font-size: 16px;
}

.menu li a:hover {
  color: #ffad00;
}

.acciones {
  margin-left: auto;
}

.iniciar-sesion {
  color: #ffad00; 
  text-decoration: none;
  background-color: #fff;
  padding: 10px 15px;
  border-radius: 5px;
}

.iniciar-sesion:hover {
  background-color: #ffad00; 
  color: #000; 
}

</style>


<script>
export default {
    name: 'BarraMenu',
}
</script>