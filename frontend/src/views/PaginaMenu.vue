<template>
    <div class ="container-fluid ">
        <div class="barra-menu row">

        </div>
        <div class="buscador row ">
            <button class="btn-regresar col-1" >
                Regresar
            </button>
            <h2 class="col-2 ">MENU DE {{ categoria.toUpperCase() }}</h2>
            <span class="col-4 linea"/>
            <div class="col-4">
            <CajaTexto placeholder="Filtrar" type="text" v-model="filtro"/>
            </div>
            <BotonComp  class="col-1">Filtro</BotonComp>
            
        </div>
        <div class ="lista-productos row">
            <div class = "col-2" v-for="producto in productos" :key="producto.id">
                <ProductoComp :producto="producto"/>
            </div>
        </div>
    </div>
</template>

<style scoped>
*{
    font-family: 'Arial Black', sans-serif;
}
.linea{
    background-color: #ffad00;
    height: 5px;
    border-radius: 1px;
    align-self: center;
}
.container-fluid{
    margin: 0;
    border: 0;
    padding:0;
    width: 100%;
}
.barra-menu{
    background-color: coral;
    height: 50px;
    width: 100%;
}
.btn-regresar{
    background-color: #ffad00;
    height: 45px; 
    align-content: center;
}
.buscador h2 {
    font-size: 18px;
    text-align: left;
    color: #ffad00;
    padding: 5px 10px;
    align-content: center;
}
.buscador{
    padding: 20px 15px;
}
.lista-productos{
    padding: 20px;
}
</style>

<script>
import BotonComp from '@/components/BotonComp.vue';
import CajaTexto from '@/components/CajaTexto.vue';
import ProductoComp from '@/components/ProductoComp.vue';

export default {
    name: 'PaginaMenu',
    components: {
        ProductoComp,
        BotonComp,
        CajaTexto,
    },
    data() {
        return {
            categoria: 'burgers',
            productos:[
            {
            id:1,
            nombre:"Cheeseburger",
            tipo_descuento:"porcentaje",
            descuento:0,
            url_foto:"https://th.bing.com/th/id/OIP.JGigDSijh-lKRw6YaZQGVwHaDs?w=342&h=174&c=7&r=0&o=5&pid=1.7"
            },
            {
            id:2,
            nombre:"Doble carne",
            tipo_descuento:"porcentaje",
            descuento:0,
            url_foto:"https://th.bing.com/th/id/OIP.IDr8Ipp1_QAlSbQIiw5YegHaHa?rs=1&pid=ImgDetMain"
            },
            ]
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