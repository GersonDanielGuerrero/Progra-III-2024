<template>
    <div>
        <BarraMenu/>
        <main>
    <h1>Pedidos</h1>
    <div class="controls">
        <select v-model="opcionSelector" class="selector-comp">
        <option value="actuales">Pedidos actuales</option>
        <option value="historial">Historial de pedidos</option>
        </select>
        <CajaTexto
        placeholder="Buscar"
        type="text"
        v-model="filtro"
        />
    </div>
    <div class="pedido-lista">
    <div v-for="pedido in pedidosFiltrados" :key="pedido.id" class="pedido">
    <p class="fecha">{{ pedido.fecha }}</p>
    <p class="cliente">{{ pedido.nombre_cliente }}</p>
    <p class="tipo">{{ pedido.tipo }}</p>
    <p class="direccion">{{ pedido.direccion }}</p>
    <p class="cantidad">
        {{ pedido.cantidad_productos }} {{ pedido.cantidad_productos === 1 ? 'producto' : 'productos' }}
        <span class="precio">$ {{ pedido.total }}</span>
    </p>
    </div>
    </div>
    </main>
    </div>
</template>

<style scoped>
* {
margin: 0;
padding: 0;
box-sizing: border-box;
}

body {
font-family: Arial, sans-serif;
background-color: #111;
color: #fff;
}

h1 {
text-align: center;
margin: 20px 0;
color: #ffad00;
font-weight: bold;
}

.controls {
display: flex;
flex-direction: column; 
align-items: center;
gap: 10px;
margin-bottom: 20px;
max-width: 600px;
margin: 0 auto;
}

.selector-comp {
padding: 10px;
font-size: 16px;
background-color: #ffad00;
color: #000;
border: none;
border-radius: 5px;
font-weight: bold;
}

.pedido-lista {
display: grid;
grid-template-columns: repeat(2,1fr);
gap: 20px;
padding: 20px;
}

.pedido {
background-color: #222;
padding: 20px;
border-radius: 5px;
}

.fecha {
color: #ffad00;
font-weight: bold;
text-align: left;
font-weight: bold;
}

.cliente,
.direccion,
.cantidad,
.tipo {
font-weight: bold;
text-align: left;
margin: 5px 0;
color: #fff
}

.precio {
float: right;
color: #ffad00;
font-weight: bold;
}
</style>

<script>
import BarraMenu from '@/components/BarraMenu.vue';
import CajaTexto from '@/components/CajaTexto.vue';
import ApiService from "@/services/ApiService"; 
import alertify from 'alertifyjs';
import 'alertifyjs/build/css/alertify.css';

export default {
    name: 'ListaPedidos',
    components: {
        BarraMenu,
        CajaTexto,
    },
    data() {
        return {
            opcionSelector: 'actuales',
            filtro: '',
            pedidos:[
                {
                    id: 1,
                    fecha: '2024-11-11 11:11:11',
                    nombre_cliente: 'Juan Perez',
                    tipo: 'Domicilio',
                    direccion: '8va Calle poniente, Barrio La Parroquia, Santa Elena',
                    cantidad_productos: 2,
                    total: 12.50,
                },
                {
                    id: 2,
                    fecha: '2024-11-11 12:44:11',
                    nombre_cliente: 'Maria Lopez',
                    tipo: 'Local',
                    direccion: '4ta Avenida Sur, Barrio El Calvario, Santa Elena',
                    cantidad_productos: 1,
                    total: 5.50,
                },
            ],
            pedidosFiltrados: [
                {
                    id: 1,
                    fecha: '2024-11-11 11:11:11',
                    nombre_cliente: 'Juan Perez',
                    tipo: 'Domicilio',
                    direccion: '8va Calle poniente, Barrio La Parroquia, Santa Elena',
                    cantidad_productos: 2,
                    total: 12.50,
                },
                {
                    id: 2,
                    fecha: '2024-11-11 12:44:11',
                    nombre_cliente: 'Maria Lopez',
                    tipo: 'Local',
                    direccion: '4ta Avenida Sur, Barrio El Calvario, Santa Elena',
                    cantidad_productos: 1,
                    total: 5.50,
                },
            ],
        };
    },
  methods: {
    // Método para obtener los pedidos (actuales o historial)
    async obtenerPedidos() {
      try {
        const respuesta = await ApiService.obtenerPedidos(this.opcionSelector);
        if (respuesta.success) {
          this.pedidos = respuesta.pedidos;
          this.pedidosFiltrados = this.pedidos; // Inicialmente todos los pedidos
        } else {
          alertify.error(respuesta.message || 'Error al obtener los pedidos');
        }
      } catch (error) {
        console.error('Error al obtener pedidos:', error);
        alertify.error('Error al obtener los pedidos');
      }
    },
    
  },
  watch: {
    // Detectar cambios en el selector y obtener los pedidos correspondientes
    opcionSelector() {
      this.obtenerPedidos();
    },
  },
  mounted() {
    // Obtener los pedidos al cargar la página
    this.obtenerPedidos();
  },
};
</script>