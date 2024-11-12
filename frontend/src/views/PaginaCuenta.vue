<template>
    <BarraMenu />
    <div class="perfil-container">
      <section class="datos-personales">
        <h2>Datos personales</h2>
        <div class="campos">
          <CajaTexto placeholder="Nombre" />
          <CajaTexto placeholder="Apellido" />
          <CajaTexto placeholder="Correo electrónico" />
          <CajaTexto placeholder="Número de Celular" />
        </div>
        <div class="boton-guardar">
          <BotonComp class="guardar">Guardar</BotonComp>
        </div>
      </section>
  
      <section class="direcciones">
        <h2>Direcciones</h2>
        <div class="boton-agregar">
          <BotonComp>Agregar dirección</BotonComp>
        </div>
        <div class="lista-direcciones">
          <div class="direccion">
            <span>Mi casa</span>
            <p>Cancha El Amate (Excirculo Estudiantil Usulután), Primer pasaje, casa 17, Usulután</p>
            <div class="acciones">
              <BotonComp> Editar </BotonComp>
              <BotonComp> Eliminar </BotonComp>
              <BotonComp> Predeterminada </BotonComp>
            </div>
          </div>
          <div class="direccion">
            <span>Trabajo</span>
            <p>Colonia el Cocal (Excirculo Estudiantil Usulután), Primer pasaje, Usulután</p>
            <div class="acciones">
                <BotonComp> Editar </BotonComp>
                <BotonComp> Eliminar </BotonComp>
                <BotonComp> Predeterminada </BotonComp>
            </div>
          </div>
          <div class="direccion">
            <span>Casa 2</span>
            <p>Colonia el Cocal (Excirculo Estudiantil Usulután), Primer pasaje, Usulután</p>
            <div class="acciones">
                <BotonComp> Editar </BotonComp>
                <BotonComp> Eliminar </BotonComp>
                <BotonComp> Predeterminada </BotonComp>
            </div>
          </div>
        </div>
      </section>
      <section class="mas-opciones">
        <h2>Más opciones</h2>
        <div class="opciones-botones">
          <BotonComp class="boton-cambiar">Cambiar contraseña</BotonComp>
          <BotonComp class="boton-eliminar-cuenta">Eliminar cuenta</BotonComp>
        </div>
      </section>
    </div>
  </template>
  
  <style scoped>

  .perfil-container {
    background-color: #000;
    color: #fff;
    padding: 10px;
    font-family: Arial, sans-serif;
    max-width: 2000px;
    margin: auto;
    border-radius: 0;
  }
  
  h2 {
    color: #fff;
    text-align: left;
    font-size: 1.4em;
    margin-bottom: 10px;
  }
  
  .campos {
    display: grid;
    grid-template-columns: 2fr 2fr;
    gap: 40px;
    margin-bottom: 20px;
  }
  
  .boton-guardar {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 20px;

  }
  
  .guardar {
    background-color: #ffad00;
    color: #000;
    padding: 0 16px;
    font-size: 0.9em;
    border-radius: 5px;
    display: inline-block;
    margin: 0 auto;
    text-align: center;
    cursor: pointer;
  }
  
  .direcciones {
    text-align: left;
    margin-bottom: 10px;
  }
  
  .boton-agregar {
  background-color: #ffad00;
  color: #000;
  padding: 0 16px; 
  font-size: 0.9em; 
  border-radius: 5px;
  width: auto; 
  display: inline-block; 
  margin: 0 auto; 
  text-align: center;
  background-color: #000000;
  color: #ffffff;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;

  }
  
  .boton-agregar:hover {
    background-color: #fff;
    color: #000;
    transition: 0.3s;
  }
  
  .lista-direcciones {
    display: flex;
    gap: 30px;
    margin-bottom: 20px;
    text-align: left;

  }

  .direccion {
    border: 1px solid #000; 
    background-color: #000000;
    padding: 15px;
    width: 100%;
    border-radius: 5px;
    text-align: left; }
  
  .direccion span {
    font-weight: bold;
    color: #ffad00;
    margin-bottom: 5px;
  }
  
  .direccion p {
    font-size: 0.9em;
    line-height: 1.5;
    margin: 0;
    color: #fff;
  }
  
  
  .acciones {
    display: flex;
    justify-content: flex-start;
    gap: 10px;
    margin-top: 10px;
    justify-content: flex-start;
  }
  
  .icono {
    background: none;
    border: none;
    color: #ffad00;
    font-size: 1.2em;
    cursor: pointer;
  }
  
  .filled {
    color: #ffad00; 
  }
  
  .far {
    color: #ccc; 
  }
  
  .mas-opciones {
    text-align: left;
    margin-top: 30px;
  }
  
  .opciones-botones {
    display: flex;
    justify-content: center;
    gap: 30px;
  }
  
  .boton-cambiar,
  .boton-eliminar-cuenta {
    background-color: #000000;
    color: #ffffff;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .boton-cambiar:hover,
  .boton-eliminar-cuenta:hover {
    background-color: #fff;
    color: #000;
    transition: 0.3s;
  }
  </style>


<script>
import BarraMenu from '@/components/BarraMenu.vue';
import CajaTexto from '@/components/CajaTexto.vue';
import BotonComp from '@/components/BotonComp.vue';
export default {
    name: 'PaginaCuenta',
    components: {
     BarraMenu,
     CajaTexto,
     BotonComp,
    },
    data() {
        return {
            
        }
    },
    methods: {
        
    }
}
</script>