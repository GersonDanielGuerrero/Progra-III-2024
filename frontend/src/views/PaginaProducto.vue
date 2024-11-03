<template>
    <div class="container">
        <header>
            <h1 class="header-title">BURGERS</h1>
        </header>
        <main class="product-view">
            <div class="product-image">
                <p class="discount-text">*Producto en descuento, restricciones aplican.</p>
                <img src="/frontend/public/imagenes/logo_color.png" alt="Imagen de la Burger Clasica" class="product-img">
                <p class="price">
                    <span class="previous-price">$4.75</span>
                    <span class="current-price">$4.00</span>
                </p>
                <p class="description">Prueba nuestra deliciosa Burger Clasica con 100g de carne de res o pollo con queso amarillo, tomate, lechuga, cebolla, incluye papas fritas y salsa de la casa.</p>
            </div>
            <div class="product-info">
                <h2 class="product-name">Burger Clasica</h2>
                <div class="placeholder-div"></div>
                
                <CajaTexto
                    placeholder="Escribe aquí (opcional)" 
                    type="text" 
                    v-model="form.detalle" 
                    :invalido="errores.detalle" 
                    :msg_error="errores.detalle"
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
    background-color: #000;
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
    margin-top: 75px;
    font-weight: bold;
}

.product-view {
    display: flex;
    gap: 30px;
}

.product-img {
    width: 90%;
    height: auto;
    background-color: #ffad00;
    object-fit: cover;
    border-radius: 8px; 
}

.discount-text {
    position: absolute;
    top: -20px;
    font-size: 0.9em;
    color: #ffad00;
    text-align: center;
    width: 100%;
    margin-right: 60px;
    font-weight: bold;
}

.placeholder-div {
    width: 100%;
    padding-top: 50%;
    background-color: #333;
    border: 1px solid #ffad00;
    margin-top: 15px;
}

.price {
    display: flex;
    justify-content: space-between;
    width: 90%;
    margin: 10px auto;
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
    margin-left: 10px;
}

.description {
    font-size: 0.9em;
    color: #fff;
    text-align: center;
    padding: 0 10px;
    max-width: 90%;
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
    margin-top: 20px;
    font-weight: bold;
}

.order-section {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    margin-top: 20px;
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
}

.quantity-controls {
    display: flex;
    align-items: center;
    gap: 10px;
    justify-content: center;
    margin-right: 65px;
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
import BotonComp from '@/components/BotonComp.vue';
import CajaTexto from '@/components/CajaTexto.vue';
export default{
    name: 'PaginaProducto',

    components: {
        BotonComp,
        CajaTexto,
    },
    data(){
        return{
        };
    },
    methods:{
    }
}
</script>