<template>
    <BarraMenu />
    <div class="perfil-container">
      <!-- Datos Personales -->
      <section class="datos-personales">
        <h2 @click="toggleDatosPersonales">Datos personales</h2>
        <div v-show="isDatosPersonalesVisible" class="campos">
          <CajaTexto v-model="formDatosPersonales.nombre" placeholder="Nombre*" />
          <CajaTexto v-model="formDatosPersonales.apellido" placeholder="Apellido*" />
          <CajaTexto v-model="formDatosPersonales.email" placeholder="Correo electrónico*" />
          <CajaTexto v-model="formDatosPersonales.telefono" placeholder="Número de Celular*" />
        </div>
        <div v-show="isDatosPersonalesVisible" class="boton-guardar">
          <BotonComp class="guardar" @click="guardarDatosPersonales">Guardar</BotonComp>
        </div>
      </section>
  
      <!-- Direcciones -->
      <section class="direcciones">
        <h2 @click="toggleDirecciones">Direcciones</h2>
        <div v-show="isDireccionesVisible" class="boton-agregar">
          <BotonComp @click="agregarDireccion">Agregar dirección</BotonComp>
        </div>
        <div v-show="isDireccionesVisible" class="lista-direcciones">
          <div v-for="(direccion, index) in direcciones" :key="index" class="direccion">
            <span>{{ direccion.nombre }}</span>
            <p>{{ direccion.direccion }}</p>
            <div class="acciones">
              <BotonComp @click="editarDireccion(index)">Editar</BotonComp>
              <BotonComp @click="eliminarDireccion(index)">Eliminar</BotonComp>
              <BotonComp @click="marcarPredeterminada(index)">Predeterminada</BotonComp>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Más opciones -->
      <section class="mas-opciones">
        <h2 @click="toggleMasOpciones">Más opciones</h2>
        <div v-show="isMasOpcionesVisible" class="opciones-botones">
          <div class="opcion">
            <span>Cambio Contraseña</span>
            <BotonComp class="boton-cambiar" @click="cambiarContraseña">Cambiar</BotonComp>
            <span>Eliminar Cuenta</span>
            <BotonComp class="boton-eliminar" @click="eliminarCuenta">Eliminar</BotonComp>
          </div>
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
    gap: 20px;
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
    padding: 18px 16px;
    font-size: 0.9em;
    border-radius: 5px;
    display: inline-block;
    margin: 0 auto;
    text-align: center;
    cursor: pointer;
    background-color:#010101;
    color: #fcfcfc;
    padding: 10px 15px;
    border-radius: 5px;
  }
  .guardar:hover {
    background-color: #fff;
    color: #000;
    transition: 0.3s;
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
    margin-top: 10px;
  }
  

  .opciones-botones {
    display: flex;
    justify-content: center;
    gap: 30px;
  }

  .opcion  {
    display: flex;
    align-items: center;
    gap: 10px;
      
  }
  
  .opcion span {
    font-weight: bold;
    color: #fcfcfc;
    margin-bottom: 3px;
  }

  
  .boton-cambiar,
  .boton-eliminar {
    background-color: #000000;
    color: #ffffff;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .boton-cambiar:hover,
  .boton-eliminar:hover {
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
      // Datos personales
      formDatosPersonales: {
        nombre: '',
        apellido: '',
        email: '',
        telefono: '',
      },
      // Direcciones
      direcciones: [
        {
          nombre: 'Casa',
          direccion: 'Cancha El Amate (Excirculo Estudiantil Usulután), Primer pasaje, casa 17, Usulután',
        },

        {
          nombre: 'Mi casa',
          direccion: 'Cancha El Amate (Excirculo Estudiantil Usulután), Primer pasaje, casa 17, Usulután',
        },
        {
          nombre: 'Trabajo',
          direccion: 'Colonia el Cocal (Excirculo Estudiantil Usulután), Primer pasaje, Usulután',
        },
      ],
      // Opciones adicionales
      isDatosPersonalesVisible: false,
      isDireccionesVisible: false,
      isMasOpcionesVisible: false,
    };
  },
  methods: {
    // Toggle secciones desplegables
    toggleDatosPersonales() {
      this.isDatosPersonalesVisible = !this.isDatosPersonalesVisible;
    },
    toggleDirecciones() {
      this.isDireccionesVisible = !this.isDireccionesVisible;
    },
    toggleMasOpciones() {
      this.isMasOpcionesVisible = !this.isMasOpcionesVisible;
    },
    // Guardar datos personales
    guardarDatosPersonales() {
      console.log('Datos personales guardados:', this.formDatosPersonales);
      // Aquí puedes enviar esta información a un servidor o almacenarla
    },

    // Editar una dirección
    editarDireccion(index) {
      const direccion = this.direcciones[index];
      console.log('Editando dirección:', direccion);
      // Aquí puedes implementar la edición de la dirección
    },
    // Eliminar una dirección
    eliminarDireccion(index) {
      this.direcciones.splice(index, 1);
      console.log('Dirección eliminada');
    },
    // Marcar dirección como predeterminada
    marcarPredeterminada(index) {
      this.direcciones.forEach((dir, idx) => {
        if (idx === index) {
          dir.predeterminada = true;
        } else {
          dir.predeterminada = false;
        }
      });
      console.log('Dirección predeterminada:', this.direcciones[index]);
    },
    // Cambio de contraseña
    cambiarContraseña() {
      console.log('Cambio de contraseña solicitado');
    },
    // Eliminar cuenta
    eliminarCuenta() {
      console.log('Cuenta eliminada');
    },
  },
};
</script>
