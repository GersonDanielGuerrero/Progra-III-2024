<template>
  <header class="header">
    <div class="img">
      <img src="imagenes/image.png" alt="image" />
      <button @click="editarLogo" class="edit-logo-btn">✏️</button>
    </div>
    <nav>
      <ul>
        <li :class="{ active: opcionSeleccionada === 'Inicio' }">
          <a href="#" @click="seleccionarOpcion('Inicio')">Inicio</a>
        </li>
        <li :class="{ active: opcionSeleccionada === 'Redes' }">
          <a href="#" @click="seleccionarOpcion('Redes')">Redes</a>
        </li>
        <li :class="{ active: opcionSeleccionada === 'Atención al Cliente' }">
          <a href="#" @click="seleccionarOpcion('Atención al Cliente')">Atención al Cliente</a>
        </li>
        <li :class="{ active: opcionSeleccionada === 'Administración' }">
          <a href="#" @click="seleccionarOpcion('Administración')">Administración</a>
        </li>
      </ul>
    </nav>
    <div class="user-actions">
      <button class="search-btn">🔍</button>
      <button class="cart-btn">🛒</button>
      <button @click="enviarLogin" class="login-btn">
        {{ usuario ? 'Cuenta' : 'Iniciar Sesión' }}
      </button>
    </div>
  </header>
</template>

<style scoped>
/* Estilos generales */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #000;
  color: #ffffff;
}

/* Header */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #000;
  border-bottom: 2px solid #fdfdfd46;
}

.img {
  display: flex;
  align-items: center;
}

.img img {
  width: 120px;
  margin-right: 10px;
  height: auto;
  border-radius: 10px;
}

.edit-logo-btn {
  background-color: transparent;
  color: #fff;
  border: none;
  cursor: pointer;
  font-size: 18px;
}

nav ul {
  list-style: none;
  display: flex;
  gap: 20px;
}

nav ul li a {
  text-decoration: none;
  color: #fff;
  font-weight: bold;
}

nav ul li.active a {
  color: #f6a901;
}

.user-actions {
  display: flex;
  gap: 10px;
}

.login-btn {
  background-color: #f6a901;
  color: #000;
  border: none;
  padding: 8px 10px;
  cursor: pointer;
  font-weight: bold;
}

.cart-btn,
.search-btn {
  background-color: #000000;
  color: #000;
  border: none;
  padding: 8px 10px;
  cursor: pointer;
  font-weight: bold;
}
</style>

<script>
export default {
  name: 'BarraMenu',
  data() {
    return {
      opcionSeleccionada: 'Inicio',
      usuario: null, 
    };
  },
  methods: {
    enviarLogin() {
      this.$router.push('/login');
    },
    seleccionarOpcion(opcion) {
      this.opcionSeleccionada = opcion;
    },
    editarLogo() {
    
      console.log('Edit logo clicked');
    },
  },
};
</script>