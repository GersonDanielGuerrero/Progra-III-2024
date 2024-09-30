<template>
    <div class="container">
        <div class="logo">
            <img src="../../public/imagenes/logo_color.png" alt="Good Burguer Logo" />
        </div>
        <form class="register-form">
            <CajaTexto 
            v-bind:placeholder="'Nombres'"
            v-bind:icon-src="''">
            </CajaTexto>

            <CajaTexto
            v-bind:placeholder="'Apellidos'"
            v-bind:icon-src="''">
                
            </CajaTexto>

            <CajaTexto
            v-bind:placeholder="'Correo Electronico'"
            v-bind:icon-src="''"
            v-bind:is-half="true">
            </CajaTexto>

            <CajaTexto
            v-bind:placeholder="'Contraseña'"
            v-bind:icon-src="''">
            </CajaTexto>

            <CajaTexto 
            v-bind:placeholder="'Confirmar Contraseña'"
            v-bind:icon-src="''">
            </CajaTexto>

            <BotonComp v-bind:label="'Registrar'" v-bind:icon-src="''"></BotonComp>
        </form>
    </div>
</template>

<style scoped>
.container{
    text-align: center;
}

.logo img{
    width: 150px;
    margin-bottom: 20px;
}

.register-form{
    width: 400px;
    background-color: #000;
    padding: 20px;
    border-radius: 8px;
}
</style>

<!-- C U I D A D I T O -->

<script>
import BotonComp from '@/components/BotonComp.vue';
import CajaTexto from '@/components/CajaTexto.vue';
export default {
    name: 'RegistroUsuario',
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