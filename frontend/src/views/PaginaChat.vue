<template>
    <div>
        
    </div>
</template>

<style scoped>

</style>

<script>
//Importaciones de componentes

import { useAuthStore } from "@/stores/auth";
import ApiService from "@/services/ApiService"; 
import alertify from 'alertifyjs';
import 'alertifyjs/build/css/alertify.css';

//Fin de importaciones de componentes

export default {
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