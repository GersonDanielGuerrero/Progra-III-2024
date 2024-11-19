<template>
  <header class="header">
    <div class="img">
      <img src="imagenes/image.png" alt="image" />
      <button @click="editarLogo" class="edit-logo-btn">✏️</button>
    </div>
    <nav>
      <ul>
        <li :class="{ active: opcionSeleccionada === 'Inicio' }">
          <a href="#" @click="enviarA('/')">Inicio</a>
        </li>
        <li :class="{ active: opcionSeleccionada === 'Redes' }">
          <a href="#" @click="enviarA('/redes')">Redes</a>
        </li>
        <li :class="{ active: opcionSeleccionada === 'Atención al Cliente' }">
          <a href="#" @click="enviarA('/preguntas')">Atención al Cliente</a>
        </li>
        <li v-if="roles.includes('Administrador')" :class="{ active: opcionSeleccionada === 'Administración' }">
          <a href="#" @click="enviarA('/admin')">Administración</a>
        </li>
        <li>
          <button class="search-btn" @click="enviarA('/ubicacion')">
            <i class="bi bi-geo-alt-fill" :class="{ active: opcionSeleccionada === 'Ubicación' }"></i>
          </button>
        </li>
        <li>
          <button class="cart-btn" @click="enviarA('/carrito')">
          <i class="bi bi-cart-fill" :class="{ active: opcionSeleccionada === 'Carrito' }"></i>
          </button>
        </li>
      </ul>
      <div class="user-actions">
        <BotonComp @click="enviarA('/login')" class="login-btn">
          {{ usuario ? 'Cuenta' : 'Iniciar Sesión' }}
        </BotonComp>
      </div>
    </nav>
  </header>
</template>

<style scoped>
i{
  color: #fffe;
  height: 100%;
  width: 100%;
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

nav ul, nav {
  list-style: none;
  display: flex;
  gap: 20px;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
}
nav {
  margin-right: 20px;
}

nav ul li a {
  text-decoration: none;
  color: #fff;
  font-weight: bold;
}

nav ul li.active a {
  color: #f6a901;
}
.active {
  color: #f6a901;
}
.user-actions {
  display: flex;
  gap: 10px;
}

.cart-btn,
.search-btn {
  background-color: #000000;
  border: none;
  padding: 8px 10px;
  cursor: pointer;
  font-weight: bold;
}
</style>

<script>
import BotonComp from './BotonComp.vue';
export default {
  components: {
    BotonComp,
  },
  name: 'BarraMenu',
  data() {
    return {
      usuario: null,
      roles: [],
    };
  },
  methods: {
    enviarA(opcion) {
      this.$router.push(opcion);
    },
    editarLogo() {
    
      console.log('Edit logo clicked');
    },
  },
  props: {
    opcionSeleccionada: {
      type: String,
      required: true,
    },
  },
};
</script>