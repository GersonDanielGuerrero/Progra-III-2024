<template>
     <BarraMenu />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <div class="container">
      <div class="cart">
        <h2>CARRITO (3)</h2>
        <div class="select-all">
          <input type="checkbox" id="select-all">
          <label for="select-all">SELECCIONAR TODOS</label>
          <button class="delete">
           ELIMINAR <i class="fas fa-trash-alt"></i>
        </button>
    </div>
        <div class="cart-item">
          <div class="item-info">
            <input type="checkbox" class="item-checkbox" id="item-1">
            <img src="burger-image.jpg" alt="Burger Guacamole">
            <div class="item-details">
              <h3>BURGER GUACAMOLE</h3>
              <p>Res - Papas G. - 0 Extras</p>
            </div>
          </div>
          <div class="quantity">
            <button>-</button>
            <span>1</span>
            <button>+</button>
          </div>
          <span class="price">$6.75</span>
        </div>
  
        <div class="cart-item">
          <div class="item-info">
            <input type="checkbox" class="item-checkbox" id="item-2">
            <img src="placeholder-image.jpg" alt="Producto">
            <div class="item-details">
              <h3>PRODUCTO</h3>
              <p>Especialidad - Acompañante - Extras</p>
            </div>
          </div>
          <div class="quantity">
            <button>-</button>
            <span>1</span>
            <button>+</button>
          </div>
          <span class="price">$0.00</span>
        </div>
  
        <div class="cart-item">
          <div class="item-info">
            <input type="checkbox" class="item-checkbox" id="item-3">
            <img src="placeholder-image.jpg" alt="Producto">
            <div class="item-details">
              <h3>PRODUCTO</h3>
              <p>Especialidad - Acompañante - Extras</p>
            </div>
          </div>
          <div class="quantity">
            <button>-</button>
            <span>1</span>
            <button>+</button>
          </div>
          <span class="price">$0.00</span>
        </div>
      </div>
  
      <div class="order">
        <h2>REALIZA TU PEDIDO</h2>
        <div class="order-option">
          <p>Escoge el tipo de entrega</p>
          <button>Domicilio</button>
        </div>
        <div class="order-option">
          <p>Selecciona la dirección</p>
          <button>Dirección</button>
        </div>
        <div class="order-option">
          <p>Escoge el método de pago</p>
          <button>Seleccionar</button>
        </div>
        <div class="total">
          <p>Total:</p>
          <span>$6.75</span>
        </div>
        <button class="order-button">PEDIR</button>
      </div>
    </div>
  </template>
  
  <style scoped>
  @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
  }
  
  body, html {
    background-color: #000;
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
  }
  
  .container {
    display: flex;
    gap: 30px;
    width: 100%;
    padding: 40px;
    box-sizing: border-box;
    max-width: 1200px;
    margin: 0 auto;
  }
 
  .cart,
  .order {
    background-color: #333;
    padding: 20px;
    border-radius: 5px;
    width: 70%;
    min-width: 500px;
  }
 
  .cart h2,
  .order h2 {
    color: #ffad00; 
    font-size: 1.2em;
    margin-bottom: 15px;
    width: 100%;
    min-width: 300px;
  }
  .cart h2 {
    text-align: center;
    font-size: 1.2em;
    width: 0.1px;
    min-width: 300px;
    font-weight: bold;
  }
  .select-all {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 15px;
    justify-content: space-between;
  }
  
  .select-all label {
    color:  #ffad00; 
  }
  .select-all input[type="checkbox"],
.item-checkbox {
  appearance: none;
  width: 18px;
  height: 18px;
  border: 2px solid #ffad00;
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  margin-right: 10px;
}

.select-all input[type="checkbox"]:checked,
.item-checkbox:checked {
  background-color: #ffad00;
}


.delete {
  margin-left: auto;
  background: none;
  border: none;
  color: #ffffff;
  font-size: 0.9em;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 20px;
}


  .cart-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 15px;
  }
  
  .item-info {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .item-info img {
    width: 40px;
    height: 40px;
    border-radius: 5px;
  }
  
  .item-details h3 {
    font-size: 1em;
    color: #ffad00; 
    margin-bottom: 5px;
  }
  
  .item-details p {
    font-size: 0.9em;
    color:  #ffad00; 
  } 
  
  .quantity {
    display: flex;
    align-items: center;
    gap: 5px;
    color: #ffad00;
  }
  
  .quantity button {
    background-color: #333;
    border: none;
    color:  #ffad00;
    font-size: 1em;
    width: 20px;
    height: 20px;
    cursor: pointer;
    border-radius: 3px;
  }
  
  .price {
    color: #ffad00;
    font-size: 1em;
  }
  
  .order-option {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
    color: #ffffff;
  }
  
  .order-option p {
    font-size: 0.9em;
    color: #ffffff; 
  }
  
  .order-option button {
    background-color: #ffad00;
    border: none;
    padding: 5px 10px;
    color: #000;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .total {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
    font-size: 1.2em;
    color: #ffad00; 
  }
  
  .total p {
    font-size: 1em;
    color: #ffffff; 
  }
  
  .total span {
    color: #ffad00; 
    font-size: 1em;
  }
  

  .order-button {
    background-color: #ffad00;
    border: none;
    width: 49%;
    padding: 10px;
    color: #000;
    font-weight: bold;
    font-size: 1em;
    cursor: pointer;
    border-radius: 5px;
    margin-top: 20px;
  }
  </style>


<script>
import BarraMenu from '@/components/BarraMenu.vue';
import ApiService from "@/services/ApiService"; 

export default {
  name: 'PaginaCarrito',
    components: {
        BarraMenu
    },
  data() {
    return {
      productos: [],
      direcciones: [],
      direccionSeleccionada: null,
      tipoEntrega: "",
      metodoPago: "",
    };
  },
  computed: {
    totalCarrito() {
      return this.productos
        .filter((producto) => producto.seleccionado)
        .reduce((acc, producto) => acc + producto.precioTotal, 0);
    },
    cantidadProductos() {
      return this.productos.reduce((acc, producto) => acc + producto.cantidad, 0);
    },
  },
  methods: {
    async obtenerCarrito() {
      const respuesta = await ApiService.obtenerCarrito(); 
      if (!respuesta.error) {
        this.productos = respuesta.datos.productos;
      } else {
        alertify.error(respuesta.mensaje);
      }
    },
    async obtenerDirecciones() {
      const respuesta = await ApiService.obtenerDirecciones(); 
      if (!respuesta.error) {
        this.direcciones = respuesta.datos;
      } else {
        alertify.error(respuesta.mensaje);
      }
    },
    async actualizarCarrito() {
      const productosActualizados = this.productos.map(({ id, cantidad }) => ({ id, cantidad }));
      const data = {
        productos: productosActualizados,
        tipo_entrega: this.tipoEntrega,
        id_direccion: this.direccionSeleccionada,
        metodo_pago: this.metodoPago,
      };
      const respuesta = await ApiService.actualizarCarrito(data); 
      if (respuesta.error) {
        alertify.error(respuesta.mensaje);
      }
    },
    async realizarPedido() {
      const productosPedido = this.productos.filter((p) => p.seleccionado);
      if (productosPedido.length === 0 || !this.tipoEntrega || !this.metodoPago || !this.direccionSeleccionada) {
        alertify.error("Por favor completa todos los campos y selecciona al menos un producto.");
        return;
      }
      const data = {
        productos: productosPedido.map(({ id, cantidad }) => ({ id, cantidad })),
        tipo_entrega: this.tipoEntrega,
        id_direccion: this.direccionSeleccionada,
        metodo_pago: this.metodoPago,
      };
      const respuesta = await ApiService.realizarPedido(data); 
      if (respuesta.error) {
        alertify.error(respuesta.mensaje);
      } else {
        alertify.success("Pedido realizado con éxito");
        await this.obtenerCarrito();
      }
    },
    async sumarProducto(id) {
      const respuesta = await ApiService.sumarProducto(id); 
      if (!respuesta.error) {
        await this.obtenerCarrito();
      } else {
        alertify.error(respuesta.mensaje);
      }
    },
    async restarProducto(id) {
      const producto = this.productos.find((p) => p.id === id);
      if (producto.cantidad === 1) {
      alertify.confirm(
          'Eliminar producto',
          '¿Deseas eliminar este producto del carrito?',
          async () => {
            const respuesta = await ApiService.restarProducto(id); 
            if (!respuesta.error) {
              await this.obtenerCarrito();
            } else {
              alertify.error(respuesta.mensaje);
            }
          },
          function() {} 
        );

    }else {
      const respuesta = await ApiService.restarProducto(id); 
      if (!respuesta.error) {
        await this.obtenerCarrito();
      } else {
        alertify.error(respuesta.mensaje);
      }
    }
  },
    async borrarProductos() {
      const productosSeleccionados = this.productos.filter((p) => p.seleccionado);
      if (productosSeleccionados.length === 0) return;
      alertify.confirm(
        'Eliminar productos',
        '¿Deseas eliminar los productos seleccionados?',
        async () => {
          const ids = productosSeleccionados.map((p) => p.id);
          const respuesta = await ApiService.borrarProductos(ids); 
          if (!respuesta.error) {
            await this.obtenerCarrito();
          } else {
            alertify.error(respuesta.mensaje);
          }
        },
        function() {} 
      );
    },
  },
  async mounted() {
    await this.obtenerCarrito();
    await this.obtenerDirecciones();
  },
};
</script>