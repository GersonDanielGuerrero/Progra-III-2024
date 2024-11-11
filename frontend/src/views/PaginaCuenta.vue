<template>
    <div class="Datos-personales">
      <h2>Datos personales</h2>
      <div class="campos">
        <div class="campo">
          <CajaTexto icono="👤" placeholder="Nombre" />
        </div>
        <div class="campo">
          <CajaTexto icono="👤" placeholder="Apellido" />
        </div>
        <div class="campo">
          <CajaTexto icono="✉" placeholder="Correo electrónico" />
        </div>
        <div class="campo">
          <CajaTexto icono="📞" placeholder="Número de Celular" />
        </div>
      </div>
      <div class="boton-guardar">
        <BotonComp texto="Guardar" clase="guardar" />
      </div>
    </div>
</template>

<style scoped>
.datos-personales {
  background-color: #000; 
  color: #fff; 
  padding: 20px;
  border-radius: 10px;
  width: 600px;
  margin: 20px auto;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
}

h2 {
  color: #ffad00; 
  text-align: center;
  margin-bottom: 20px;
}

.campos {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.campo {
  display: flex;
  align-items: center;
}

.campo CajaTexto {
  width: 100%;
}


.boton-guardar {
  text-align: center;
  margin-top: 20px;
}

.guardar {
  background-color: #ffad00; 
  color: #000;
  padding: 10px 30px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.guardar:hover {
  background-color: #fff;
  color: #000;
}
</style>

<script>
export default {
    name: 'PaginaCuenta',
    components: {
    
    },
    data() {
        return {
            
        }
    },
    methods: {
        
    }
}
</script>