<template>
    <div class = "container">
        <div class = "row">
            <BarraMenu />
        </div>
        <div class = "row">

        </div>
        <div class = "row lista-categorias">
            <div class = "col-2" v-for="categoria in categorias" :key="categoria.id"
            @click="abrirMenu(categoria.nombre)"
            >
                <CategoriaComp :categoria="categoria"/>
            </div>
        </div>
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
  import ApiService from '@/services/ApiService'; 
import BarraMenu from '@/components/BarraMenu.vue';
import CategoriaComp from "@/components/CategoriaComp.vue";
  
  export default {
    data() {
      return {
        categorias: [{
            id: 1,
            nombre: 'burgers',
            imagen: 'https://th.bing.com/th/id/R.c691ed37c9ce3040c3ebd2892e88870c?rik=QUBcFflN%2b9oqPQ&pid=ImgRaw&r=0'
        },
        {
            id: 2,
            nombre: 'snacks',
            imagen: 'img/image2.png'
        },
        {
            id: 3,
            nombre: 'bebidas',
            imagen: 'img/image3.png'
        },
        {
            id: 4,
            nombre: 'combos',
            imagen: 'img/image4.png'
        },
        {
            id: 5,
            nombre: 'promociones',
            imagen: 'img/image5.png'
        }
    ], 
        anuncio: []  
      };
    },
    components: {
      BarraMenu,
      CategoriaComp,
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
      },
        abrirMenu(categoria) {
            this.$router.push({ name: 'PaginaMenu', query: { categoria } });
        }
    },
    mounted() {
      this.cargarDatos();
    }
  };
  </script>
  