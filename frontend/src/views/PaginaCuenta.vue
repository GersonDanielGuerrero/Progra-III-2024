<template>
    <BarraMenu />
    <div class="perfil-container">
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
import ApiService from "@/services/ApiService"; 
import alertify from 'alertifyjs';
import 'alertifyjs/build/css/alertify.css';

export default {
  name: 'PaginaCuenta',
  components: {
    BarraMenu,
    CajaTexto,
    BotonComp,
  },
  data() {
  return {
    isLoading: true,
         
      isDatosPersonalesVisible: false,
      isDireccionesVisible: false,
      isMasOpcionesVisible: false,
      
      usuario: {
          nombres: 'Juan Edgardo',
          apellidos: 'Pérez García',
          correo: 'juanpe@gmail.com',
          telefono: '3563-4232',
        },
        direcciones: [
          {
            id:'1',
            nombre: 'Casa',
            direccion: 'Cancha El Amate (Excirculo Estudiantil Usulután), Primer pasaje, casa 17, Usulután',
            predeterminada:true,
          },
          {
            id:'2',
            nombre: 'Mi casa',
            direccion: 'Cancha El Amate (Excirculo Estudiantil Usulután), Primer pasaje, casa 17, Usulután',
            predeterminada:false,
          },
          {
            id:'3',
            nombre: 'Trabajo',
            direccion: 'Colonia el Cocal (Excirculo Estudiantil Usulután), Primer pasaje, Usulután',
            predeterminada:false,
          },
        ],
        roles: [],
    mensaje: '',
    error: false,
  };
},

 methods: {
   // Método para redirigir a la página para añadir una nueva dirección
   agregarDireccion() {
    this.$router.push({
      path: "/direccion",
      state: { accion: "añadir" }
    });
  },

  // Método para redirigir a la página para editar una dirección existente
  editarDireccion(id) {
    this.$router.push({
      path: "/direccion",
      state: { accion: "editar", id }
    });
  }
},
  async guardarDatosUsuario() {
      try {
        const respuesta = await ApiService.guardarDatosUsuario(this.usuario);
        if (!respuesta.error) {
          alertify.success('Datos guardados correctamente');
        } else {
          alertify.error('Error al guardar los datos');
        }
      } catch (error) {
        console.error("Error al guardar los datos del usuario:", error);
        alertify.error('Ocurrió un error al guardar los datos');
      }
    },
    async marcarDireccionPredeterminada(id) {
      try {
        const respuesta = await ApiService.marcarPredeterminada(id);
        if (!respuesta.error) {
          this.direcciones = this.direcciones.map(direccion => ({
            ...direccion,
            predeterminada: direccion.id === id,
          }));
          alertify.success('Dirección marcada como predeterminada');
        } else {
          alertify.error('Error al marcar la dirección como predeterminada');
        }
      } catch (error) {
        console.error("Error al marcar la dirección predeterminada:", error);
        alertify.error('Ocurrió un error al marcar la dirección predeterminada');
      }
    },

async mounted() { 
    try {
      const respuesta = await ApiService.cargarDatos();
      
      if (!respuesta.error) {
        
        this.usuario = respuesta.datos.usuario;
        this.direcciones = respuesta.datos.direcciones;
        this.roles = respuesta.datos.roles;
        
       
        alertify.success('Datos cargados correctamente');
      } else {
       
      }
    } catch (error) {
     
      console.error("Error en la carga de datos:", error);
      alertify.error('Ocurrió un error al cargar los datos');
    }
  }
};
</script> 