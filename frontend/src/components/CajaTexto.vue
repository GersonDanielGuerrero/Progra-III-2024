<template>
    <div class="input-group">
    <input :type="type" :placeholder="placeholder" />
    <i class="icon" v-if="icon">{{ icon }}</i>
    </div>
</template>

<style scoped>
    .input-group {
position: relative;
margin-bottom: 15px;
width: 100%;
}

.input-group input {
width: 100%;
padding: 10px;
padding-right: 40px;
background-color: rgba(255, 255, 255, 0.3);
border: none;
border-radius: 5px;
color: #000;
}

.input-group input::placeholder {
color: #ffad00;
}

.input-group i.icon {
position: absolute;
right: 10px;
top: 50%;
transform: translateY(-50%);
color: #ffad00;
}

</style>

<!-- C U I D A D I T O -->

<script>
export default {
    name: 'CajaTexto',
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