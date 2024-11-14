<template>
    <div>
    <CajaTexto type="text" v-model="busqueda" placeholder="Buscar..." @input ="buscar"/>
    </div>
</template>

<style scoped>

</style>
<script>
import CajaTexto from './CajaTexto.vue';
export default {
    name: 'BusquedaComp',
    components: {
        CajaTexto,
    },
    data() {
        return {
            busqueda:"",
        };
    },
    props: {
        
    },
    methods: {
        buscar(){
            
        }
    },
}
</script>