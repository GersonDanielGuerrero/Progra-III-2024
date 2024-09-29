<template>
    <div>
        <button 
        :id="btnRegister" 
        class="btn-register"
        @click="metodoClick">Registrar
    <i class="icon" v-if="icon">{{ icon }}</i></button>
    </div>
</template>

<style scoped>
    .btn-register {
        background-color: #ffad00;
        color: #000;
        border: none;
        padding: 10px;
        cursor: pointer;
        width: 200px;
        margin-top: 20px;
        border-radius: 5px;
    }

    .btn-register i.icon {
        margin-right: 10px;
        color: #fff;
    }

    .btn-register:hover {
        opacity: 0.9;
    }



</style>

<!-- C U I D A D I T O -->

<script>
export default {
    name: 'BotonComp',
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