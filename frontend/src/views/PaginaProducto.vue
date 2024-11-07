<template>
    <div class="container">

        <div class = "row">
            <BarraMenu/>
        </div>

        <h1 class="header-title">{{producto.categoria}}</h1>

        <div class="product-view">
            <div class="product-image">
                <p class="discount-text" v-if="producto.precio_anterior">*Producto en descuento, restricciones aplican.</p>
                <img :src="producto.imagen" alt="Imagen de la Burger Clasica" class="product-img">
                <p class="price">
                    <span class="previous-price" v-if="producto.precio_anterior" >${{producto.precio_anterior}}</span>
                    <span class="current-price">${{producto.precio}}</span>
                </p>
                <p class="description">{{producto.descripcion}}</p>
            </div>
            <div class="product-info">
                <h2 class="product-name">{{ producto.nombre }}</h2>
                <div class="placeholder-div"></div>
                
                <CajaTexto
                    placeholder="Escribe aquí (opcional)" 
                    type="text" 
                    v-model="detalles" 
                />

                <div class="order-section">
                    <div class="total-container">
                        <span class="total-label">Total:</span> <span>$4.75</span>
                    </div>
                    <div class="controls-and-button">
                        <div class="quantity-controls">
                            <button id="subtract" @click="restarCantidad">-</button>
                            <span id="quantity">{{ cantidad }}</span>
                            <button id="add" @click="sumarCantidad">+</button>
                        </div>
                        <BotonComp @metodo_click="agregarACarrito">Añadir a mi orden 🛒</BotonComp>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
    color: #fff;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.header-title {
    text-align: center;
    font-size: 1.8em;
    color: #fff;
    margin-bottom: 20px;
    font-weight: bold;
}

.product-view {
    display: flex;
    justify-content: center; 
    gap: 30px;
}

.product-img {
    width: 500px; 
    height: 500px; 
    object-fit: cover;
    border-radius: 8px;
    background-color: transparent;
}

.discount-text {
    font-size: 0.9em;
    color: #ffad00;
    text-align: center;
    margin-bottom: 10px;
    font-weight: bold;
    width: 100%;
}

.placeholder-div {
    width: 750px; 
    height: 400px;
    background-color: #333;
    border: 1px solid #ffad00;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ffad00;
    font-size: 1.2em;
}

.price {
    display: flex;
    justify-content: space-between;
    width: 400px; 
    margin-top: 10px;
    font-size: 1.2em;
    color: #fff;
    font-weight: bold;
}

.previous-price {
    text-decoration: line-through;
    color: #ffad00;
    font-size: 1.1em;
}

.current-price {
    color: #fff;
    font-size: 1.3em;
    margin-left: 375px;
}

.description {
    font-size: 0.9em;
    color: #fff;
    padding-top: 10px;
    max-width: 500px;
    font-weight: bold;
    text-align: left;
}

.product-info {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.product-name {
    font-size: 1.6em;
    font-weight: bold;
    color: #ffad00;
    text-align: center;
    margin-top: 10px;
}

.order-section {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    margin-top: 10px;
    font-weight: bold;
}

.total-container {
    font-size: 1.2em;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 5px;
}

.total-label {
    color: #fff;
}

.total-container span:last-child {
    color: #ffad00;
}

.controls-and-button {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
    margin-top: 15px;
}

.quantity-controls {
    display: flex;
    align-items: center;
    gap: 10px;
    justify-content: center;
    font-weight: bold;
}

.quantity-controls button {
    background-color: #333;
    border: none;
    padding: 5px 10px;
    color: #ffad00;
    font-weight: bold;
    font-size: 1.2em;
    cursor: pointer;
}

.quantity-controls span {
    font-size: 1.2em;
    color: #fff;
}

</style>

<script>
import BarraMenu from '@/components/BarraMenu.vue';
import BotonComp from '@/components/BotonComp.vue';
import CajaTexto from '@/components/CajaTexto.vue';
export default{
    name: 'PaginaProducto',

    components: {
        BotonComp,
        CajaTexto,
        BarraMenu,
    },
    data(){
        return{
            producto: {
                // DATOS DE PRUEBA
                id: 1,
                nombre: 'Burger Clasica',
                precio: 4.75,
                precio_anterior: 5.25,
                categoria: 'burgers',
                descripcion: 'Prueba nuestra deliciosa Burger Clasica con 100g de carne de res o pollo con queso amarillo, tomate, lechuga, cebolla, incluye papas fritas y salsa de la casa.',
                imagen: 'https://th.bing.com/th/id/R.c691ed37c9ce3040c3ebd2892e88870c?rik=QUBcFflN%2b9oqPQ&pid=ImgRaw&r=0',
            },
            detalles: '',
            cantidad: 1,

        };
    },
    methods:{
    },
    computed:{
        total(){
            return this.producto.precio * this.cantidad;
        }
    }
}
</script>