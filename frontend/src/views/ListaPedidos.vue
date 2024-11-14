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
        <p class="cliente">{{ pedido.cliente }}</p>
        <p class="tipo">{{ pedido.tipo }}</p>
        <p class="direccion">{{ pedido.direccion }}</p>
        <p class="cantidad">{{ pedido.cantidad }} <span class="precio">{{ pedido.precio }}</span></p>
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
}

.pedido-lista {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
gap: 20px;
padding: 20px;
}

.pedido {
background-color: #444;
padding: 20px;
border-radius: 5px;
}

.fecha {
color: #ffad00;
font-weight: bold;
}

.cliente,
.direccion,
.cantidad
.tipo {
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

//Importaciones de componentes


//Fin de importaciones de componentes
export default {
    name: 'ListaPedidos',
    components: {
        BarraMenu,
        CajaTexto,
    },
    data() {
        return {

        };
    },
}
</script>