<template>
    <div class="container">

        <div class = "row">
            <BarraMenu/>
        </div>
        <BotonComp @click="CargarProducto">
            Recargar
        </BotonComp>

        <h1 class="header-title">{{producto.categoria}}</h1>

        <div class="product-view">
            <div class="product-image">
                <p class="discount-text" v-if="producto.precio_anterior">*Producto en descuento, restricciones aplican.</p>
                <img :src="producto.imagen" alt="Imagen de la Burger Clasica" class="product-img">
                <p class="price">
                    <span class="previous-price" v-if="producto.precio_anterior" > ${{producto.precio_anterior}} </span>
                    <span class="current-price"> ${{producto.precio}} </span>
                </p>
                <p class="description">{{producto.descripcion}}</p>
            </div>
            <div class="product-info">
                <h2 class="product-name">{{ producto.nombre }}</h2>
                <div class="placeholder-div"></div>
                
                <!-- Caja de texto para detalles -->
                <CajaTexto
                    placeholder="Escribe aquí (opcional)" 
                    type="text" 
                    v-model="detalles" 
                />

                <div class="order-section">
                    <div class="total-container">
                        <span class="total-label">Total:</span> <span>${{ total }}</span>
                    </div>
                    <div class="controls-and-button">
                        <div class="quantity-controls">
                            <!-- Botones para cambiar la cantidad -->
                            <button id="subtract" @click="restarCantidad">-</button>
                            <span id="quantity">{{ cantidad }}</span>
                            <button id="add" @click="sumarCantidad">+</button>
                        </div>
                        <!-- Botón para añadir al carrito -->
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
import ApiService from '@/services/ApiService';
import Alertify from 'alertifyjs'
export default{
    name: 'PaginaProducto',

    components: {
        BotonComp,
        CajaTexto,
        BarraMenu,
    },
    data() {
    return {
      producto: {
        id: 0,  
        nombre: 'Burger Clasica',
        descripcion: 'Prueba nuestra deliciosa Burger Clasica...',
        categoria: 'Burgers',
        precioAnterior: 4.75,
        precio: 4.00,
        imagen: 'https://proyectodb.blob.core.windows.net/imgs/Burger_de_la_casa.jpeg',
      },
      cantidad: 1,
      form: {
        detalle: '',
      },
      errores: {
        detalle: false,
      },
    };
  },
  methods: {
    
    sumarCantidad() {
      this.cantidad++;
    },

    
    restarCantidad() {
      if (this.cantidad > 1) {
        this.cantidad--;
      }
    },

    
    async agregarACarrito() {
      const datosCarrito = {
        id: this.producto.id,  
        cantidad: this.cantidad,
        ingredientes: [],  
        detalles: this.form.detalle,  
      };

      const respuesta = await ApiService.agregarACarrito(datosCarrito);
      if (!respuesta.error) {
        console.log('Producto agregado al carrito:', respuesta.datos);
      } else {
        console.error('Error al agregar al carrito:', respuesta.mensaje);
      }
    },
    async CargarProducto(id){
        ApiService.obtenerProducto(id)
      .then((respuesta) => {
        if (!respuesta.error) {
          this.producto = respuesta.datos;
          
        Alertify.success(JSON.stringify(this.producto));
        } else {
          console.error('Error al obtener producto:', respuesta.mensaje);
          Alertify.error('Error al obtener producto');
        }
      });
    },
  },

  computed: {
   
    total() {
      return (this.producto.precio * this.cantidad).toFixed(2);

    }
  },
};
</script>