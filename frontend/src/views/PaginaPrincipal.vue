<template>
    <div>
        <CategoriaComp :categoria = "categoria"/>
        <img src="../../public/iconos/logo_icono.svg"/>
        <HelloWorld msg="Pagina Principal"/>
    </div>
</template>

<style scoped>
    

</style>

<!-- C U I D A D I T O -->

<script>
import CategoriaComp from "@/components/CategoriaComp.vue";
import HelloWorld from "@/components/HelloWorld.vue";
export default {
    name: 'PaginaPrincipal',
    components: {
        HelloWorld,
        CategoriaComp
    },
    data() {
        return {
            categoria:{
                nombre: 'Bebidas',
                imagen: 'https://th.bing.com/th/id/OIP.gT9pclNP37-ncOXukl9l2QHaHa?rs=1&pid=ImgDetMain'
        }
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