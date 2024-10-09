<template>
   <header class="header">
    <div class="img">
      <img src="imagenes/image.png" alt="image" />
    </div>
    <nav>
      <ul>
        <li><a href="#">Inicio</a></li>
        <li><a href="#">Redes</a></li>
        <li><a href="#">Atención al Cliente</a></li>
      </ul>
    </nav>
    <div class="user-actions">
      <button class="search-btn">🔍</button>
      <button class="cart-btn">🛒</button>
      <button class="login-btn">Iniciar Sesión</button>
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

.img img {
  width: 120px; /* Ajusta el tamaño de la imagen */
  margin-right: 1px;
  height: auto;
  border-radius: 10px;
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

