<template>
    <div class = "container-fluid">
        <div class = "row">
            <BarraMenu />
        </div>
        <div class = "row">
        </div>
        <div class = "row lista-categorias">
            <div class = "col-3" v-for="categoria in categorias" :key="categoria.id"
            @click="abrirMenu(categoria.nombre)"
            >
                <CategoriaComp class="categoria" :categoria="categoria"/>
            </div>
        </div>
    </div>
    <div class = "footer">
      <p>
        Esto de aquí sería el footer, pero no se nos proporcionó la informacion necesaria
      </p>
    </div>
</template>
 
<style scoped>
.categoria{
  margin:10px;
}
.container-fluid{
  height: 100vh;
}
.footer{
  height: 20vh;
  background-color: #fff2;
  padding: 100px;
}
.footer p{
  color: white;
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
      };
    },
    components: {
      BarraMenu,
      CategoriaComp,
    },
    methods: {
      async cargarDatos() {
        try {

          let respuesta = await ApiService.obtenerCategorias();
          this.categorias = respuesta.datos;
        } catch (error) {
          console.error('Error al cargar los datos:', error);
        }
      },
        abrirMenu(categ) {
          window.location.href = '/menu?categoria=' + categ;
        }
    },
    mounted() {
      this.cargarDatos();
    }
  };
  </script>
  