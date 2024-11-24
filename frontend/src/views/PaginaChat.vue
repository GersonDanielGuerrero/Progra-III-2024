<template>
  <BarraMenu/>
  <div class="container">
    <h1>
      Chat de atención al cliente
      <span v-if="usuario.esEmpleado && clienteActual">
        - {{ clienteActual.nombre }}
      </span>
      <span v-if="versionIA"> - IA</span>
    </h1>

    <div class="row">
      <div 
        class="comp1 col-md-4" 
        v-if="usuario.esEmpleado && (pantallaGrande || componenteMostrado === 1)"
      >
        <h2>Clientes</h2>
        <div class="lista-clientes">
          <div 
            v-for="cliente in clientes" 
            :key="cliente.id" 
            class="cliente" 
            @click="seleccionarCliente(cliente)"
          >
            <strong>{{ cliente.nombre }}</strong>
            <p class="ultimo-mensaje">
              {{ cliente.ultimo_mensaje }}
            </p>
            <small>{{ cliente.fecha_ultimo_mensaje }}</small>
          </div>
        </div>
      </div>

      <div 
        class="comp2 col-md-8 col-sm-12" 
        v-if="componenteMostrado === 2 || pantallaGrande"
      >
        <h2>Mensajes</h2>
        <div class="lista-mensajes">
          <div 
            v-for="(mensaje, index) in mensajes" 
            :key="index" 
            :class="['mensaje', mensaje.enviado ? 'enviado' : 'recibido']"
          >
            <span>{{ mensaje.contenido }}</span>
            <small>{{ mensaje.fecha }}</small>
          </div>
        </div>

        <div class="input-container">
        <CajaTexto 
          v-model="mensajeActual" 
          placeholder="Escribe tu mensaje..."
          
        />
        <button 
            class="btn btn-primary enviar-btn" 
            @click="enviarMensaje"
          >
            Enviar
          </button>
        </div>
      </div>
    </div>

    <BotonComp @click="cambiarVersion">
      <i class="fas fa-hand-paper"></i>
      Cambiar Versión
    </BotonComp>

    <BotonComp
      v-if="usuario.esEmpleado && !pantallaGrande" 
      @click="cambiarComponente"
    >
      {{ "Mostrar " + (componenteMostrado === 1 ? "Mensajes" : "Clientes") }}
    </BotonComp>
  </div>
</template>

<style>
h1 {
  margin-top: 20px;
  text-align: center;
  font-family: 'Arial-Black';
  color: #ffad00;
}

.row {
  height: 70vh;
  display: flex;
}

.comp1, .comp2 {
  padding: 20px;
  border: 4px solid #ffad00;
  color: #ffad00;
  overflow-y: auto;
}

.comp2 {
  border-color: palevioletred;
  color: palevioletred;
}

.lista-clientes, .lista-mensajes {
  height: 90%;
  display: flex;
  flex-direction: column-reverse;
  overflow-y: auto;
}

.cliente {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
}

.cliente:hover {
  background-color: #f9f9f9;
}

.ultimo-mensaje {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis; 
}

.mensaje {
  margin: 10px 0;
  padding: 10px;
  border-radius: 10px;
}

.mensaje.enviado {
  background-color: #e0ffe0;
  text-align: right;
}

.mensaje.recibido {
  background-color: #ffe0e0;
  text-align: left;
}

.input-container {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

.enviar-btn {
  background-color: #ffad00;
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
}

.enviar-btn:hover {
  background-color: #ff8c00;
}

</style>

<script>
//Importaciones de componentes

import { useAuthStore } from "@/stores/auth";
import ApiService from "@/services/ApiService"; 
import alertify from 'alertifyjs';
import 'alertifyjs/build/css/alertify.css';
import BarraMenu from "@/components/BarraMenu.vue";
import CajaTexto from "@/components/CajaTexto.vue";
import BotonComp from "@/components/BotonComp.vue";
//Fin de importaciones de componentes

export default {
  components: {
    BarraMenu,
    CajaTexto,
    BotonComp,
  },
    name: 'PaginaChat',
    data() {
        return {
            comp1permitido: true,
            componenteMostrado: 2, // 1 = Clientes, 2 = Mensajes
            pantallaGrande: false,
            versionIA: false,
            mensajeActual: "",
            mensajes: [],
            clientes: [],
            clienteActual: null,
            esCliente: false,
            esEmpleado: false,
        }
    },
    computed: {
    // Obtener usuario del auth store
    usuario() {
      return useAuthStore().getUsuario();
    },
  },
  methods: {
    // Cambiar entre la vista de clientes y mensajes
    cambiarComponente() {
      this.componenteMostrado = this.componenteMostrado === 1 ? 2 : 1;
    },

    // Actualizar el estado de pantalla grande en función del tamaño de la ventana
    actualizarPantallaGrande() {
      this.pantallaGrande = window.innerWidth > 768;
    },

    // Cambiar la versión de IA y obtener los mensajes nuevamente
    async cambiarVersion() {
      this.versionIA = !this.versionIA;
      try {
        await this.obtenerMensajes(this.versionIA, this.clienteActual?.id);
      } catch (error) {
        alertify.error('Error al cambiar la versión de IA');
      }
    },

    // Seleccionar un cliente y cargar los mensajes
    async seleccionarCliente(idCliente) {
      try {
        this.clienteActual = this.clientes.find((cliente) => cliente.id === idCliente);
        if (!this.clienteActual) {
          alertify.error('Cliente no encontrado');
          return;
        }
        await this.obtenerMensajes(this.versionIA, this.clienteActual.id);
      } catch (error) {
        alertify.error('Error al seleccionar el cliente');
      }
    },

    // Obtener los clientes (para el empleado)
    async obtenerClientes() {
      if (this.esEmpleado) {
        try {
          const respuesta = await ApiService.obtenerClientes();
          this.clientes = respuesta;
          this.clientes.sort((a, b) => new Date(b.fecha_ultimo_mensaje) - new Date(a.fecha_ultimo_mensaje));
        } catch (error) {
          alertify.error('Error al obtener los clientes');
        }
      }
    },

    // Obtener los mensajes del cliente o IA
    async obtenerMensajes(versionIA, idCliente) {
      try {
        const respuesta = await ApiService.obtenerMensajes(versionIA, idCliente);
        this.mensajes = respuesta.mensajes.sort((a, b) => new Date(a.fecha) - new Date(b.fecha));
      } catch (error) {
        alertify.error('Error al obtener los mensajes');
      }
    },

    // Inicializar la pantalla al cargar
    async mounted() {
      try {
        this.esCliente = this.usuario.roles.includes("Atención al cliente");
        this.esEmpleado = this.usuario.roles.includes("Cliente");
        if (this.esEmpleado) {
          await this.obtenerClientes();
        }
        this.actualizarPantallaGrande();
        window.addEventListener("resize", this.actualizarPantallaGrande);
      } catch (error) {
        alertify.error('Error al inicializar la pantalla');
      }
    },
  },
};
</script>