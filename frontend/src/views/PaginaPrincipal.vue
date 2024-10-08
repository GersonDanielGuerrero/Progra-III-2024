<template>
    <div>

    </div>
</template>

<style scoped>
    

</style>

<!-- C U I D A D I T O -->

<script>

export default {
    name: 'PaginaPrincipal',
    components: {
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
  