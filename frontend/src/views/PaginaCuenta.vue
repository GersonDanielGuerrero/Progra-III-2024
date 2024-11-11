<template>
    <div class="perfil-container">
      <section class="datos-personales">
        <h2>Datos personales</h2>
        <CajaTexto placeholder="Nombre" />
        <CajaTexto placeholder="Apellido" />
        <CajaTexto placeholder="Correo electrónico" />
        <CajaTexto placeholder="Número de Celular" />
        <BotonComp texto="Guardar" clase="boton-guardar" />
      </section>
  
      <section class="direcciones">
        <h2>Direcciones</h2>
        <BotonComp texto="Agregar dirección" clase="boton-agregar" />
        <div class="lista-direcciones">
          <div class="direccion">
            <span>Mi casa</span>
            <p>Cancha El Amate (Excirculo Estudiantil Usulután), Primer pasaje, casa 17, Usulután</p>
            <BotonComp texto="Editar" clase="boton-editar" />
            <BotonComp texto="Eliminar" clase="boton-eliminar" />
            <BotonComp texto="Predeterminada" clase="boton-predeterminada" />
          </div>
          <div class="direccion">
            <span>Trabajo</span>
            <p>Colonia el Cocal (Excirculo Estudiantil Usulután), Primer pasaje, Usulután</p>
            <BotonComp texto="Editar" clase="boton-editar" />
            <BotonComp texto="Eliminar" clase="boton-eliminar" />
          </div>
          <div class="direccion">
            <span>Casa 2</span>
            <p>Colonia el Cocal (Excirculo Estudiantil Usulután), Primer pasaje, Usulután</p>
            <BotonComp texto="Editar" clase="boton-editar" />
            <BotonComp texto="Eliminar" clase="boton-eliminar" />
          </div>
        </div>
      </section>

      <section class="mas-opciones">
        <h2>Más opciones</h2>
        <BotonComp texto="Cambio contraseña" clase="boton-cambiar" />
        <BotonComp texto="Eliminar cuenta" clase="boton-eliminar-cuenta" />
      </section>
    </div>
  </template>

<style scoped>
.perfil-container {
  background-color: #000;
  color: #fff;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h2 {
  color: #ffad00;
  margin-bottom: 15px;
}

.datos-personales, .direcciones, .mas-opciones {
  margin-bottom: 30px;
}

.CajaTexto {
  display: block;
  width: 100%;
  margin-bottom: 10px;
  padding: 10px;
  background-color: #000;
  border: 1px solid #ffad00;
  color: #fff;
}

.boton-guardar, .boton-agregar, .boton-editar, .boton-eliminar, .boton-predeterminada, .boton-cambiar, .boton-eliminar-cuenta {
  background-color: #ffad00;
  color: #000;
  border: none;
  padding: 10px 20px;
  margin-right: 10px;
  margin-top: 10px;
  cursor: pointer;
}

.boton-guardar:hover, .boton-agregar:hover, .boton-editar:hover, .boton-eliminar:hover, .boton-predeterminada:hover, .boton-cambiar:hover, .boton-eliminar-cuenta:hover {
  background-color: #fff;
  color: #000;
}

.lista-direcciones {
  display: flex;
  flex-direction: column;
}

.direccion {
  border: 1px solid #ffad00;
  padding: 15px;
  margin-bottom: 20px;
  background-color: #222;
}

.direccion span {
  font-weight: bold;
  color: #ffad00;
  display: block;
  margin-bottom: 8px;
}

.direccion p {
  margin: 0;
  margin-bottom: 10px;
  color: #fff;
}
</style>

<script>
export default {
    name: 'PaginaCuenta',
    data() {
        return {
            
        }
    },
    methods: {
        
    }
}
</script>