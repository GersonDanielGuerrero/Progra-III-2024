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
            <BotonComp @click="modalCategoria.visible = true">Agregar categoría</BotonComp>
        </div>
        
    </div>
    <b-modal class="modal-categoria" v-model="modalCategoria.visible" :title="modalCategoria.accion + 'categoría'">
      <form>
        <div class="form-group">
          <label for="nombre">Nombre</label>
          <input v-model="modalCategoria.categoria.nombre" type="text" class="form-control" id="nombre" placeholder="Nombre de la categoría">
        </div>
        <div class = "form-group">
          <label for="imagen">Imagen</label>
          <!--Imagen anterior-->
          <div v-if="modalCategoria.accion === 'Editar' && modalCategoria.categoria.imagen && !modalCategoria.categoria.nuevaImagen">
            <img :src="modalCategoria.categoria.imagen" alt="Imagen de la categoría" class="img-thumbnail" width="200">
          </div>
          <!--Imagen nueva-->
          <div v-else-if ="modalCategoria.categoria.nuevaImagen">
            <img :src="modalCategoria.categoria.nuevaImagen" alt="Imagen de la categoría" class="img-thumbnail" width="200">
          </div>
            <input type="file" class="form-control-file" @change="cambioImagenCategoria" accept="image/*">
        </div>
      </form>
      <template #footer>
        <BotonComp @click="guardarCategoria">Guardar</BotonComp>
        <BotonComp @click="modalCategoria.visible = false">Cancelar</BotonComp>
      </template>
    </b-modal>
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
import BotonComp from '@/components/BotonComp.vue';
import CategoriaComp from '@/components/CategoriaComp.vue';
  
  export default {
    data() {
      return {
        modalCategoria: {
          visible: false,
          accion: 'Editar',
          categoria: {
            id: 6,
            nombre: 'burgers',
            imagen: 'https://th.bing.com/th/id/R.c691ed37c9ce3040c3ebd2892e88870c?rik=QUBcFflN%2b9oqPQ&pid=ImgRaw&r=0',
            nuevaImagen: null,
            archivoNuevaImagen: null
          }
        },
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
      BotonComp,
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
        },
        cambioImagenCategoria(event){
          const archivo = event.target.files[0];
          this.modalCategoria.categoria.archivoNuevaImagen = archivo;

          if(archivo){
            const reader = new FileReader();
            reader.onload = (e) => {
              this.modalCategoria.categoria.nuevaImagen = e.target.result;
            };
            reader.readAsDataURL(archivo);
          }
          else{
            this.modalCategoria.categoria.nuevaImagen = null;
          }
        },
        guardarCategoria(){
          if(this.modalCategoria.accion === 'Agregar'){
            this.categorias.push(this.modalCategoria.categoria);
          }
          else{
            const index = this.categorias.findIndex(categoria => categoria.id === this.modalCategoria.categoria.id);
            this.categorias[index] = this.modalCategoria.categoria;
          }
          this.modalCategoria.visible = false;
        }
    },
    mounted() {
      this.cargarDatos();
    }
  };
  </script>
  