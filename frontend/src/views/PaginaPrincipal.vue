<template>
    <div>
      <BarraMenu/>
    </div>

    <div>
        <section class="menu">
        <div class="menu-title">
            <div class="line"></div>
             <h2>MENU</h2>
            <div class="line"></div>
        </div>
        <div class="menu-grid">
            <div class="menu-item">
                <p>Burgers</p>
                <img src="img/image1.png" alt="Burgers">
               
            </div>
            <div class="menu-item">
                <p>Snacks</p>
                <img src="img/image2.png" alt="Snacks">
                
            </div>
            <div class="menu-item">
                <p>Bebidas</p>
                <img src="img/image3.png" alt="Bebidas">
               
            </div>
            <div class="menu-item">
                <p>Combos</p>
                <img src="img/image4.png" alt="Combos">
               
            </div>
            <div class="menu-item">
                <p>Promociones</p>
                <img src="img/image5.png" alt="Promociones">
                
            </div>
        </div>
    </section>
    </div>
</template>
 
<style scoped>
/* Estilos de menú */
.menu {
  padding: 20px;
  text-align: center;
}

.menu-title {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  position: relative;
}

.menu-title h2 {
  font-size: 23px;
  color: #fff;
  margin: 0 20px;
}

.menu-title .line {
  height: 2px;
  background-color: #ffae00;
  flex: 1;
}

.menu-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
}

.menu-item {
  background-color: #2f2e2e;
  padding: 20px;
  text-align: center;
  border-radius: 10px;
}

.menu-item img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  margin-bottom: 10px;
}

.menu-item p {
  color: #ffffff;
  font-size: 18px;
  font-weight: bold;
}

img {
  max-width: 150px;
  max-height: 290px;
  object-fit: cover;
}

</style>

<!-- C U I D A D I T O -->

<script>
import BarraMenu from '@/components/BarraMenu.vue';


export default {
    name: 'PaginaPrincipal',
    components: {
        BarraMenu
        
    },
    data() {
        return {
            
        }
    },
    props: {
        
    },
    methods: {
        
    },
    computed: {
        
    },

}
</script>

<template>
    <div>
      <h1>Página Principal</h1>
      <div v-if="categorias.length">
        <h2>Categorías:</h2>
        <ul>
          <li v-for="categoria in categorias" :key="categoria.id">
            {{ categoria.nombre }} - <img :src="categoria.url_foto" :alt="categoria.nombre" />
          </li>
        </ul>
      </div>
  
      <div v-if="anuncio.length">
        <h2>Anuncios:</h2>
        <ul>
          <li v-for="item in anuncio" :key="item.id">
            <a :href="item.url_redireccion">
              <img :src="item.url_foto" :alt="'Anuncio ' + item.id" />
            </a>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import ApiService from '@/apiservice.js'; 
  
  export default {
    data() {
      return {
        categorias: [], 
        anuncio: []  
      };
    },
    methods: {
      async cargarDatos() {
        try {

          const categoriasData = await ApiService.obtenerCategorias();
          const anunciosData = await ApiService.obtenerAnuncios();
  

          this.categorias = categoriasData;
          this.anuncio = anunciosData;
  
        } catch (error) {
          console.error('Error al cargar los datos:', error);
        }
      }
    },
    mounted() {
      this.cargarDatos();
    }
  };
  </script>
  
  <style scoped>
  </style>
  